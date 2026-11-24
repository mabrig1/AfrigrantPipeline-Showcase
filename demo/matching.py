"""Independent fictional eligibility example; no network or AI calls."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Opportunity:
    name: str
    level: str | None
    subject: str | None

def screen(level: str, subject: str, opportunity: Opportunity) -> str:
    if not level.strip() or not subject.strip():
        raise ValueError("Applicant level and subject required")
    pairs = [(level, opportunity.level), (subject, opportunity.subject)]
    if any(required is not None and actual.casefold() != required.casefold() for actual, required in pairs):
        return "criteria mismatch"
    if any(required is None for _, required in pairs):
        return "needs review"
    return "potential match"

if __name__ == "__main__":
    for item in [Opportunity("Fictional A","masters","engineering"), Opportunity("Fictional B",None,"engineering")]:
        print(item.name, screen("masters","engineering",item))
