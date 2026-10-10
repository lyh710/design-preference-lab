# Why this project exists: the two Canva roles

This is the starting brief for the learning programme. Read it before choosing
lessons or changing project direction. The learner's applications to these two
roles prompted the project; the broader goal is lasting ability to conduct
hands-on generative-AI research, regardless of either application outcome.

Role requirements below are concise paraphrases of the linked Canva postings,
reviewed on **10 October 2026**. Preserve this dated context if listings disappear;
record new evidence explicitly when requirements change.

## Principal Research Scientist – Evaluations

**Canva, Sydney · Job ID 4459354951 · [Original posting](https://www.linkedin.com/jobs/view/4459354951/)**

The role sets evaluation direction across research teams. It calls for measures
that reflect human experience and product outcomes, including when automated
judges disagree with people. Important areas include preference rubrics, rater
agreement and cultural differences; judge bias and benchmark contamination;
learned visual-quality models; reward modelling; and diagnosing regressions during
training. It explicitly distinguishes a useful evaluator from a suitable reward
for optimisation. Communication, mentoring, shared standards and decisions under
uncertainty are part of the role, alongside technical measurement work.

**Implication for this project:** demonstrate how an evaluator is validated,
where it fails, and when it should or should not drive model improvement.

## Senior Research Scientist – Design Generation (Sydney)

**Canva, Sydney · Job ID 4460307145 · [Original posting](https://www.linkedin.com/jobs/view/4460307145/)**

The role owns scoped generative-design research from question to validated result.
It emphasises practical training and fine-tuning of language and multimodal models,
data pipelines, training objectives, multi-GPU experimentation, useful quality
metrics, failure analysis and clear communication of trade-offs. Applying a
pretrained model alone is insufficient for its stated training emphasis. Diffusion
or image-generation experience is a bonus; language and multimodal-model depth are
the central requirements.

**Implication for this project:** personally run and debug training, compare
alternatives, and explain data/objective choices and their observed consequences.

## Learner starting point and priorities

These are learner-provided facts and goals, not claims inferred from the job ads:

- Experienced PhD/data-science research leader with substantial LLM evaluation
  experience; has not yet personally trained or fine-tuned generative models.
- Wants practical understanding of language and multimodal training, LoRA/QLoRA,
  diffusion, distributed training, human preferences and reward modelling.
- Wants to use coding agents for engineering support while personally owning
  the hypotheses, important technical decisions and interpretation of evidence.
- Wants a working app and reproducible public research materials that support
  interview discussions and independent research beyond these applications.

Build on existing evaluation expertise. Give early priority to actual training
and learned multimodal evaluation. A long sequence of template comparisons or UI
features would leave the main hands-on gap unresolved. Local work on the current
Mac comes first; environment details and spending boundaries are in
[learning-state.md](learning-state.md).

## How the project connects both roles

**Research question:** can we improve generated designs, and establish whether
the evaluator used to guide improvement reflects what people value?

| Planned work | Learning and portfolio evidence | Main role connection |
| --- | --- | --- |
| Current template app | Inspectable outputs, repeatable checks and a human-comparison workflow | Shared experiment foundation |
| Tiny local model, then LoRA | Real training runs, inspected loss/masks, checkpoint reload, failure analysis | Design Generation |
| Quantised adaptation and controlled comparisons | Memory/quality trade-offs and tests on unseen brief families | Design Generation |
| Visual preference evaluator | Human-agreement study, disagreement slices and evaluator limitations | Evaluations |
| Optimise against the evaluator | Check whether score gains survive independent human judgement | Both; evaluator versus reward distinction |
| Later diffusion and multi-GPU experiments | Bounded hands-on reproductions and honest scale limitations | Broader multimodal and training depth |

These are our chosen learning methods, not a claim that every named technique
is explicitly required by the postings. See [the roadmap](learning-roadmap.md)
for the sequence, and [learning-state.md](learning-state.md) for actual progress.

## What success means

For each substantive experiment, the learner can explain the question, data,
objective, implementation choices, observed results, limitations and next test.
The repo preserves commands, configurations, safe artifacts and a short research
memo. Assess engineering completion and learner understanding separately.

A working template app is only the starting point. Small local experiments can
demonstrate learning and judgement; they do not establish industrial-scale
training experience, Principal-level organisational impact, or interview success.
Record negative results honestly. Each lesson should name the capability above
that it develops and the evidence needed to show progress.
