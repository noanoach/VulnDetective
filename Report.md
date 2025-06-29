# VulnDetective - Work Report

## Background

This exercise aimed to build a CLI tool that analyzes C/C++ code for security vulnerabilities using a local LLM.

The goal was to:
- Parse a C/C++ source file.
- Send the code to an LLM.
- Receive vulnerability analysis.
- Display the results clearly to the user.

---

## Technology Choices & Process

### Language

I chose **Python** because:
- Quick to develop CLI tools (argparse).
- Simple file I/O handling.
- Good ecosystem for integration with APIs and subprocess calls.

---

### LLM Model

The exercise mentions:
- Microsoft’s phi-4
- gemma3:1b

During research I discovered:
- **phi-4 does not exist publicly** for download.
- **gemma3:1b also does not exist** under that exact name.

Therefore, I selected **Gemma 2B** from Google:
- Available on Hugging Face in GGUF format.
- Suitable for local inference using llama.cpp.

---

### Running the Model

I first attempted to integrate with **Ollama**:
- Easy local LLM serving.
- However, failed due to 401 errors when trying to pull Gemma from Hugging Face, even after token authentication.

Hence, I switched to **downloading Gemma manually** via Hugging Face CLI and using **llama.cpp** for local inference.

---

### Project Structure

My project structure is:

```
/VulnDetective
│
├── analyzer.py         # CLI tool
├── llm_client.py       # Code handling LLM requests
├── parser.py           # Code splitting & response parsing
├── README.md           # Documentation
├── Report.md           # This report
├── requirements.txt    # Python dependencies
└── .gitignore
```

---

### Implementation Details

- Created a CLI using `argparse`.
- Read the code file from the filesystem.
- Sent the code snippet as a prompt to the LLM.
- Printed the LLM analysis to the console.

Planned improvements:
- Parse LLM responses into structured JSON.
- Extract line numbers and vulnerability types for clearer output.

---

## Challenges

- **Unavailable models:** phi-4 and gemma3:1b do not exist publicly.
- Gated access required for Gemma on Hugging Face.
- Time-consuming downloads for large models (~2.4GB).
- Integration issues between Ollama and Hugging Face gated models.

---

## Summary

Despite the challenges, I built a working CLI that:
- Integrates with a local LLM.
- Accepts C/C++ code as input.
- Outputs a vulnerability analysis.

The tool runs successfully using Gemma 2B via llama.cpp, and provides a solid foundation for future development.

Next steps:
- Structured parsing of LLM output.
- Support additional languages and LLM models.
- Enhance the CLI with richer reporting features.
