import asyncio, logging
from memory.memory_bank import MemoryBank
from agents.research_agent import ResearchAgent
from agents.math_agent import MathAgent
from agents.diagram_agent import DiagramAgent
from agents.writer_agent import WriterAgent

logger = logging.getLogger("supervisor_agent")
logging.basicConfig(level=logging.INFO)

class SupervisorAgent:
    def __init__(self, session_id="session_1", tools=None, memory=None):
        self.session_id = session_id
        self.tools = tools or {}
        self.memory = memory or MemoryBank()
        # create agents with shared tools
        self.research = ResearchAgent(self.tools)
        self.math = MathAgent(self.tools)
        self.diagram = DiagramAgent(self.tools)
        self.writer = WriterAgent(self.tools)

    async def run(self, title, prompt):
        logger.info(f"Supervisor run for session={self.session_id}")
        # parallel: research, math, diagram
        research_task = asyncio.create_task(self.research.run(prompt))
        math_task = asyncio.create_task(self.math.run(prompt))
        diagram_task = asyncio.create_task(self.diagram.run(prompt))
        research_out, math_out, diagram_out = await asyncio.gather(research_task, math_task, diagram_task)
        # sequential: writer
        doc = await self.writer.run(title, research_out, math_out, diagram_out)
        # save metadata to memory
        doc_meta = {"title": title, "pdf_path": doc["pdf_path"], "summary": research_out.get("summary","")}
        doc_id = self.memory.save_document(self.session_id, doc_meta)
        logger.info(f"Document saved with id={doc_id}")
        return {"doc": doc, "doc_meta": doc_meta, "doc_id": doc_id}
