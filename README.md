# CC -> Build Your Own wc Tool

Inspired by Coding Challenges by John Crickett
https://codingchallenges.fyi/challenges/challenge-wc

This challenge is to build your own version of the Unix command line tool wc!

All about building own wc:
WC(1)                       General Commands Manual                      WC(1)

NAME
     wc – word, line, character, and byte count

Go to terminal -> do man wc -> check output

DESCRIPTION
     The wc utility displays the number of lines, words, and bytes contained
     in each input file, or standard input (if no file is specified) to the
     standard output.  A line is defined as a string of characters delimited
     by a ⟨newline⟩ character.  Characters beyond the final ⟨newline⟩
     character will not be included in the line count.
     
     A word is defined as a string of characters delimited by white space
     characters.  White space characters are the set of characters for which
     the iswspace(3) function returns true.  If more than one input file is
     specified, a line of cumulative counts for all the files is displayed on
     a separate line after the output for the last file.

# To clone the repository:
git clone <project url>

# Set up a virtual environment and install dependencies:
mac:
    create: python3 -m venv wc_tool_env 
    activate: source wc_tool_env/bin/activate # 
windows:
    wc_tool_env\Scripts\activate
    pip install -r requirements.txt

## Testing
Run tests using pytest: pytest tests/

# example
python wc_tool/wc.py -l -w example.txt

# Key Steps for Building a Custom wc Tool
1. Define the Functionalities: The Unix wc command typically provides:
    Line count (-l)
    Word count (-w)
    Character count (-c)

2. Set Up the Command-Line Interface (CLI):
    Use Python's argparse module to handle flags like -l, -w, and -c.
    Enable input from either files or standard input (stdin), as wc does.

3. Implement Core Counting Logic:
    Lines: Count newline characters ('\n').
    Words: Count space-separated words, which can be done by splitting on whitespace.
    Characters: Count the total characters in the input.

4. Output:
    Display each count based on the flags provided.
    If no flags are provided, display all counts as wc does.

5. Compose with Other Programs: 
    Design the tool to accept piped input or direct file paths, making it composable with other tools. 
    Using sys.stdin.read() allows for piped input.


1. Step 1: Choose and Set Up Your IDE/Editor
    Install an IDE/Editor: If you haven't chosen one yet, popular choices are:
        1. VS Code: Great for Python and supports a wide range of extensions.
        2. PyCharm: Powerful for Python, with debugging and testing tools.
        3. Vim/Nano: Lightweight, terminal-based editors if you prefer working in the command line.
    Configure Your IDE:
        Extensions: Install necessary extensions for syntax highlighting, linting (like Pylint for Python), and version control (like Git).
        Integrated Terminal: Set up an integrated terminal within your IDE for running scripts and tests directly.
        Testing Support: If you use VS Code, you might want to install the Python Test Explorer for test management.
2. Step 2: Set Up a Python Environment
    Create a Virtual Environment:
        Run: python3 -m venv wc_tool_env
    Activate it:
        macOS/Linux: source wc_tool_env/bin/activate
        Windows: wc_tool_env\Scripts\activate
    Install Necessary Packages:
        For basic CLI tools, no external libraries are needed. However, if you want to add testing frameworks:

3. Step 3: Set Up Project Structure:
    Organize your project in a way that makes testing and development easier. 

4. Step 4: Prepare for Testing
        1. Write initial testing
        2. Run following commands on terminal: pytest tests/

5. Step 5: Document Setup
    Create a README.md to explain how to set up and use the project, making it easier for others (or future you) to get started.


## LICENSE

[MIT LICENSE](LICENSE)
