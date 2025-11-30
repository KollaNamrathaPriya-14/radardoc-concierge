# run_demo.py
import asyncio
from agents.supervisor_agent import SupervisorAgent
from tools.image_tool import ImageTool
from tools.search_tool import SearchTool
from tools.code_exec_tool import CodeExecTool
from memory.memory_bank import MemoryBank

async def main():
    tools = {
        "image": ImageTool(out_dir="examples"),
        "search": SearchTool(),
        "code_exec": CodeExecTool()
    }
    memory = MemoryBank()
    sup = SupervisorAgent(session_id="demo_session", tools=tools, memory=memory)
    title = "Blind_Speeds_AMTI_Note"
    prompt = "Produce a technical note on blind speeds, AMTI radar, MTI delay-line canceller, including derivation and diagram."
    result = await sup.run(title, prompt)
    print("Done. PDF at:", result["doc"]["pdf_path"])
    print("Memory entries:", memory.list_documents("demo_session"))

if __name__ == "__main__":
    asyncio.run(main())
