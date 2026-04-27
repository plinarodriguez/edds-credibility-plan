from pathlib import Path

ROOT_DIR = Path(".")
OUTPUT_FILE = ROOT_DIR / "edds_credibility_plan.md"

ORDER = [
    "01_question_of_interest.md",
    "02_context_of_use.md",
    "03_risk_assessment.md",
    "04_credibility_goals.md",
]

def shift_headers(content: str) -> str:
    """
    Add one extra '#' to every markdown header line.
    """
    new_lines = []
    for line in content.splitlines():
        if line.strip().startswith("#"):
            new_lines.append("\n\n#" + line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def combine_markdown_files():
    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:
        outfile.write("# EDDS Credibility Plan\n\n The EDDS Credibility Plan defines the question of interest, context of use, risk, and evidence requirements for establishing confidence in the computational model.")
        for filename in ORDER:
            path = ROOT_DIR / filename
            content = path.read_text(encoding="utf-8").strip()
            content = shift_headers(content)
            outfile.write(content)
            # outfile.write("\n\n---\n\n")

    print(f"Combined markdown created: {OUTPUT_FILE}")

if __name__ == "__main__":
    combine_markdown_files()