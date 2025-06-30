import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"

def build_prompt(code_snippet: str, start_line: int) -> str:
    prompt = (
        "Analyze the following C or C++ code for actual security vulnerabilities.\n\n"
        "Your ONLY allowed reply must follow this format:\n\n"
        "Line <line_number>: <Short description of the vulnerability>\n\n"
        "Rules:\n"
        "- If there are no real vulnerabilities, reply exactly: No vulnerabilities found.\n"
        "- Only report lines that contain code which is actually vulnerable in the context of this program as written.\n"
        "- Do NOT report merely theoretical risks or recommendations if the code is safe as implemented.\n"
        "- Do NOT include explanations, summaries, or example code.\n"
        "- Do NOT write \"Answer:\" or any heading.\n"
        "- Reply ONLY with the list of lines as instructed.\n"
        "- Look for real issues like buffer overflows, out-of-bounds accesses, hardcoded secrets, unsafe input handling, format string vulnerabilities, integer overflows, or any other security vulnerabilities.\n\n"
        f"IMPORTANT:\n"
        f"- The code below starts at line number {start_line}. "
        "All line numbers in your output MUST correspond to the real line numbers in the original file.\n\n"
        "Here is the code to analyze:\n\n"
        + code_snippet
    )


    return prompt


def analyze_code(code_snippet: str, start_line: int = 1) -> str:
    """
    Sends code to the local LLM via Ollama and returns the response as string.
    """
    prompt = build_prompt(code_snippet, start_line)

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
        return f"⚠️ Failed to connect to Ollama server: {e}"

    if response.status_code != 200:
        return f"⚠️ Ollama server error {response.status_code}: {response.text}"

    data = response.json()
    result = data.get("response", "").strip()

    if not result:
        return "⚠️ The model returned empty output!"
    else:
        return result
