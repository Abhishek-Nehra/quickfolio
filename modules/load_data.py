from json import load as ld

from pathlib import Path

data_file = Path(__file__).parent.parent / "data/data.json"

print(data_file)
def load() -> dict:
    with open(data_file,"r") as file:
        return ld(file)