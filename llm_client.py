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

# Path to llama.cpp 
MODEL_PATH = "../llama.cpp/build/bin/llama-cli"

# Path to your GGUF model file
MODEL_FILE = "./gemma-3-1b-it-q4_k_m.gguf"

# Default number of code lines per chunk (if you want to split long files)
CHUNK_SIZE = 200

def build_prompt(code_snippet: str) -> str:
    """
    Builds a strict prompt instructing the LLM to reply
    only in a specific format without explanations or additional text.
    """
    prompt = (
        "You are a strict security analysis assistant.\n"
        "You MUST follow these instructions EXACTLY and produce no extra text:\n\n"
        "1. Analyze the following C/C++ code for security vulnerabilities.\n"
        "2. If there are NO vulnerabilities, reply with EXACTLY this text (no quotes):\n"
        "No vulnerabilities found.\n\n"
        "3. Otherwise, reply ONLY with lines in this format:\n"
        "Line <line_number>: <Short description of the vulnerability>\n\n"
        "STRICT RULES:\n"
        "- Do NOT write explanations.\n"
        "- Do NOT write summaries.\n"
        "- Do NOT include example code.\n"
        "- Do NOT greet the user.\n"
        "- Do NOT write any heading, title, or introductory text.\n"
        "- Do NOT mention that you are an AI or assistant.\n"
        "- Reply ONLY with the vulnerability lines, or the exact text: No vulnerabilities found.\n\n"
        "Here is the code to analyze:\n\n"
        + code_snippet
    )
    return prompt


def analyze_code(prompt: str) -> str:
    """
    Analyzes the given C/C++ code using a local LLM
    and returns the model's output as a string.
    """

    process = subprocess.Popen(
        [
            MODEL_PATH,
            "-m",
            MODEL_FILE,
            "-n",
            "512",
            "--simple-io",
            "--no-display-prompt",
            "--no-warmup"
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Send the prompt via stdin and close stdin automatically (like pressing Ctrl+D)
    stdout, stderr = process.communicate(prompt)

    if stdout.strip() == "":
        print("⚠️ The model returned empty output!")
    else:
        print("✅ Model output:")
        print(stdout)

    if stderr.strip():
        print("⚠️ STDERR:")
        print(stderr)

    return stdout
