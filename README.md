# aipm-skills

AI PM skills for structured product thinking and AI product PRD creation.

This repository contains Codex/Claude-style skills for AI product managers. The skills are designed to help with two different stages of work:

- Think through a problem with the right framework before jumping into execution.
- Produce realistic, usable AI product PRDs without inventing unknown facts.

## Skills

| Skill | Purpose | Use when |
| --- | --- | --- |
| `aipm-thinking` | Selects structured thinking frameworks and guides problem analysis | You need to reason through strategy, business model, product opportunity, prioritization, root cause, risk, or stakeholder alignment |
| `aipm-prd` | Drafts, completes, reviews, or improves AI product PRDs | You need a real AI product requirements document covering model choice, prompt design, evaluation, data, launch, risks, and acceptance criteria |

## `aipm-thinking`

`aipm-thinking` acts as a thinking-framework router. It chooses a suitable method based on the problem type instead of forcing every question into one fixed template.

Supported framework groups include:

- Strategy: SWOT, PESTLE, Porter Five Forces, scenario planning.
- Business: Business Model Canvas, Value Proposition Canvas, unit economics.
- Product: JTBD, user journey, Kano, RICE, ICE, MoSCoW.
- Decision and risk: decision matrix, risk matrix, premortem, Delphi, DACI, RACI.
- Problem solving: 5 Whys, fishbone diagram, MECE, first principles, systems thinking.

Example prompts:

```text
Use $aipm-thinking to help me analyze whether we should enter the enterprise training market.
```

```text
Use $aipm-thinking to choose the right framework for prioritizing these AI product features.
```

## `aipm-prd`

`aipm-prd` helps produce AI product PRDs. It is optimized for AI/LLM product work, including:

- Why the product needs an AI model instead of rules, traditional ML, or manual workflow.
- Requirement priority and dependency design.
- Model-selection process and constraints.
- Prompt strategy and prompt version management.
- Training data, knowledge data, and evaluation sets.
- Output quality control, hallucination governance, safety, and stability.
- Prototype interaction states for waiting, uncertainty, feedback, exceptions, and human intervention.
- Data flywheel, launch strategy, cost monitoring, rollback, and risk controls.

The skill is intentionally strict about truthfulness. It should not invent model names, competitor facts, costs, metrics, launch dates, or evaluation scores. When important information is missing, it should ask the user targeted questions first. If the user asks for a draft anyway, unknowns are marked as `待确认` or `假设`.

Example prompts:

```text
Use $aipm-prd to create a PRD for an AI course creation website.
```

```text
Use $aipm-prd to review this AI customer-service PRD and identify missing launch risks.
```

## Recommended Workflow

Use the two skills together:

1. Start with `aipm-thinking` when the problem is vague, strategic, or still needs framing.
2. Move to `aipm-prd` after the product direction, scope, and key assumptions are clear.
3. Use `aipm-thinking` again for specific decisions, such as prioritization, risk analysis, or business model choices.

## Repository Structure

```text
aipm-skills/
├── aipm-thinking/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
└── aipm-prd/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    ├── scripts/
    └── evals/
```

## Word Output

`aipm-prd` includes a small no-dependency Markdown-to-Word converter:

```bash
python3 aipm-prd/scripts/markdown_to_docx.py input.md output.docx
```

It supports headings, paragraphs, lists, fenced code blocks, and simple Markdown tables.

## Validation

Each skill can be validated with the `skill-creator` quick validation script:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py ./aipm-prd
python3 /path/to/skill-creator/scripts/quick_validate.py ./aipm-thinking
```

## Design Principles

- Frameworks serve the problem; do not stack methods for decoration.
- Ask targeted questions before filling important unknowns.
- Separate `已确认`, `假设`, `待确认`, and `建议`.
- Do not present uncertain information as fact.
- Prefer practical outputs that can support real PM decisions.
