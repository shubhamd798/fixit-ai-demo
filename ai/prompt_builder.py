def build_prompt(error_log: str, code_context: dict) -> str:
    prompt = f"""
You are an expert DevOps engineer.
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
Provide a fixed code snippet only.
    """
    return prompt.strip()