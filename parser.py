# parser.py

"""
Helpers for:
- Splitting C/C++ code into smaller chunks (e.g. per function)
- Parsing the LLM response into structured data
"""

# לדוגמה, תתחילי לכתוב פונקציה כזו:

def split_code_into_chunks(code: str, max_lines: int = 50):
    """
    מחלק את הקוד לחתיכות בגודל X שורות.
    """
    lines = code.split('\n')
    for i in range(0, len(lines), max_lines):
        yield '\n'.join(lines[i:i+max_lines])
