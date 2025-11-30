import logging
from tools.search_tool import SearchTool

logger = logging.getLogger("research_agent")

class ResearchAgent:
    def __init__(self, tools=None):
        self.tools = tools or {}
        self.search_tool = self.tools.get("search") or SearchTool()

    async def run(self, prompt):
        logger.info("ResearchAgent started")
        # Simple simulated search call
        results = await self.search_tool.search(prompt)
        # Combine results into summary text
        summary = "\n".join([
            f"{r['title']}: {r['snippet']} ({r['url']})"
            for r in results
        ])
        return {"summary": summary, "references": results}
