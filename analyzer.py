import argparse
from llm_client import analyze_code
from parser import split_code_into_chunks

DEFAULT_MAX_LINES = 50

def analyze_entire_file(code: str):
    """
    Analyzes a complete code file in a single LLM request.
    Prints the vulnerability analysis result directly.
    """
    try:
        result = analyze_code(code, start_line=1)
        print("\n--- Vulnerability Analysis ---\n")
        print(result)
    except Exception as e:
        print("Error while analyzing the entire file:")
        print(str(e))


def analyze_file_in_chunks(code: str, max_lines: int):
    """
    Splits the code into chunks and analyzes each chunk separately.
    Concatenates all results into a single final report.
    Prints the vulnerability analysis result directly.
    """
    try:
        chunks = list(split_code_into_chunks(code, max_lines=max_lines))
        all_responses = []

        for i, chunk in enumerate(chunks):
            start_line = i * max_lines + 1
            try:
                response = analyze_code(chunk, start_line=start_line)
                all_responses.append(response)
            except Exception as e:
                print(f"Error analyzing chunk starting at line {start_line}: {e}")

        final_report = "\n".join(all_responses)
        print("\n--- Vulnerability Analysis ---\n")
        print(final_report)
    except Exception as e:
        print("Error during chunked analysis:")
        print(str(e))


def main():
    """
    Entry point for the CLI.
    Decides whether to analyze the file as a whole or in chunks,
    depending on its length.
    """
    parser = argparse.ArgumentParser(
        description="Analyze C/C++ code for vulnerabilities using a local LLM (Ollama)."
    )
    parser.add_argument(
        "path",
        help="Path to the C/C++ source file to analyze"
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=DEFAULT_MAX_LINES,
        help="Maximum lines per chunk for splitting large files (default: 50)"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=DEFAULT_MAX_LINES,
        help="Line count threshold above which splitting into chunks will happen (default: 50)"
    )
    args = parser.parse_args()

    try:
        with open(args.path, "r") as f:
            code = f.read()

        if not code.strip():
            print("The file is empty.")
            return

        num_lines = len(code.splitlines())

        if num_lines <= args.threshold:
            analyze_entire_file(code)
        else:
            analyze_file_in_chunks(code, args.max_lines)

    except FileNotFoundError:
        print(f"File not found: {args.path}")
    except Exception as e:
        print("Unexpected error occurred:")
        print(str(e))


if __name__ == "__main__":
    main()
