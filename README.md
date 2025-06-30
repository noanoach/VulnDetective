# VulnDetective

**VulnDetective** 
is a command-line tool that analyzes C/C++ source code for potential security vulnerabilities using a local Large Language Model (LLM).  

This version works entirely locally with the **Gemma 2B** model downloaded from Hugging Face, and runs inference via **llama.cpp**.

---

## 🚀 Quick Start

### 1. Clone the Repository

Clone this project from GitHub:

```bash
git clone https://github.com/noanoach/VulnDetective.git
cd VulnDetective
```

Or if you're using SSH:

```bash
git clone git@github.com:noanoach/VulnDetective.git
cd VulnDetective
```

---

### 2. Install Python & Virtual Environment

Ensure Python 3 is installed.

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Python Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

### 4. Create a Hugging Face Account

Since **Gemma 2B** is a gated model, you must:

✅ Create a free account on Hugging Face.  
✅ Accept the license agreement for **Gemma 2B** here:

👉 [https://huggingface.co/google/gemma-2b-it-GGUF](https://huggingface.co/google/gemma-2b-it-GGUF)

---

### 5. Install Hugging Face CLI

Install the CLI tool (inside your virtual environment):

```bash
pip install huggingface_hub --break-system-packages
```

---

### 6. Login to Hugging Face

Run:

```bash
huggingface-cli login
```

Enter your token when prompted.  
Your token can be created here:

👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

### 7. Download the Gemma Model

Download the model directly into your project folder:

```bash
huggingface-cli download google/gemma-3-1b-it-GGUF gemma-3-1b-it-q4_k_m.gguf --local-dir ./ --local-dir-use-symlinks False

```

After downloading, you'll have:

```
./gemma-3-1b-it-q4_k_m.gguf

```

---

### 8. Install llama.cpp

Clone and compile llama.cpp:

#### Linux/macOS

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
```

#### Windows

Follow the Windows build instructions here:  
👉 [https://github.com/ggerganov/llama.cpp#build-windows](https://github.com/ggerganov/llama.cpp#build-windows)

---

### 9. Test llama.cpp

Run a test inference:

```bash
../llama.cpp/build/bin/llama-cli -m ./gemma-3-1b-it-q4_k_m.gguf -p "Hello!"

```

You should see a textual answer from the model.

---

### 10. Run VulnDetective

Once your environment is set up, run VulnDetective:

```bash
python analyzer.py path/to/your_file.c
```

Example output:

```
--- Vulnerability Analysis ---

Line 20: Possible buffer overflow due to unsafe use of strcpy().
Line 35: Potential use-after-free vulnerability detected.
```

---

## 🛠 Project Architecture and Design

The project is organized as follows:

```
/VulnDetective
│
├── analyzer.py         # CLI tool
├── llm_client.py       # Code handling LLM requests
├── parser.py           # Code splitting into manageable chunks
├── README.md           # Documentation
├── Report.md           # Project work report
├── requirements.txt    # Python dependencies
├── .gitignore
└── tests/              # Test C/C++ code samples
```

---
Enjoy analyzing your code securely with VulnDetective!