# Lightweight code execution tool for safe python snippet execution
import textwrap, subprocess, tempfile, os, sys

class CodeExecTool:
    async def run_python(self, code: str):
        """
        Runs the given python code safely in a subprocess.
        Returns stdout, stderr, and return code.
        """
        code = textwrap.dedent(code)

        with tempfile.NamedTemporaryFile("w+", suffix=".py", delete=False) as f:
            f.write(code)
            f.flush()
            file_path = f.name

        try:
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {"error": str(e)}
        finally:
            try:
                os.remove(file_path)
            except:
                pass
