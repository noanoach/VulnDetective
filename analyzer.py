import argparse
from llm_client import analyze_code

def main():
    parser = argparse.ArgumentParser(description="Analyze C/C++ code for vulnerabilities using an LLM.")
    parser.add_argument("path", help="Path to C/C++ source file")
    args = parser.parse_args()

    # קראי את הקובץ
    with open(args.path, "r") as f:
        code = f.read()

    # הריצי את המודל
    analysis = analyze_code(code)

    # הדפיסי את התוצאה
    print("\n--- Vulnerability Analysis ---\n")
    print(analysis)

if __name__ == "__main__":
    main()
