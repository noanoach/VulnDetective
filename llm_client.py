import ollama

def analyze_code(code_snippet: str) -> str:
    """
    Sends a C/C++ code snippet to the LLM and returns a textual analysis
    describing potential security vulnerabilities.
    """

    # System prompt to define the LLM's role and context
    system_prompt = (
        "You are a security expert analyzing C/C++ code for potential vulnerabilities."
    )

    # User prompt that includes instructions and the code snippet to analyze
    user_prompt = (
        f"Analyze the following C/C++ code and list any potential security "
        f"vulnerabilities. Include line numbers if possible and provide explanations:\n\n"
        f"{code_snippet}"
    )

    # Send the prompts to the local LLM via Ollama
    response = ollama.chat(
        model="gemma:1b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract the textual response from the model and return it
    return response["message"]["content"]
