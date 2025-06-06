# AI Agents Guide / Notes

## Overview
Agents are systems that independently accomplish tasks on your behalf, using LLMs to dynamically direct their own processes and tool usage.

## Key Concepts

### Workflows vs Agents
- **Workflows**: Systems where LLMs and tools are orchestrated through predefined code paths
- **Agents**: Systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks

### Core Components
| Component | Description |
|-----------|-------------|
| **Model** | The LLM powering the agent's reasoning and decision-making |
| **Tools** | External functions or APIs the agent can use to take action |
| **Instructions** | Explicit guidelines and guardrails defining how the agent should behave |

## When to Use Agents

### Best Use Cases
Prioritize workflows that have previously resisted automation:

| Category | Description |
|----------|-------------|
| **Complex decision-making** | Workflows involving nuanced judgment, exceptions, or context-sensitive decisions (e.g., refund approval in customer service) |
| **Difficult-to-maintain rules** | Systems with unwieldy, extensive rulesets that are costly or error-prone to update (e.g., vendor security reviews) |
| **Heavy reliance on unstructured data** | Interpreting natural language, extracting meaning from documents, conversational interactions (e.g., processing insurance claims) |

### Considerations
- Use agents where you require conversation, autonomous action, and have clear success criteria
- Agents can be expensive because they are autonomous
- Agents trade latency and cost for better task performance
- Find the simplest solution possible first - only increase complexity when needed

### Common Applications
- **Customer Support**: Tools for customer data, order history, policies; automated actions like refunds/ticket updates
- **Coding Agents**: Development assistance and automation
- **Web Search**: Information gathering and research

## Implementation Guidelines

### Best Practices
- Start simple - many patterns can be implemented in a few lines of code using LLM APIs directly
- If using frameworks, understand the underlying code to avoid debugging issues
- Validate your use case meets the criteria before building an agent
- Consider if a deterministic solution might suffice

### Framework Considerations
- Frameworks simplify standard tasks but add abstraction layers
- Can obscure underlying prompts/responses, making debugging harder
- May encourage unnecessary complexity

## Resources

### Primary Resources
- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) 🥇
- [OpenAI: Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Anthropic Cookbook - Agent Patterns](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)

### Additional Resources
- [Video: AI Agents Deep Dive](https://youtu.be/LP5OCa20Zpg?si=-MewT4qxwmI7mOZx)
- [Weaviate: AI Agents Blog](https://weaviate.io/blog/ai-agents)

