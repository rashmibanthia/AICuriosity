### Resources
- https://www.anthropic.com/research/building-effective-agents
- https://youtu.be/LP5OCa20Zpg?si=-MewT4qxwmI7mOZx
- https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents

## Notes
- Use Agents where you require conversation, autonomous action and have clear success criteria (ie test cases)
- Agents can be expensive because they are autonomous

Usecases 
- Customer Support 

1. Tools can be integrated to pull customer data, order history, policies. 
2. Actions such as issuing refunds or updating tickets can be handled programmatically; and
3. Success can be clearly measured through user-defined resolutions. 


- Coding Agents
- Web Search 


### More Resources
https://weaviate.io/blog/ai-agents

----


### Notes - https://www.anthropic.com/engineering/building-effective-agents
(This is one the best article on AI Agents - 🥇🥇🥇)

> At Anthropic, we categorize all these variations as agentic systems, but draw an important architectural distinction between workflows and agents:
>
> Workflows are systems where LLMs and tools are orchestrated through predefined code paths.
> Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

<br/>

> **When (and when not) to use agents**

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

> When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

> **Frameworks**

> Frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

> We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.


