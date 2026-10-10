"""Pure template generation and transparent structural checks, without ML claims."""

import hashlib
import json
import random
import re
import textwrap
from html import escape
from typing import Any

SCHEMA_VERSION = 1
GENERATOR_VERSION = "templates-v1"
METRICS_VERSION = "geometry-v1"
LIMITS = {"title": 120, "details": 240, "cta": 60}
PALETTES = [
    ("#172c2b", "#f5f0df", "#c8ed87"),
    ("#29223d", "#fff4e4", "#fbbca6"),
    ("#12334e", "#f5f5ef", "#9fe2ed"),
]


def validate_brief(data: Any) -> dict[str, str]:
    if not isinstance(data, dict):
        raise ValueError("Brief must contain title, details and cta.")
    result = {}
    for key, limit in LIMITS.items():
        value = data.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError(f"{key} must contain 1–{limit} characters.")
        if any(
            ord(c) < 32 or 0xD800 <= ord(c) <= 0xDFFF or ord(c) in (0xFFFE, 0xFFFF) for c in value
        ):
            raise ValueError(f"{key} contains unsupported control characters.")
        result[key] = value.strip()
    return result


def stable_json(value: Any) -> str:
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False
    )


def generate_pair(brief: Any, seed: int) -> list[dict[str, Any]]:
    brief = validate_brief(brief)
    if type(seed) is not int or not 0 <= seed < 2**32:
        raise ValueError("Seed must be an integer from 0 to 4294967295.")
    background, foreground, accent = random.Random(seed).choice(PALETTES)
    designs = []
    for variant in (0, 1):
        elements = []
        positions = (
            [("title", 145, 210, 54), ("details", 405, 120, 23), ("cta", 660, 80, 24)]
            if variant == 0
            else [("title", 250, 210, 54), ("details", 110, 110, 23), ("cta", 660, 80, 24)]
        )
        for key, y, height, size in positions:
            elements.append(
                {
                    "role": key,
                    "text": brief[key],
                    "x": 48,
                    "y": y,
                    "width": 504,
                    "height": height,
                    "font_size": size,
                    "color": accent if key == "cta" else foreground,
                }
            )
        design = {
            "schema_version": SCHEMA_VERSION,
            "generator": GENERATOR_VERSION,
            "seed": seed,
            "variant": variant,
            "brief": brief,
            "width": 600,
            "height": 800,
            "background": background,
            "accent": accent,
            "elements": elements,
        }
        design["id"] = hashlib.sha256(stable_json(design).encode()).hexdigest()[:24]
        designs.append(design)
    return designs


def lines_for(element: dict[str, Any]) -> list[str]:
    # A deliberately visible approximation: glyph widths are not measured.
    count = max(1, int(element["width"] / (element["font_size"] * 0.56)))
    return textwrap.wrap(
        element["text"], width=count, break_long_words=True, break_on_hyphens=False
    )


def render_svg(design: dict[str, Any]) -> str:
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {design["width"]} {design["height"]}" role="img" aria-label="Event poster">',
        f'<rect width="100%" height="100%" fill="{design["background"]}"/>',
        f'<path d="M48 55 H552" stroke="{design["accent"]}" stroke-width="4"/>',
    ]
    for element in design["elements"]:
        weight = "700" if element["role"] == "title" else "400"
        parts.append(
            f'<text fill="{element["color"]}" font-family="Arial, sans-serif" font-size="{element["font_size"]}" font-weight="{weight}">'
        )
        for i, line in enumerate(lines_for(element)):
            baseline = element["y"] + element["font_size"] * (1 + 1.2 * i)
            parts.append(f'<tspan x="{element["x"]}" y="{baseline}">{escape(line)}</tspan>')
        parts.append("</text>")
    return "".join(parts) + "</svg>"


def contrast(a: str, b: str) -> float:
    def luminance(color: str) -> float:
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
            raise ValueError("Expected a six-digit hex color.")
        channels = [int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
        return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))

    low, high = sorted((luminance(a), luminance(b)))
    return (high + 0.05) / (low + 0.05)


def evaluate(design: dict[str, Any]) -> dict[str, Any]:
    elements = design["elements"]
    outside = sum(
        e["x"] < 0
        or e["y"] < 0
        or e["x"] + e["width"] > design["width"]
        or e["y"] + e["height"] > design["height"]
        for e in elements
    )
    overlaps = sum(
        a["x"] < b["x"] + b["width"]
        and b["x"] < a["x"] + a["width"]
        and a["y"] < b["y"] + b["height"]
        and b["y"] < a["y"] + a["height"]
        for i, a in enumerate(elements)
        for b in elements[i + 1 :]
    )
    overflow = sum(len(lines_for(e)) * e["font_size"] * 1.2 > e["height"] for e in elements)
    return {
        "version": METRICS_VERSION,
        "out_of_bounds": outside,
        "text_box_overlaps": overlaps,
        "estimated_text_overflow": overflow,
        "minimum_contrast": round(
            min(contrast(e["color"], design["background"]) for e in elements), 2
        ),
    }


def comparison(brief: Any, seed: int) -> dict[str, Any]:
    designs = generate_pair(brief, seed)
    return {
        "schema_version": SCHEMA_VERSION,
        "generator": GENERATOR_VERSION,
        "seed": seed,
        "brief": designs[0]["brief"],
        "designs": [{**d, "svg": render_svg(d), "metrics": evaluate(d)} for d in designs],
    }
