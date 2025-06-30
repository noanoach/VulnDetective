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
- Good ecosystem for integration with subprocess calls.

---

### LLM Model

The exercise mentions:
- Microsoft’s phi-4
- gemma3:1b

After research, I concluded:
- **phi-4 does not exist publicly** for download.
- **gemma3:1b** does not exist under that exact name.

Therefore, I selected **Gemma 3 1B IT** from Google:
- Available publicly on Hugging Face in GGUF format.
- Medium-sized (~760 MB), suitable for local inference.
- Supports a large context window of up to ~32,768 tokens.

---

### Running the Model

I integrated the model using **llama.cpp**, running fully offline:
- Downloaded `gemma-3-1b-it-q4_k_m.gguf` from Hugging Face.
- Built llama.cpp locally.
- Call the llama-cli binary directly via Python’s subprocess module.
- Tested both interactive and non-interactive modes to automate prompt submissions.

This approach avoids the need for cloud APIs like Ollama and ensures completely local operation.

---

### Project Structure

My project structure is:

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

- **Unavailable models:** phi-4 and gemma3:1b do not exist publicly under those names.
- Gemma 3 1B IT is chat-oriented and tends to produce verbose explanations instead of short, structured answers.
- Difficult to suppress interactive mode completely with certain llama.cpp flags.
- Time-consuming initial loading of the model during first run.
- Processing performance slower than expected on longer code inputs.
- Difficulty forcing the model to comply strictly with a minimal output format (even with detailed prompts).

---

## Summary

Despite these challenges, I built a working CLI that:
- Integrates with a local LLM via llama.cpp.
- Accepts C/C++ code as input.
- Outputs vulnerability analysis, although improvements are still needed to enforce precise output formatting.

The tool runs successfully using **Gemma 3 1B IT** via llama.cpp and provides a solid foundation for future development.

Next steps:
- Refine system prompts for stricter control over model output.
- Implement automated post-processing to strip unnecessary text.
- Consider experimenting with alternative LLMs optimized for instruction-following.
- Add richer reporting and visualization features to the CLI.
