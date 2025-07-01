# VulnDetective

🔎 VulnDetective analyzes C/C++ source code for potential security vulnerabilities using a local Large Language Model (LLM) via Ollama.

---

## 🚀 What is this?

This project lets you:  
✅ Analyze your C or C++ code for vulnerabilities  
✅ Get short, precise vulnerability reports  
✅ Run everything locally without sending code to external servers

---

## ✅ Requirements

- Python 3.9+
- [Ollama](https://ollama.com/download) installed locally
- A pulled model (e.g. `gemma3:1b`)

---

## 📥 Installation

### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Running Ollama

Start the Ollama server locally:

```bash
ollama serve
```

If you see this error:

```
Error: listen tcp 127.0.0.1:11434: bind: address already in use
```

Check what is using the port:

```bash
lsof -i :11434
```

Then kill the process:

```bash
kill -9 <PID>
```

---

### Check available models

List your downloaded models:

```bash
ollama list
```

You should see something like:

```
NAME              SIZE
gemma3:1b         815 MB
```

If you haven’t downloaded the model yet, pull it:

```bash
ollama pull gemma3:1b
```

---

## 🔧 How to Use

Analyze a C or C++ file:

```bash
python analyzer.py path/to/your_file.c
```

Example:

```bash
python analyzer.py tests/test.c
```

Sample output:

```
--- Vulnerability Analysis ---

Line 5: Buffer overflow vulnerability due to unsafe strcpy usage.
Fix: Use strncpy with a proper size limit or ensure bounds checking before copying.

Line 8: Use of hardcoded password detected in code.
Fix: Store secrets securely outside the source code, e.g. in environment variables or secure vaults.

```

---

## 📦 Project Structure

```
VulnDetective/
├── requirements.txt         # Python dependencies required for running the tool
├── analyzer.py              # Main script to analyze C/C++ files for vulnerabilities
├── llm_client.py            # Handles communication with the Ollama LLM API
├── parser.py                # Utilities for splitting large code files into smaller chunks
└── other C/C++ source files # Your C/C++ code files to be analyzed.

```

---

## 📝 Models

By default, VulnDetective uses the following model:

```
gemma3:1b
```

If you want to change the model, edit the `MODEL_NAME` variable in `llm_client.py`:

```
MODEL_NAME = "gemma3:1b"
```

---

## ⚠️ Notes

- Ensure your system has enough RAM to run your chosen model.
- VulnDetective sends your prompt locally to Ollama and does **not** require an internet connection once the model is downloaded.

---

## 🎉 enjoy
