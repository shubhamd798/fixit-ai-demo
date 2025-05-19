import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


from cicd.pipeline_listener import check_pipeline_status
from logs.error_parser import extract_error_from_logs
from ai.prompt_builder import build_prompt
from ai.fixer_agent import get_fix
from gitops.pr_creator import create_pull_request


def run_fixit():
    print("\n🔧 Listening for CI/CD failures...")

    failure_info = check_pipeline_status()
    if not failure_info:
        print("✅ No failures detected.")
        return

    error_log = extract_error_from_logs(failure_info["log_url"])
    prompt = build_prompt(error_log, failure_info["code_context"])
    suggested_fix = get_fix(prompt)

    pr_url = create_pull_request(suggested_fix)
    print(f"✅ Fix submitted via PR: {pr_url}")


if __name__ == "__main__":
    run_fixit()
