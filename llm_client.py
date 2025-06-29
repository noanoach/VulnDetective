"""
llm_client.py

This module handles communication with a local Large Language Model (LLM) 
running via llama.cpp.

It provides a function to:
- Send C/C++ source code snippets as prompts to the LLM.
- Receive a textual analysis of potential security vulnerabilities.

Instead of relying on Ollama or external APIs, it uses subprocess calls 
to run llama.cpp locally, ensuring full offline operation once the model 
has been downloaded.

Dependencies:
- llama.cpp compiled binary available in the same directory as this script.
- gemma-2b-it.gguf model file in the project directory.

Usage:
    from llm_client import analyze_code

    result = analyze_code("void foo() { char buf[10]; strcpy(buf, input); }")
    print(result)
"""

import subprocess

def analyze_code(code_snippet: str) -> str:
    
    # Compose the prompt to analyze the code
    prompt = (
        "Analyze the following C/C++ code and list potential security vulnerabilities, "
        "line numbers if possible, and explanations:\n\n"
        + code_snippet
    )

    # Run llama.cpp executable via subprocess
    result = subprocess.run(
        [
            "./main", 
            "-m", 
            "./gemma-2b-it.gguf",
            "-p",
            prompt
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"llama.cpp failed:\n{result.stderr}")

    # Return only the stdout
    return result.stdout.strip()
