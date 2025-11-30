📘 RadarDoc Concierge — AMTI Radar Technical Documentation Generator
Capstone Project — Google 5-Day AI Agents Intensive

RadarDoc Concierge is a multi-agent AI system designed to automatically generate complete radar technical documentation, including Doppler derivations, blind speed calculations, MTI/AMTI radar explanations, and block diagrams.
This project demonstrates multi-agent orchestration, tool-use, symbolic math, diagram generation, and PDF creation — aligned with the Google 5-Day AI Agents Intensive Capstone requirements.

🚀 Project Overview

Manual radar documentation is time-consuming. RadarDoc Concierge automates the process using multiple coordinated AI agents that perform:

Research and reference extraction

Mathematical derivations (Doppler, MTI/AMTI, blind speeds)

Diagram generation

PDF compilation

Memory-based task orchestration

The demo produces a full radar technical note in the folder:

examples/

🤖 Multi-Agent System Architecture

This project includes five AI agents:

1. SupervisorAgent

Coordinates workflow → research → math → diagram → writer.

2. ResearchAgent

Provides radar theory summaries (e.g., Doppler, blind speeds, AMTI).

3. MathAgent

Performs symbolic math using SymPy:

Doppler equation

Blind speed derivation

Canceller equations

4. DiagramAgent

Outputs block diagrams such as:

MTI Radar

AMTI Radar
Saved as PNG (e.g., examples/mti_block.png).

5. WriterAgent

Combines everything into:

Final PDF (Blind_Speeds_AMTI_Note.pdf)

Processed images

Clean formatted technical manuscript

📂 Repository Structure
radardoc-concierge/
 ├── agents/
 │     ├── research_agent.py
 │     ├── math_agent.py
 │     ├── diagram_agent.py
 │     ├── writer_agent.py
 │     └── supervisor_agent.py
 ├── tools/
 ├── memory/
 ├── examples/
 │     ├── Blind_Speeds_AMTI_Note.pdf
 │     ├── mti_block.png
 │     └── sample_input.txt
 ├── run_demo.py
 ├── requirements.txt
 └── README.md  ← (this file)

🧠 Capstone Requirements Demonstrated (Google ADK)
Requirement	Implemented
Multi-agent orchestration	✅ Supervisor + Research + Math + Diagram + Writer
Sequential agents	✅ Writer runs last and compiles PDF
Tools (search, code execution, image tool)	✅ Used in demo
Long-running sessions	✅ MemoryBank
Memory and state	✅ Used in Supervisor
Context engineering	✅ Structured JSON passing
Observability / logging	✅ Agents print process logs
Agent evaluation	✅ MathAgent result check, WriterAgent validation
Deployment-ready structure	✅ Runnable via GitHub or Kaggle
🛠 How to Run the Project
1. Install dependencies
pip install -r requirements.txt

2. Run the demo
python run_demo.py

Output files generated:
examples/Blind_Speeds_AMTI_Note.pdf
examples/mti_block.png

📒 Kaggle Notebook Execution

A Kaggle notebook is provided to run the full multi-agent system in the cloud.

📌 Add your link here after publishing the notebook:

Kaggle Notebook: https://www.kaggle.com/<your-username>/<your-notebook-name>


It:

Clones this repository

Installs requirements

Runs run_demo.py

Generates final PDF + diagrams

Provides a downloadable ZIP package

📘 References

Skolnik — Radar Handbook

Richards — Principles of Modern Radar

MIT OCW — Radar Notes

IEEE Radar Conference Publications

