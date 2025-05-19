def build_prompt(error_log: str, code_context: dict) -> str:
    prompt = f"""
You are an expert DevOps engineer and senior Python developer.

Below is a CI/CD failure log followed by a code snippet.
Your task is to identify the root cause of the failure and provide a **minimal fix**.

---

📌 Example:
Error log: NameError: name 'math' is not defined

```python
def area(r):
    return math.pi * r ** 2
