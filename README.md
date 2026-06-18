# RegistrarDSL: University Money & Database Management

Welcome to the **RegistrarDSL** project! This is a Domain Specific Language (DSL) built using ANTLR4 and Python, specifically designed to handle university registrar work.

## What is RegistrarDSL?

A Domain Specific Language (DSL) is a programming language or specification language dedicated to a particular problem domain, a particular problem representation technique, and/or a particular solution technique. Unlike general-purpose languages like Python or Java, RegistrarDSL uses simple, English-like syntax targeted purely at managing university students and finances.

This project uses:
*   **Lexer**: Breaks raw input into tokens (like words in a sentence).
*   **Parser**: Takes tokens and builds a structure, ensuring syntax is correct (like checking grammar).
*   **Parse Tree**: The resulting structure of the parsed syntax.
*   **Visitor**: An algorithm that traverses the parse tree to execute actual Python code based on the commands.

## Architecture

```text
DSL Script (test_commands.txt) 
      |
      v
   Lexer (Tokenizes commands)
      |
      v
   Parser (Checks grammar and builds Parse Tree)
      |
      v
   Parse Tree
      |
      v
   Visitor (RegistrarEvalVisitor)
      |
      v
   Interpreter (Updates database.py)
      |
      v
   Output (Console results)
```

## Setup Instructions

### 1. Prerequisites
You need **Python 3** and **Java** (required to run the ANTLR generator) installed on your system.
You also need the ANTLR Python runtime:
```bash
pip install antlr4-python3-runtime
pip install antlr4-tools
```

### 2. Generate the Parser
Navigate to the `grammar/` directory and run ANTLR to generate the Python lexer and parser files:
```bash
cd grammar
antlr4 -Dlanguage=Python3 -visitor -no-listener Registrar.g4
```

### 3. Run the Project
Navigate to the `src/` directory and execute the main interpreter with a test script:
```bash
cd ../src
python main.py ../tests/test_commands.txt
```

## Available Commands

*   `ENROLL STUDENT <id> NAME "<name>" MAJOR "<major>"`
*   `DROP STUDENT <id>`
*   `PAY FEE <id> AMOUNT <number>`
*   `GRANT SCHOLARSHIP <id> AMOUNT <number>`
*   `SHOW STUDENT <id>`
*   `SHOW ALL STUDENTS`
*   `SHOW REVENUE`
*   `RESET`

## Example Usage

```text
ENROLL STUDENT 101 NAME "Alice Smith" MAJOR "Computer Science"
PAY FEE 101 AMOUNT 1500.50
SHOW STUDENT 101
SHOW REVENUE
```

Output:
```text
Successfully enrolled student: Alice Smith (ID: 101, Major: Computer Science)
Payment of $1500.50 received from student ID 101. Current Balance: $1500.50
Student Info:
  ID: 101
  Name: Alice Smith
  Major: Computer Science
  Balance: $1500.50
Total University Revenue: $1500.50
```
