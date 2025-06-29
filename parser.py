# parser.py

"""
Helpers for:
- Splitting C/C++ code into smaller chunks (e.g. per function)
- Parsing the LLM response into structured data
"""

def split_code_into_chunks(code: str, max_lines: int = 50):
    """
    Splits the given C/C++ code into smaller chunks,
    each containing up to max_lines lines.

    Args:
        code (str): The complete C/C++ source code as a single string.
        max_lines (int): The maximum number of lines per chunk.

    Yields:
        str: A string representing a chunk of the code.
    """

    # Split the code into individual lines
    lines = code.split('\n')

    # Loop through the lines in steps of max_lines
    for i in range(0, len(lines), max_lines):
        # Join the current chunk of lines back into a single string
        chunk = '\n'.join(lines[i:i + max_lines])
        yield chunk
