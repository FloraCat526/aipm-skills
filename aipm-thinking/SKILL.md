---
name: aipm-thinking
description: Use this skill when the user needs to think through a business, product, strategy, decision, or complex problem using structured thinking frameworks. It selects suitable methods such as SWOT, PESTLE, Delphi, Business Model Canvas, 5 Whys, JTBD, RICE, ICE, Kano, MECE, Porter Five Forces, scenario planning, and risk matrix, then guides the user with framework-specific questions and outputs structured reasoning results.
---

# AI PM Thinking

Use this skill as a thinking-framework router. The goal is not to show off frameworks, but to help the user reason through a problem with the smallest useful method set.

## Core Workflow

1. Restate the user's problem in one sentence.
2. Identify the problem type: strategy, business model, product opportunity, prioritization, root-cause diagnosis, risk, consensus, or complex decomposition.
3. Select 1-2 suitable frameworks. Avoid stacking many frameworks unless the user explicitly asks for a workshop-style analysis.
4. Explain briefly why the selected framework fits the problem.
5. Ask framework-specific questions when key information is missing. Do not fabricate business facts, market data, user research, or evaluation results.
6. If the user asks to proceed immediately, mark unknowns as `待确认` or `假设` and continue.
7. Output structured thinking results, including insights, options, trade-offs, next steps, and validation questions.

## Framework Router

Read [references/framework-router.md](references/framework-router.md) when you need to choose a method.

Default routing:

- Strategy: SWOT, PESTLE, Porter Five Forces, scenario planning.
- Business model: Business Model Canvas, Value Proposition Canvas, unit economics.
- Product opportunity: JTBD, user journey, Kano, RICE.
- Prioritization: RICE, ICE, MoSCoW, Kano.
- Root cause: 5 Whys, fishbone diagram, causal loop.
- Risk: risk matrix, premortem, scenario planning.
- Consensus: Delphi, DACI, RACI.
- Complex decomposition: MECE, first principles, systems thinking.

## Reference Loading

Use only the relevant reference file:

- Strategy and external environment: [references/strategy-frameworks.md](references/strategy-frameworks.md)
- Business model and value proposition: [references/business-frameworks.md](references/business-frameworks.md)
- Product opportunity and prioritization: [references/product-frameworks.md](references/product-frameworks.md)
- Decisions, risks, and consensus: [references/decision-frameworks.md](references/decision-frameworks.md)
- Root-cause analysis and complex decomposition: [references/problem-solving-frameworks.md](references/problem-solving-frameworks.md)

## Truthfulness Rules

Separate:

- `已确认`: information provided by the user or supplied material.
- `假设`: working assumptions used to continue the analysis.
- `待确认`: missing facts that affect the conclusion.
- `建议`: recommendations derived from the framework, not verified facts.

Never invent market size, user pain severity, competitor position, financial numbers, conversion rates, strategic constraints, team capacity, or expert consensus.

## Question-First Behavior

If the problem is vague, ask 3-6 questions before applying a framework. Good questions clarify:

- What decision must be made?
- What goal or success metric matters?
- Who are the stakeholders or users?
- What constraints are fixed?
- What options are already on the table?
- What information is missing or disputed?

If the user provides enough context, proceed directly.

## Output Template

Use this default structure unless a framework has a more natural format:

```markdown
# 结构化思考结果

## 1. 问题定义
## 2. 已确认信息 / 假设 / 待确认
## 3. 选择的思考框架
## 4. 框架化分析
## 5. 关键洞察
## 6. 可选方案与取舍
## 7. 建议下一步
## 8. 待验证问题
```

For a workshop or decision memo, make the output more formal. For quick brainstorming, keep it concise.
