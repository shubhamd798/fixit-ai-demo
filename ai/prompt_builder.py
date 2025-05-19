def build_prompt(error_log: str, code_context: dict) -> str:
    prompt = f"""
You are an expert DevOps engineer and senior Python developer.
Below is a CI/CD failure log followed by a code snippet.
Identify the root cause and suggest a fix.

--- ERROR LOG ---
{error_log}

--- CODE CONTEXT ---
Filename: {code_context['file']}
Line: {code_context['line']}
Code:
{code_context['snippet']}

---
✅ Please fix the code **without changing unrelated logic, renaming functions, or deleting the existing structure**.
✅ Keep the fix minimal and relevant to the error shown.
✅ Output only the updated code snippet (no explanation).
"""
    return prompt.strip()
