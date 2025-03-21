import os

def save_to_file(content, filename):
    """Save generated content to a file."""
    os.makedirs("output", exist_ok=True)
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
