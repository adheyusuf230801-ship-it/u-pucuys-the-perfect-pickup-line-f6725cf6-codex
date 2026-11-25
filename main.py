import os
from pathlib import Path


LINE = "I'm trained to finish sentences, but I'd rather start something with you. Coffee?"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
