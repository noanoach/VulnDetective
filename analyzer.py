import argparse
from llm_client import analyze_code

def main():
    # Create an argument parser for command-line interface
    parser = argparse.ArgumentParser(
        description="Analyze C/C++ code for vulnerabilities using an LLM."
    )
    
    # Add a required argument: path to the C/C++ source file
    parser.add_argument(
        "path",
        help="Path to the C/C++ source file to analyze"
    )
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Read the contents of the source code file
    with open(args.path, "r") as f:
        code = f.read()

    # Send the code to the LLM for analysis
    analysis = analyze_code(code)

    # Print the results to the console
    print("\n--- Vulnerability Analysis ---\n")
    print(analysis)

# Entry point for the script
if __name__ == "__main__":
    main()
