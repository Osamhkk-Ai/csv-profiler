from __future__ import annotations
from csv import DictReader
from pathlib import Path


def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    """Read a CSV as a list of rows (each row is a dict of strings)."""
    path=Path(path)
    if not path.exists():
        raise FileNotFoundError(f"There is no file with this path {path}")
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        reader = DictReader(f)
        for row in reader:
            print(row)
            rows.append(row)
    
    if not rows:
        raise ValueError("The CSV file is empty. Please check again.")
    
    return rows



# if __name__ == "__main__":

#     read_csv_rows("../data/sample.csv")
