# Best Practices for Cursor / Claude Rules

1. **Specify the Environment**  
   Always state which environment to use (e.g., Conda or uv). If you don’t, the model may attempt to install packages independently, leading to redundant or conflicting setups.

2. **Document API Key Locations**  
   Specify where API keys are stored or how they should be accessed. Without this, the model may generate unnecessary code for API keys and often doesn't work.

3. **Documentation**  
    Have claude generate `Claude.md` file for the work done. You can have multiple `Claude.md` files in multiple directories too. This serves as documentation for future. 

4. **Create a Project Context File (`Claude.md`)**  
   Maintain a `Claude.md` file in your project root. I use it to provide essential context, such as:
   - Project structure
   - Metrics
   - Datasets
   - Any other important information



---

**Resources/References:**

https://www.anthropic.com/engineering/claude-code-best-practices
