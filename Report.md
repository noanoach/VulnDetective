# VulnDetective - Work Report

## Background

This exercise aimed to build a CLI tool that analyzes C/C++ code for security vulnerabilities using a local Large Language Model (LLM).

The goal was to:

- Read a C/C++ source file.
- Send the code to an LLM as a prompt.
- Receive vulnerability analysis.
- Display the results clearly to the user.

---

## Technology Choices & Process

### Language

I chose **Python** because:

- Easy to build CLI tools (argparse).
- Simple file I/O handling.
- Mature ecosystem for HTTP requests and JSON handling.

---

### LLM Model

Originally, the exercise mentioned:

- Microsoft’s phi-4
- gemma3:1b

After research, I concluded:

- **phi-4** demands bigger RAM memory then I have available in my laptop.
- **gemma3:1b** does not exist under that exact name.

Therefore, I selected **Gemma 3 1B IT** from Google:

- Available publicly on Hugging Face in GGUF format.
- Medium-sized (~760 MB), suitable for local inference.
- Good context window (~32,768 tokens).
- Also available as an Ollama-compatible model.

---

### Running the Model

Initially, I integrated the model using **llama.cpp**, running fully offline:

- Downloaded `gemma-3-1b-it-q4_k_m.gguf` from Hugging Face.
- Built llama.cpp locally.
- Called the llama-cli binary directly via Python’s subprocess module.
- Handled interactive and non-interactive prompt modes.

However, I migrated the project to **Ollama** for better maintainability:

- Ollama runs a local HTTP server exposing REST APIs.
- Models like `gemma3:1b` are pulled via Ollama’s CLI.
- Ollama manages model loading, streaming, and optimizations internally.

---

## How VulnDetective Works (Process Explanation)

Here’s how the tool works in its current design:

1. **Read C/C++ Code from File**
    - The user runs the CLI with the path to a C or C++ source file.
    - Python reads the entire code into a string.
    - if the file is too big it divide it into chunks and then combines the results.

2. **Prepare Prompt for the LLM**
    - A strict prompt template is built, instructing the LLM to:
        - Search for vulnerabilities.
        - Respond only in a precise format:
            ```
            Line <line_number>: <short description of vulnerability>
            ```
        - Avoid explanations, summaries, or extra text.

3. **Send Prompt to LLM via Ollama**
    - A single HTTP POST request is sent to:
      ```
      http://localhost:11434/api/generate
      ```
    - The payload includes:
        - Model name (e.g. `gemma3:1b`).
        - The full text prompt.
        - A flag to disable streaming (so output returns as one block).

4. **Receive Response**
    - Ollama returns a JSON response with a single field:
      ```
      "response": "<the analysis text>"
      ```
    - No additional text is streamed if streaming is disabled.

5. **Print Analysis to Console**
    - The tool prints the LLM’s output directly to the terminal.
    - If no vulnerabilities exist, the LLM returns:
      ```
      No vulnerabilities found.
      ```

This fully satisfies the requested process:
- **Read file → send to LLM → get answer → display to user.**

---

## Project Structure

My current project structure:

```
VulnDetective/
├── requirements.txt         # Python dependencies required for running the tool
├── analyzer.py              # Main script to analyze C/C++ files for vulnerabilities
├── llm_client.py            # Handles communication with the Ollama LLM API
├── parser.py                # Utilities for splitting large code files into smaller chunks
└── other C/C++ source files # Your C/C++ code files to be analyzed (e.g. library.c, etc.)
```

---

## Example Run

Example command:

```bash
python analyzer.py tests/test.c
```

Example output:

```
--- Vulnerability Analysis ---

Line 5: Buffer overflow vulnerability due to unsafe strcpy usage.
Fix: Use strncpy with a proper size limit or ensure bounds checking before copying.

Line 8: Use of hardcoded password detected in code.
Fix: Store secrets securely outside the source code, e.g. in environment variables or secure vaults.

```

---

## Next Steps

- Improve prompt engineering for more concise outputs.
- Add JSON parsing for easier integration into pipelines.
- Test different models to improve accuracy and efficiency.
- Enhance the CLI UX with colored outputs or summaries.

---

# 🚀 Final Status

✅ VulnDetective successfully analyzes C/C++ code for security vulnerabilities using local LLMs via Ollama!
