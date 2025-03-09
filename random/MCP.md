**Motivation**

- Models are only as good as context provided to them 

**What**
- MCP standardizes how AI applications interact with external systems.
    - Prompts
    - Tools
    - Resources

MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. 
Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way 
to connect AI models to different data sources and tools.




**Resources**
- https://youtu.be/kQmXtrmQ5Zg?si=cT0u2wl2JSiqqTca

- https://modelcontextprotocol.io/introduction


---
---


### Install File System MCP Server with Claude Desktop 

File System MCP Server is pre built by Anthropic. 

Once installed we can use prompts in Claude Desktop like - "Which files can be deleted from my Downloads folder ? (do not delete them) I just want a list." 

From: https://www.anthropic.com/news/model-context-protocol
"The Model Context Protocol is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools."

So here data source is my local file system and Claude Sonnet 3.x is AI Powered tool


Follow instructions here - https://modelcontextprotocol.io/quickstart/user

There are multiple tools that come with MCP Server - Claude Desktop will be able to use all these tools.

---

### Sequential Thinking MCP Server in Cursor 

- https://smithery.ai/server/@smithery-ai/server-sequential-thinking

- What does following command do, when added to cursor - https://grok.com/share/bGVnYWN5_5266854d-3baa-49c3-8ae4-22d92703bb56 
```
npx -y @smithery/cli@latest run @smithery-ai/server-sequential-thinking --config "{}"
```