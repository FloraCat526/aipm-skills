# AI Product PRD Template

Use this reference when creating a full AI product PRD. Keep only sections relevant to the actual product; explicitly mark omitted sections as "不适用" with a reason when the omission could affect delivery.

Truthfulness rule: do not invent facts. If a value, model, competitor, metric, cost, date, or compliance requirement is unknown, first ask the user a question to resolve it. Only mark it as `待确认` or put it under `待确认问题` when the user asks for a draft before the answer is known. Use `假设` only when a working assumption is necessary and clearly label it as such.

## Interview Questions

Use these questions before writing the full PRD. Ask only the questions relevant to the user's request and keep each round short.

### Round 1: Scope And Value

- 目标用户是谁？他们现在用什么方式完成这个任务？
- MVP 首期必须解决哪 1-3 个核心场景？
- 这次产品要提升哪个业务指标或用户行为？
- 哪些能力明确不在首期范围内？

### Round 2: AI, Data, And Compliance

- AI 的输入是什么：用户文本、文件、图片、音频、数据库、第三方 API，还是以上组合？
- 是否已有候选模型、供应商或部署方式？如果没有，PRD 是否只定义选型流程？
- 是否有隐私、版权、数据出境、行业合规或内容安全要求？
- 是否有可用的知识库、样例数据、线上日志或评测集？

### Round 3: Quality, Cost, And Launch

- 什么样的输出算“可用”：人工采纳率、准确率、格式通过率、用户满意度，还是其他指标？
- 是否已有延迟、QPS、可用性、成本预算或 SLA 目标？
- 上线方式是什么：内部测试、小流量灰度、A/B Test，还是直接全量？
- 失败时需要怎样回滚或降级？

If the user cannot answer, put those unanswered items in `0.1 Confirmed Facts, Assumptions, And Open Questions` and keep related table cells as `待确认`.

## 0. Document Header

- Title: 大模型产品的需求文档（PRD）
- Feature or product name: `[VX.X.X] 产品/功能名称`
- Version rule: major version + feature iteration + minor update. A fourth digit is only for technical optimization without functional changes.

Revision table:

| 更新记录 | 修改人 | 修改时间 |
| --- | --- | --- |
| 初版/修订内容（待确认） | 待确认 | 待确认 |

## 0.1 Confirmed Facts, Assumptions, And Open Questions

Use this section near the top so readers know what is real and what still needs validation.

| 类型 | 内容 | 来源/负责人 |
| --- | --- | --- |
| 已确认 | 用户已提供的信息 | 用户/项目材料 |
| 假设 | 为推进初稿而做的工作假设 | PM 待确认 |
| 待确认 | 会影响范围、成本、合规、模型或上线的问题 | 负责人待确认 |

## 1. Background

Explain why this requirement exists. Classify the background into business value, user experience improvement, or problem fix.

### 1.1 Business Background

Describe the current business state, pain points, and opportunity.

### 1.2 Why Use a Large Model

Answer why this scenario must use a large model rather than rules, traditional ML, or manual workflow. Include the limitations of traditional approaches, the model's unique advantage in this scenario, and expected ROI.

### 1.3 Competitive Analysis

| 竞品名称 | 技术方案 | 模型选型 | 核心差异 | 效果水平 |
| --- | --- | --- | --- | --- |
| 待确认竞品 | 待确认 | 待确认 | 待调研 | 待评测 |

Do not fill competitor rows with invented products or unverifiable claims. If no competitor research is provided, write the analysis framework and list the research questions instead.

### 1.4 Product Goals

- Business goal:
- Model goal:
- User experience goal:

## 2. Requirement Description

Briefly describe the requirement so readers understand the scope and priorities. Use `P0`, `P1`, and `P2`; `P0` is the highest priority.

### 2.1 Requirement List

| 序号 | 优先级 | 需求点 | 需求简述 |
| --- | --- | --- | --- |
| 1 | P0 |  | Include summary and dependency with other requirements |

### 2.2 Requirement Categories

Functional requirements: language understanding, generation capability, multi-domain support, tool use, or user workflow support.

Performance requirements:

| 指标 | 标准 | 说明 |
| --- | --- | --- |
| 首Token延迟 | 待确认 | 用户发出请求到看到第一个输出的时间 |
| 端到端延迟 P95 | 待确认 | 95% 请求的完整响应时间 |
| 并发支持 | 待确认 | 峰值并发量 |
| 可用性 | 待确认 | 月度服务可用性 |

Security requirements: user data security, privacy, encryption, access control, data residency, and sensitive output handling.

Data requirements:

- 埋点数据: execution path and user operation path.
- 正负 case 数据: examples that represent acceptable and unacceptable results.
- 业务数据: metrics used to verify product value.

## 3. Business Flow

Describe user-view operation steps or business flow. Use a flowchart or swimlane diagram when possible.

## 4. System Flow

Describe execution chains across systems, data, and actions. For AI products, explicitly mark:

- LLM 调用节点: model used and expected latency.
- 工具调用节点: external tools or APIs.
- 判断/路由节点: routing logic, such as intent classification.
- 人工介入节点: confirmation or manual edit points.
- 异常处理分支: timeout and error handling.

## 5. Model Selection

Model selection is a core AI product decision. Start from small models when validating; if effects are similar, prefer the lower-cost model.

### 5.1 Selection Constraints

| 约束维度 | 要求 | 说明 |
| --- | --- | --- |
| 推理成本预算 | 待确认 | Single-call cost ceiling |
| 延迟要求 | 待确认 | End-to-end response time |
| 部署方式 | 待确认 | Cloud API / private deployment; depends on compliance |
| 数据合规 | 待确认 | Data residency and privacy constraints |
| 许可协议 | 待确认 | Commercial availability and license constraints |
| 微调需求 | 待确认 | Whether domain fine-tuning or LoRA is required |

### 5.2 Candidate Model Comparison

| 维度 | 待确认候选模型1 | 待确认候选模型2 | 待确认候选模型3 |
| --- | --- | --- | --- |
| 参数量/上下文 | 待确认 | 待确认 | 待确认 |
| 推理成本 | 待确认 | 待确认 | 待确认 |
| 延迟表现 | 待实测 | 待实测 | 待实测 |
| 场景效果 | 待评测 | 待评测 | 待评测 |
| 许可协议 | 待确认 | 待确认 | 待确认 |
| 部署复杂度 | 待确认 | 待确认 | 待确认 |

Choose domain-specialized models based on requirement type, such as multimodal, digital human, or text. Compare similar-parameter models through blind tests and periodic validation. If the user has not provided candidate models or actual evaluation data, do not make a selection; list the selection method and mark the conclusion as pending.

### 5.3 Selection Conclusion

State the selected primary model, backup model for failover, estimated cost, and rationale only when confirmed by evaluation or user-provided constraints. Otherwise write:

- 主模型: 待确认
- 备用模型: 待确认
- 成本预估: 待确认，需基于 token 量、调用频次和供应商价格计算
- 选型前置条件: 候选模型清单、评测集、成本预算、合规要求

## 6. Prompt Engineering

Prompt is a core deliverable of an AI product and must be documented, versioned, and evaluated before release.

### 6.1 System Prompt Design

- Role definition: what role the model plays and its capability boundary.
- Output constraints: format, length, language style, and forbidden content.
- Core instruction: key task logic.
- System prompt example: paste the complete prompt or link to prompt version docs.

### 6.2 Prompt Strategy

| 策略 | 是否采用 | 说明 |
| --- | --- | --- |
| Few-shot 示例 | 是/否 | Example count, selection logic, dynamic/static |
| Chain-of-Thought | 是/否 | Whether to require visible reasoning. Avoid exposing hidden reasoning if not needed. |
| 结构化输出 JSON/XML | 是/否 | Output schema definition |
| 多步骤链式调用 | 是/否 | Orchestration logic; see system flow |

### 6.3 Prompt Version Management

| 版本 | 变更内容 | 评测集得分 | 上线状态 | 变更日期 |
| --- | --- | --- | --- | --- |
| v1.0 | 初始版本/待确认 | 待评测 | 待确认 | 待确认 |
| v1.1 | 优化方向待确认 | 待评测 | 待确认 | 待确认 |

Prompt changes must pass evaluation before gray release. Do not release unevaluated prompts directly.

## 7. Training Dataset

If fine-tuning or knowledge-base injection is not involved, simplify this section and state why.

| 数据类型 | 说明 | 示例 |
| --- | --- | --- |
| 知识类数据 | Domain terms, industry jargon, field definitions, background material |  |
| 参考示例 | Reference examples across scenarios |  |
| 约束条件 | What can be output, what cannot, and format rules |  |
| 正向数据 Good Case | Correct and excellent input-output pairs |  |
| 负向数据 Bad Case | Incorrect inputs and outputs |  |

## 8. Evaluation System

Evaluation is one of the most important assets for an AI product PM.

### 8.1 Evaluation Set Construction

Data sources:

| 来源方式 | 适用阶段 | 说明 |
| --- | --- | --- |
| PM人工构造 | MVP冷启动 | PM writes core cases from business understanding |
| 真实用户 query 采样 | 灰度/全量阶段 | Sample real requests from production logs |
| LLM批量生成 + 人工筛选 | 规模扩充阶段 | Generate candidate data, then manually review quality |
| 线上 Bad Case 回流 | 持续运营阶段 | Add production failures to the eval set |

Coverage guidance:

| 场景层级 | 说明 | 占比建议 | 示例 |
| --- | --- | --- | --- |
| 核心场景 | Most common user path | 70% | Standard Q&A, routine generation |
| 边界场景 | Abnormal input, extreme conditions | 20% | Long text, mixed language, special symbols, empty input |
| 对抗场景 | User intentionally bypasses limits | 5% | Prompt injection, role-play attack, forbidden output |
| 安全场景 | Safety-sensitive input | 5% | Sensitive content, compliance, private information |

Scale standard:

| 阶段 | 最低评测条数 | 说明 |
| --- | --- | --- |
| MVP验证 | 50-100 | Cover core scenarios |
| 灰度上线 | 200-500 | Cover all four scenario types |
| 全量上线 | 500+ | Expand continuously and review monthly |

### 8.2 Evaluation Dimensions

| 维度 | 分值 | 1分（差） | 3分（及格） | 5分（优秀） |
| --- | --- | --- | --- | --- |
| 准确性 | 0-5 | 事实错误、答非所问 | 基本正确，有小瑕疵 | 完全准确，信息丰富 |
| 完整性 | 0-5 | 严重遗漏关键信息 | 覆盖主要信息 | 全面覆盖，逻辑完整 |
| 格式规范 | 0-5 | 格式混乱，不可用 | 基本符合格式要求 | 格式标准，开箱即用 |
| 安全合规 | 0-5 | 出现违规/敏感内容 | 无违规内容 | 主动规避风险 |
| 表达质量 | 0-5 | 语句不通，难以理解 | 表达清晰流畅 | 语言优秀，超出预期 |

Example score formula: `总分 = 准确性*30% + 完整性*25% + 格式规范*15% + 安全合规*20% + 表达质量*10%`.

Safety is a veto dimension: if safety compliance is `<= 2`, the case fails regardless of total score.

### 8.3 Evaluation Set Examples

Single-turn positive cases: input, expected output, scenario level, and type.

Single-turn negative cases: input, unexpected output, scenario level, and failure type.

Multi-turn positive and negative cases: input/output sequence and type.

### 8.4 Evaluation Execution

| 方式 | 适用场景 | 成本 | 可靠性 |
| --- | --- | --- | --- |
| PM自评 | MVP quick validation | 低 | 中，有主观偏差 |
| 标注团队评测 | 灰度/全量阶段 | 中 | 高 |
| LLM-as-Judge 自动评测 | Daily regression and frequent iteration | 低 | 中，需要校准 |
| 人机混合盲测 | Image/text generation scenarios | 高 | 最高 |

Triggers:

- Prompt any change: run core subset `>= 50` cases.
- Model version upgrade: run full evaluation set.
- Production bad cases reach threshold: run special evaluation.
- Periodic regression: run full evaluation at least monthly.

Release gates:

| 阶段 | 达标线 | 说明 |
| --- | --- | --- |
| MVP上线 | 待确认 | Partial quality issues acceptable |
| 灰度发布 | 待确认 | Known issue list required |
| 全量上线 | 待确认 | Zero tolerance for safety |

### 8.5 Continuous Maintenance

- Bad Case 回流: add weekly production bad cases to evaluation set and label scenario level and failure cause.
- 场景扩展同步: add evaluation cases whenever feature scenarios expand.
- 版本管理: version evaluation sets, such as `eval_v1.0`.
- 定期清理: review quarterly and remove stale cases.

## 9. Quality and Stability Strategy

Define quality controls from model output to user-visible result.

### 9.1 Output Quality Control

| 控制手段 | 说明 | 是否采用 |
| --- | --- | --- |
| 结构化输出 Schema约束 | Require JSON/XML and validate through schema |  |
| 输出格式校验 + 自动重试 | Retry when format is invalid; max retries 待确认 |  |
| 后处理过滤 | Sensitive word filtering, length interception, format checks |  |
| 多次采样选优 | Sample N times, rank/score, choose best result |  |
| 规则引擎兜底 | When model cannot handle, use rules to give baseline response |  |

### 9.2 Hallucination Governance

| 治理手段 | 说明 | 适用场景 |
| --- | --- | --- |
| RAG引用溯源 | Output includes source citations for verification | Knowledge Q&A |
| Cross-check校验 | Use another model or knowledge base to fact-check | High-accuracy scenarios |
| 置信度评分 | Prompt or refuse when confidence is below threshold | General |
| "我不确定"机制 | The model states uncertainty instead of inventing answers | General |

### 9.3 Stability Engineering

| 策略 | 配置 | 说明 |
| --- | --- | --- |
| 超时阈值 | 待确认 | Trigger downgrade after timeout |
| 重试策略 | 待确认 | Exponential backoff to avoid cascading failure |
| 多模型 Failover | 待确认 | Switch automatically when primary is unavailable |
| 请求限流 | 待确认 | Queue when threshold exceeded |
| 缓存策略 | 待确认 | Reduce repeated calls, cost, and latency |
| 熔断机制 | 待确认 | Prevent incident spread |

### 9.4 Consistency Assurance

| 策略 | 说明 |
| --- | --- |
| Temperature / Top_p 控制 | Target values 待确认; choose based on product need and model/provider behavior. For some models, `do_sample=false` means greedy decoding and temperature/top_p are ignored. |
| Seed固定 | Use fixed seed for reproducible scenarios when provider supports it |
| 模型版本锁定 | Lock model version in production and evaluate before upgrade |
| Prompt变更灰度 | Traffic ratio and observation period 待确认 |

## 10. Prototype

AI prototypes should pay special attention to waiting experience, uncertainty handling, and feedback entry.

| 原型 | 序号 | 功能 | 交互说明 |
| --- | --- | --- | --- |
| 插入原型截图 | 1 |  | Interaction rule |

AI-specific interaction requirements:

| 交互场景 | 设计要求 |
| --- | --- |
| 等待/加载状态 | Long generation needs progress feedback, such as streaming output, progress bar, or phase hints |
| 结果不确定性 | Provide retry/regenerate, multiple candidates, or user choice |
| 用户反馈入口 | Add thumbs up/down, adopt/not adopt, and text feedback near AI output |
| 异常状态引导 | Provide user copy and guidance when timeout, refusal, or safety blocking occurs |
| 人工介入入口 | Provide handoff or manual edit when AI cannot satisfy the task |

## 11. AI Capability Boundaries

Clearly tell engineering and business stakeholders what the current model can and cannot do.

Can do:

- List verified capabilities in this scenario.

Cannot do:

- List known limitations, such as unsupported languages, unsupported formats, or insufficient accuracy in specific scenarios.

Known defects:

- List known issues not fixed in this version, with reason and planned fix version.

## 12. Data Flywheel and Iteration

Long-term competitiveness comes from data flywheel: user usage generates data, data drives model optimization, and optimization improves user experience.

### 12.1 User Feedback Collection

| 反馈类型 | 采集方式 | 说明 |
| --- | --- | --- |
| 显式反馈 | 点赞/踩、评分、文字反馈 | User actively expresses satisfaction |
| 隐式反馈 | 采纳率、编辑率、重试率、停留时长 | Infer satisfaction from behavior |

### 12.2 Monitoring and Alerts

| 监控指标 | 告警阈值 | 响应动作 |
| --- | --- | --- |
| 日均负反馈率 | 待确认 | Trigger bad-case analysis |
| 模型调用失败率 | 待确认 | Stability investigation |
| 平均响应时间 | 待确认 | Performance bottleneck review |
| 安全拦截率突增 | 待确认 | Check for new attack pattern |

### 12.3 Data Feedback Loop

Flow: 用户使用 -> 数据采集 -> Bad Case 标注 -> 评测集更新 -> 问题归因分析 -> 模型/Prompt优化 -> 效果提升.

Operations:

- Weekly: summarize production bad cases and classify failure causes.
- Monthly: assess whether prompt iteration or model upgrade is needed.
- Quarterly: review data flywheel efficiency.

## 13. Launch and Operation Plan

### 13.1 Gray Release or A/B Test

| 阶段 | 流量比例 | 持续时间 | 观察指标 | 进入下阶段条件 |
| --- | --- | --- | --- | --- |
| 内部测试 | Internal users | 待确认 | Availability, visible bugs | No P0/P1 issues |
| 小流量灰度 | 待确认 | 待确认 | Evaluation score, feedback rate | Release gate met |
| 扩大灰度 | 待确认 | 待确认 | Stability, cost | No abnormal fluctuation |
| 全量上线 | 100% | - | Full monitoring metrics | - |

### 13.2 Cost Monitoring

| 监控项 | 预算 | 告警阈值 |
| --- | --- | --- |
| 日均 Token 消耗 | 待确认 | 待确认 |
| 日均 API 调用次数 | 待确认 | 待确认 |
| 单次请求平均成本 | 待确认 | 待确认 |

### 13.3 Rollback Plan

Define rollback trigger, rollback steps, and impact assessment when online effect misses target or severe issues appear.

## 14. Risks and Countermeasures

| 风险类型 | 风险描述 | 概率 | 影响 | 应对策略 |
| --- | --- | --- | --- | --- |
| 模型效果风险 | Model effect below target in some scenarios | 待评估 | 待评估 | Prepare backup model and baseline solution |
| 模型服务风险 | API unstable or unavailable | 待评估 | 待评估 | Multi-model failover + cache |
| 安全风险 | Model outputs illegal or sensitive content | 待评估 | 待评估 | Multi-layer filtering + human review + safety eval set |
| 成本风险 | Actual traffic exceeds expected cost | 待评估 | 待评估 | Cost alerts + cache + rate limiting |
| 合规风险 | Data residency or privacy leak | 待评估 | 待评估 | Data residency architecture + privacy desensitization |

Risk probability and impact should be scored by the project team or based on incident/user data. Do not present default risk ratings as verified facts.

## Appendix

Terminology:

| 术语 | 解释 |
| --- | --- |
| Prompt | Input instruction text for a large model |
| Few-shot | Include examples in prompt to guide output |
| CoT | Chain-of-Thought; guide model reasoning. Do not expose hidden reasoning unless product explicitly needs visible reasoning. |
| RAG | Retrieval augmented generation, combining external knowledge with model output |
| Failover | Automatically switch to backup service when primary service fails |
| Temperature | Controls output randomness; lower value means more deterministic output |
| Token | The unit of model text processing; affects cost and latency |
| LLM-as-Judge | Use a model to evaluate another model's output |

Appendix B: link evaluation set files, such as Excel or CSV.

Appendix C: link complete prompt version management documentation.
