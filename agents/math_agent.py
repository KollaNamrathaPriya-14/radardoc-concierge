import sympy as sp
import logging
from tools.code_exec_tool import CodeExecTool

logger = logging.getLogger("math_agent")

class MathAgent:
    def __init__(self, tools=None):
        self.tools = tools or {}
        self.exec_tool = self.tools.get("code_exec") or CodeExecTool()

    async def run(self, prompt):
        logger.info("MathAgent started")

        # Symbolic variables
        v, lam, T, n = sp.symbols('v lambda T n')

        # Blind speed formula (simplified symbolic derivation)
        # v_n = n * lambda / (2 * T)
        v_n = sp.simplify(n * lam / (2*T))
        derivation_str = f"Derived blind speed general term:\n\nv_n = {sp.pretty(v_n)}"

        # Numeric test example through code execution
        code = f"""
import sympy as sp
n = 1
lam = 0.03   # meters
T = 0.001    # seconds
v = n * lam / (2*T)
print('Calculated blind speed v_n =', v)
"""

        exec_result = await self.exec_tool.run_python(code)

        return {
            "derivation": derivation_str,
            "numeric_test": exec_result
        }
