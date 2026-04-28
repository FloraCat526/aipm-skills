---
name: aipm-prd
description: Use this skill to draft, complete, review, or improve PRDs for AI or large-model products. Trigger whenever the user mentions AI product PRD, large model requirements, prompt design, model selection, evaluation set, model rollout, AI capability boundaries, data flywheel, AI product launch plan, or asks a product manager to turn an idea into an AI product requirements document.
---

# AI PM PRD

Use this skill to produce product requirements documents for AI products, especially products built around LLMs, prompts, model selection, evaluation, quality controls, and rollout operations.

## Core Workflow

1. Clarify the product context only when missing: target user, scenario, business goal, existing workflow, data sources, compliance constraints, and launch scope.
2. Decide the document mode: new PRD, PRD completion, PRD review, or PRD rewrite.
3. For any AI capability, explicitly answer why a large model is needed instead of rules, traditional ML, or manual workflow.
4. Define requirements with priorities from `P0` to `P2`; mark dependencies between requirements.
5. Cover the AI-specific design sections: model selection, prompt engineering, training or knowledge data, evaluation, output quality control, hallucination governance, stability, prototype interaction, capability boundaries, data flywheel, launch plan, and risks.
6. End with measurable acceptance criteria and unresolved questions.

## Output Standards

Write in Chinese by default unless the user asks otherwise. The expected final output is a document. Prefer generating a Word `.docx` file; if the environment cannot create or attach a Word document, provide Markdown content instead.

Recommended document workflow:

1. Draft the PRD in Markdown first.
2. Save the Markdown as an intermediate `.md` file when creating a file output.
3. Convert it to `.docx` with `scripts/markdown_to_docx.py` when a Word file is requested or clearly useful.
4. If conversion fails, keep the Markdown output and explain the blocker briefly.

Use a PRD structure with clear numbered headings, tables where comparison or acceptance criteria are needed, and concrete placeholders when exact data is unavailable.

Avoid vague claims such as "improve experience" without measurable indicators. Prefer concrete metrics: first-token latency, end-to-end latency, P95, QPS, availability, evaluation score, bad-case rate, user feedback rate, cost per request, daily token budget, and rollback thresholds.

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
