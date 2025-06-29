import ollama

def analyze_code(code_snippet: str) -> str:
    """
    שולח קטע קוד למודל ומחזיר את הניתוח הטקסטואלי.
    """

    system_prompt = "You are a security expert analyzing C/C++ code for vulnerabilities."
    user_prompt = f"Analyze the following C/C++ code and list potential security vulnerabilities, line numbers if possible, and explanations:\n\n{code_snippet}"

    response = ollama.chat(
        model="gemma:1b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response["message"]["content"]
