# VulnDetective

🔎 VulnDetective analyzes C/C++ source code for potential security vulnerabilities using a local Large Language Model (LLM) via Ollama.

---

## 🚀 What is this?

This project lets you:  
✅ Analyze your C or C++ code for vulnerabilities  
✅ Get short, precise vulnerability reports  
✅ Run everything locally without sending code to external servers

Originally built for `llama.cpp`, now fully upgraded to work with **Ollama** and models like `gemma3:1b`.

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
Line 8: Use of hardcoded password detected in code.
```

---

## 📦 Project Structure

```
VulnDetective/
│
├── analyzer.py
├── llm_client.py
├── requirements.txt
└── tests/
     ├── test.c
     └── medium_test.cpp
```

---

## 📝 Models

By default, VulnDetective uses the following model:

```
gemma3:1b
```

If you want to change the model, edit the `MODEL_NAME` variable in `llm_client.py`:

```python
MODEL_NAME = "gemma3:1b"
```

---

## ⚠️ Notes

- Ensure your system has enough RAM to run your chosen model.
- For larger code files, consider splitting the code into smaller chunks.
- VulnDetective sends your prompt locally to Ollama and does **not** require an internet connection once the model is downloaded.

---

## 🎉 Status

✅ VulnDetective successfully analyzes C/C++ code for security vulnerabilities using local LLMs via Ollama!
