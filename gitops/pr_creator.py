import os
import shutil
import subprocess
from git import Repo, Actor
from utils.config import (
    GITHUB_REPO,
    GITHUB_BRANCH,
    GITHUB_TOKEN,
    GIT_AUTHOR_NAME,
    GIT_AUTHOR_EMAIL
)

# Force-delete even locked .git files
def handle_remove_readonly(func, path, exc):
    import stat
    os.chmod(path, stat.S_IWRITE)
    try:
        func(path)
    except Exception as e:
        print(f"⚠️ Still couldn’t delete: {path} — {e}")

def create_pull_request(suggested_fix: str) -> str:
    repo_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git"
    branch_name = GITHUB_BRANCH

    tmpdir = os.path.abspath("build/repo")

    # Clean the directory forcibly
    if os.path.exists(tmpdir):
        try:
            shutil.rmtree(tmpdir, onerror=handle_remove_readonly)
        except Exception as e:
            print(f"❌ Could not remove existing repo dir: {e}")
            raise

    os.makedirs(tmpdir, exist_ok=True)

    # Clone
    repo = Repo.clone_from(repo_url, tmpdir)
    repo.git.checkout('-b', branch_name)

    # Save file
    file_path = os.path.join(tmpdir, "app.py")
    with open(file_path, "w") as f:
        f.write(suggested_fix)

    # Commit
    repo.git.add("app.py")
    author = Actor(GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL)
    repo.index.commit("fix: automated patch from FixIt.AI", author=author)

    # Push using subprocess
    subprocess.run([
        "git", "push", "--force",
        f"https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git",
        branch_name
    ], cwd=tmpdir, check=True)

    return f"https://github.com/{GITHUB_REPO}/pull/new/{branch_name}"
