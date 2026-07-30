from pathlib import Path
from func_rename import new_name
import random
import sys

def main():
    _, path, file_name = sys.argv
    path = Path(path)
    if path.is_dir():
        for item_path in path.iterdir():
            suff = item_path.suffix
            ran_count = random.randint(0, 10000)
            new_path = path / f"{file_name}{ran_count}{suff}"
            item_path.rename(new_path)
    else:
        print('Incorrect PATH')

if __name__ == "__main__":
    main()
