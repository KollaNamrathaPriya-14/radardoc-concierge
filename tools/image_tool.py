# Simulated Image Tool - returns a local placeholder path
import os
from PIL import Image, ImageDraw

class ImageTool:
    def __init__(self, out_dir="examples"):
        os.makedirs(out_dir, exist_ok=True)
        self.out_dir = out_dir

    async def generate(self, prompt_text: str, size=(1024, 768), name_hint="diagram"):
        # Create a simple placeholder image
        fname = os.path.join(self.out_dir, f"{name_hint}.png")
        img = Image.new("RGB", size, color=(255,255,255))
        draw = ImageDraw.Draw(img)

        text = "Diagram Placeholder:\n" + prompt_text[:180]
        draw.multiline_text((20,20), text, fill=(0,0,0))

        img.save(fname)
        return fname
