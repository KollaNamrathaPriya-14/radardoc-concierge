import logging

logger = logging.getLogger("diagram_agent")

class DiagramAgent:
    def __init__(self, tools=None):
        self.tools = tools or {}
        self.image_tool = self.tools.get("image")  # expected to be ImageTool

    async def run(self, prompt):
        logger.info("DiagramAgent started")
        prompt_text = (
            "MTI radar block diagram: include transmitter, receiver, delay-line canceller, "
            "PRF control, and display. Label blocks clearly."
        )
        if self.image_tool is None:
            raise RuntimeError("Image tool not provided")
        image_path = await self.image_tool.generate(prompt_text, size=(1024, 512), name_hint="mti_block")
        caption = "MTI Radar Block Diagram (auto-generated placeholder)"
        return {"image_path": image_path, "caption": caption}
