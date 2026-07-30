from pathlib import Path
import random

def main():
    print("Hi! Welcome to file-renamer!")
    full_path = Path.cwd()
    cut_path = Path(*full_path.parts[:3])
    while True:
        con_path = input("Write path after *User*: ")
        path = cut_path / con_path
        if path.is_dir():
            print(f"{path} is exist")
            break
        elif not path.is_dir():
            print(f"{path} is not exist")
    path = Path(path)
    print(path)

    for item_path in path.iterdir():
        if item_path.is_file():
            suff = item_path.suffix
            ran_count = random.randint(0,1000)
            item_path.rename(f"image_{ran_count}{suff}")
            file = Path(f'image_{ran_count}{suff}')
            file.move_into(path)

if __name__ == "__main__":
    main()
