from pathlib import Path
import random
import sys

def main():
    try:
        _, path, file_name = sys.argv
        path = Path(path)
    except ValueError:
        print("Not enough values")
        return
    if path.is_dir():
        for item_path in path.iterdir():
            try:
                suff = item_path.suffix
                ran_count = random.randint(0, 10000)
                new_path = path / f"{file_name}{ran_count}{suff}"
                item_path.rename(new_path)
            except FileNotFoundError:
                print("File Not Found")
            except FileExistsError:
                print("File Exists")
    else:
        print("Incorrect PATH")
        
if __name__ == "__main__":
    main()
