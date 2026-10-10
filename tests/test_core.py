import copy
import unittest
import xml.etree.ElementTree as ET

from design_lab import core

BRIEF = {
    "title": "Tomorrow, together",
    "details": "A community design evening · 18 October",
    "cta": "Reserve a place",
}


class CoreTests(unittest.TestCase):
    def test_seed_reproduces_distinct_variants(self):
        pair = core.generate_pair(BRIEF, 42)
        self.assertEqual(pair, core.generate_pair(BRIEF, 42))
        self.assertNotEqual(pair[0]["id"], pair[1]["id"])
        self.assertNotEqual(pair, core.generate_pair(BRIEF, 43))
        self.assertEqual(pair[0]["brief"], BRIEF)

    def test_rejects_invalid_inputs(self):
        for value in [
            None,
            [],
            {},
            {**BRIEF, "title": " "},
            {**BRIEF, "title": "a" * 121},
            {**BRIEF, "cta": 3},
            {**BRIEF, "title": "bad\x00text"},
        ]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                core.validate_brief(value)
        for seed in [True, -1, 2**32, 1.5, "1"]:
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                core.generate_pair(BRIEF, seed)

    def test_svg_is_parseable_and_escapes_user_markup(self):
        design = core.generate_pair({**BRIEF, "title": '<script>alert("x")</script> & hi'}, 1)[0]
        svg = core.render_svg(design)
        root = ET.fromstring(svg)
        self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        self.assertNotIn("<script>", svg)
        self.assertIn("&lt;script&gt;", svg)

    def test_metrics_detect_known_failures(self):
        design = copy.deepcopy(core.generate_pair(BRIEF, 1)[0])
        self.assertEqual(core.evaluate(design)["out_of_bounds"], 0)
        design["elements"][0]["x"] = -5
        design["elements"][1].update(
            {k: design["elements"][0][k] for k in ["x", "y", "width", "height"]}
        )
        design["elements"][0]["color"] = design["background"]
        design["elements"][0]["height"] = 1
        result = core.evaluate(design)
        self.assertGreater(result["out_of_bounds"], 0)
        self.assertGreater(result["text_box_overlaps"], 0)
        self.assertGreater(result["estimated_text_overflow"], 0)
        self.assertEqual(result["minimum_contrast"], 1.0)

    def test_contrast_reference_values(self):
        self.assertAlmostEqual(core.contrast("#000000", "#ffffff"), 21.0)
        self.assertAlmostEqual(core.contrast("#abcdef", "#abcdef"), 1.0)


if __name__ == "__main__":
    unittest.main()
