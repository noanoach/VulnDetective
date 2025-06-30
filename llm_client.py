"""
llm_client.py

This module handles communication with a local Large Language Model (LLM)
running via Ollama.

It provides a function to:
- Send C/C++ source code snippets as prompts to the LLM.
- Receive a textual analysis of potential security vulnerabilities.

Instead of relying on llama.cpp binaries, it uses HTTP requests to the
local Ollama server, making integration simpler.

Dependencies:
- Ollama installed and running locally (http://localhost:11434)
- A supported model pulled in advance (e.g. gemma3:1b)

Usage:
    from llm_client import analyze_code

    result = analyze_code("void foo() { char buf[10]; strcpy(buf, input); }")
    print(result)
"""

import requests

# URL to your local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"

# Name of the model you want to use in Ollama
MODEL_NAME = "gemma3:1b"

# Default number of code lines per chunk (if you want to split long files)
CHUNK_SIZE = 200

def build_prompt(code_snippet: str) -> str:
    """
    Builds a strict prompt instructing the LLM to reply
    only in a specific format without explanations or additional text.
    """
    prompt = (
        "Analyze the following C code for potential security vulnerabilities.\n\n"
        "Your ONLY allowed reply must follow this format:\n\n"
        "Line <line_number>: <Short description of the vulnerability>\n\n"
        "Rules:\n"
        "- If there are no vulnerabilities, reply exactly: No vulnerabilities found.\n"
        "- Otherwise, write one line per issue in the format:\n"
        "Line <line_number>: <Short description of the vulnerability>\n"
        "- Do NOT include explanations, summaries, or example code.\n"
        "- Do NOT write \"Answer:\" or any heading.\n"
        "- Reply ONLY with the list of lines as instructed.\n\n"
        "Here is the code to analyze:\n\n"
        + code_snippet
    )
    return prompt


def analyze_code(code_snippet: str) -> str:
    """
    Analyzes the given C/C++ code using a local LLM
    and returns the model's output as a string.
    """

    prompt = build_prompt(code_snippet)

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
    except requests.RequestException as e:
        print(f"⚠️ Failed to connect to Ollama server: {e}")
        return ""

    if response.status_code != 200:
        print(f"⚠️ Ollama server error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    result = data.get("response", "").strip()

    if not result:
        return "⚠️ The model returned empty output!"
    else:
        return result