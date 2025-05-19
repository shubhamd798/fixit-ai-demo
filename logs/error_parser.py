def extract_error_from_logs(log_file_path: str) -> str:
    try:
        with open(log_file_path, 'r') as f:
            lines = f.readlines()

        traceback = []
        for line in lines:
            if 'Traceback' in line or line.strip().startswith('File'):
                traceback.append(line.strip())
            elif 'Error' in line or 'Exception' in line or 'TypeError' in line:
                traceback.append(line.strip())

        if traceback:
            return "\n".join(traceback)
        else:
            return "No obvious error found in logs."

    except FileNotFoundError:
        return f"❌ Log file not found at {log_file_path}"