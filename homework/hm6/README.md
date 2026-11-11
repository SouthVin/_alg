# Lambda Calculus Interpreter

This repository contains a simple Lambda Calculus Interpreter implemented in Python. This project is part of the week 6 homework for the Introduction to Algorithms course.

## 📝 Features
- **Abstract Syntax Tree (AST)**: Represents lambda expressions using fundamental structures: Variables, Abstractions, and Applications.
- **$\alpha$-conversion (Alpha-conversion)**: Automatically handles variable renaming to prevent variable capture and naming conflicts during substitution.
- **$\beta$-reduction (Beta-reduction)**: Evaluates the expressions step-by-step using normal-order evaluation.
- **Step-by-step Output**: Prints the complete calculation process, showing the state of the expression at every step until it reaches the normal form.

## 🚀 How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository or download the `lambda_calculus.py` file.
3. Open your terminal or command prompt and run the following command:

```bash
python lambda_calculus.py