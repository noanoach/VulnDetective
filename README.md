# VulnDetective

VulnDetective is a CLI tool that analyzes C/C++ source code to detect potential security vulnerabilities using a local Large Language Model (LLM) via Ollama.

---

## 🚀 Quick Start

### 1. Install Ollama

Download and install Ollama from:

👉 [https://ollama.com/download](https://ollama.com/download)

Or on Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh

Verify the installation:
ollama --version

You should see:
ollama version v0.1.28

Download the Gemma 1B model: ollama pull gemma:1b
Or simply run it once to trigger the download: ollama run gemma:1b

Clone the Repository:
git clone git@github.com:noanoach/VulnDetective.git
cd VulnDetective

Create a Python Virtual Environment
Linux / macOS:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate


Install Python Dependencies
pip install -r requirements.txt

Run the Analyzer
Run the tool on a C or C++ file:
python analyzer.py path/to/your_file.c

Example output:
--- Vulnerability Analysis ---

Line 20: Possible buffer overflow due to unsafe use of strcpy().
Line 35: Potential use-after-free vulnerability detected.


Project Architecture and Design
The project is organized into several components for modularity and clarity:

/VulnDetective
│
├── analyzer.py         # CLI entry point, handles argument parsing
├── llm_client.py       # Handles communication with the local LLM (Gemma) via Ollama
├── parser.py           # Splits C/C++ code and processes LLM responses
├── README.md           # Project documentation
├── Report.md           # Detailed explanation of design decisions and process
├── requirements.txt    # Python dependencies
└── .gitignore          # Files and folders excluded from git

