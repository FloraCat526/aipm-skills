---
name: aipm-prd
description: Use this skill to draft, complete, review, or improve PRDs for AI or large-model products. Trigger whenever the user mentions AI product PRD, large model requirements, prompt design, model selection, evaluation set, model rollout, AI capability boundaries, data flywheel, AI product launch plan, or asks a product manager to turn an idea into an AI product requirements document.
---

# AI PM PRD

Use this skill to produce product requirements documents for AI products, especially products built around LLMs, prompts, model selection, evaluation, quality controls, and rollout operations.

## Core Workflow

1. Decide the document mode: new PRD, PRD completion, PRD review, or PRD rewrite.
2. Run a short PM interview before drafting when key facts are missing. Ask only the questions that materially affect scope, model choice, compliance, cost, launch, or acceptance criteria.
3. If the user answers, incorporate the answers as `已确认`. If the user says to proceed without answering, draft with `待确认`/`假设` labels.
4. For any AI capability, explicitly answer why a large model is needed instead of rules, traditional ML, or manual workflow.
5. Define requirements with priorities from `P0` to `P2`; mark dependencies between requirements.
6. Cover the AI-specific design sections: model selection, prompt engineering, training or knowledge data, evaluation, output quality control, hallucination governance, stability, prototype interaction, capability boundaries, data flywheel, launch plan, and risks.
7. Separate confirmed facts, assumptions, and open questions. End with measurable acceptance criteria and unresolved questions.

## Interview Before Drafting

Prefer asking targeted questions over filling the PRD with `待确认`.

When the user gives only a high-level idea, ask 5-8 concise questions first. Group questions by decision area and avoid overwhelming the user with the full template. If there are many unknowns, ask in rounds:

Round 1, scope and value:

- Who is the target user, and what exact task are they trying to complete?
- What is the MVP scope, and what is explicitly out of scope?
- What business metric should this PRD improve?

Round 2, AI and data:

- What input data or documents will the AI use?
- Are there candidate models/providers already chosen, or should the PRD define a selection process?
- Are there compliance, privacy, copyright, or data residency constraints?

Round 3, launch and quality:

- What quality bar defines "usable" output?
- What performance, cost, or availability targets are already known?
- What launch path is expected: internal test, beta/gray release, or direct full release?

If the user asks to generate the PRD immediately, include a short `待确认问题` section at the top and keep unknown values as `待确认`. Do not bury unresolved questions only at the end.

## Truthfulness And Clarification

This skill is for producing PRDs that can be used in real product work. Do not invent facts to make the document look complete.

Before drafting, identify missing information that would change product scope, model choice, compliance posture, cost, launch plan, or acceptance criteria. Convert those gaps into direct questions for the user. If the user wants a draft anyway, label unknowns explicitly as `待确认` or `假设`, and keep them in a dedicated section.

Never present uncertain content as fact. This applies especially to:

- Competitor names, competitor capabilities, market share, pricing, and benchmarks.
- Specific model names, model scores, latency, context length, cost, availability, licensing, or deployment constraints.
- Business metrics, traffic, QPS, conversion rate, budget, SLA, release dates, staffing, and compliance requirements.
- User research conclusions, customer pain points, legal constraints, or data-source availability that the user did not provide.

Use these labels consistently:

- `已确认`: directly provided by the user or found in supplied project material.
- `假设`: a reasonable working assumption made to keep the draft moving.
- `待确认`: important missing information that the PM or stakeholder must verify.
- `建议`: a product recommendation, not a verified fact.

For model selection, do not use fake rows such as "模型A/模型B" unless the user explicitly asks for a template. If model names or evaluation data are unknown, write the model-selection framework and mark candidates as `待确认候选模型`, or ask the user for the intended model/provider list.

For metrics, do not fabricate target values. If no baseline or target is available, write the metric definition and mark the target as `待确认`, with a recommendation for how to determine it.

## Output Standards

Write in Chinese by default unless the user asks otherwise. The expected final output is a document. Prefer generating a Word `.docx` file; if the environment cannot create or attach a Word document, provide Markdown content instead.

Recommended document workflow:

1. Draft the PRD in Markdown first.
2. Save the Markdown as an intermediate `.md` file when creating a file output.
3. Convert it to `.docx` with `scripts/markdown_to_docx.py` when a Word file is requested or clearly useful.
4. If conversion fails, keep the Markdown output and explain the blocker briefly.

Use a PRD structure with clear numbered headings and tables where comparison or acceptance criteria are needed. When exact data is unavailable, use explicit `待确认` placeholders instead of plausible-looking numbers or names.

Avoid vague claims such as "improve experience" without measurable indicators. Prefer concrete metric definitions: first-token latency, end-to-end latency, P95, QPS, availability, evaluation score, bad-case rate, user feedback rate, cost per request, daily token budget, and rollback thresholds. Only fill target values when provided or clearly derived; otherwise mark targets as `待确认`.

When the user asks for a full PRD, read [references/prd-template.md](references/prd-template.md) and follow the complete outline. When the user asks for a partial section, load only the relevant section from that reference.

## Word Document Generation

Use the bundled converter for simple Word output:

```bash
python3 scripts/markdown_to_docx.py input.md output.docx
```

The converter supports headings, paragraphs, unordered and ordered lists, fenced code blocks, and simple Markdown tables. For highly styled documents, create the content first and then improve formatting with a richer DOCX tool if available.

## AI Product Checks

Before finalizing, verify that the PRD answers:

- What problem is solved, and what user or business value proves it matters?
- Why does this scenario need an LLM or AI model?
- Which requirements are P0/P1/P2, and what dependencies exist?
- What model is selected, what alternatives were compared, and what constraints drove the decision?
- What prompt strategy, versioning, and evaluation gate protect release quality?
- What data is needed for prompting, RAG, fine-tuning, evaluation, or monitoring?
- How are hallucination, sensitive output, instability, timeout, failover, and cost controlled?
- What does the user see when AI is waiting, uncertain, wrong, blocked, or escalated to a human?
- What are the launch, gray release, monitoring, rollback, and data flywheel plans?

## Review Mode

When reviewing an existing AI PRD, focus on missing AI-specific sections and release risks. Return findings first, grouped by severity, then provide a concise patch plan or revised sections.

High-severity gaps include missing evaluation set, no safety gate, no rollback plan, no model fallback, undefined capability boundaries, no cost controls, or no explanation for why AI is necessary.

## Minimal Template

If the user asks for a quick PRD and does not need the full template, use this compact structure:

1. 背景与目标
2. 需求清单
3. 业务流程与系统流程
4. 模型选型与 Prompt 设计
5. 数据与评测体系
6. 质量保障与稳定性策略
7. 原型交互与能力边界
8. 数据飞轮与持续迭代机制
9. 上线运营、成本、风险与回滚
10. 验收标准与待确认问题
