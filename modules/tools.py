import os

OUTPUT_DIR = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_file(filename="new_file.txt"):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write("")
    return f"File created: {path}"

def write_code(filename="code.py", code="# Sample Python Code\nprint('Hello World')"):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    return f"Code written to: {path}"

def summarize_text(text):
    return text[:100] + "..."  # simple summary