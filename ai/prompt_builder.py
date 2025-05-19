def build_prompt(error_log: str, code_context: dict) -> str:
    prompt = f'''
You are an expert DevOps engineer and senior Python developer.

Below is a CI/CD failure log followed by a code snippet.
Your task is to identify the root cause of the failure and provide a minimal fix.

---

📌 Example:
Error log: NameError: name 'math' is not defined

Code:
def area(r):
    return math.pi * r ** 2

✅ Fix:
import math

def area(r):
    return math.pi * r ** 2

---

Now fix the following issue:

--- ERROR LOG ---
{error_log}

--- CODE CONTEXT ---
Filename: {code_context['file']}
Line: {code_context['line']}
Code:
{code_context['snippet']}

---

✅ Do not rename or delete functions.
✅ Fix only the part of the code causing the failure.
✅ Return only the fixed Python code block. No explanation.
'''
    return prompt.strip()
