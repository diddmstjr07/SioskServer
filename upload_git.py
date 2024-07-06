import subprocess

def run_git_command(directory, commands):
    try:
        subprocess.run(commands, cwd=directory, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {commands} in directory {directory}: {e}")
        raise

def main():
    commit_index = input("Commit 구문을 작성해주세요: ")

    try:
        run_git_command(".", ["git", "init"])
        run_git_command(".", ["git", "add", "."])
        run_git_command(".", ["git", "commit", "-m", commit_index])
        run_git_command(".", ["git", "push", "https://github.com/diddmstjr07/SioskServer.git", "main", "--force"])
    except subprocess.CalledProcessError:
        print("Failed to perform Git operations in the main directory.")
        return

if __name__ == "__main__":
    main()