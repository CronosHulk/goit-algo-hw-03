import argparse
import shutil
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за розширенням.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("--destination", type=str, default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():
                file_extension = item.suffix[1:] if item.suffix else "no_extension"
                target_subdir = dest_dir / file_extension
                
                try:
                    target_subdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target_subdir)
                    print(f"Скопійовано: {item} -> {target_subdir / item.name}")
                except OSError as e:
                    print(f"Помилка при копіюванні файлу {item}: {e}")
    except FileNotFoundError:
        print(f"Помилка: Директорію не знайдено - {source_dir}")
    except PermissionError:
        print(f"Помилка: Немає доступу до директорії - {source_dir}")
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")

def main():
    args = parse_arguments()
    source_path = Path(args.source)
    destination_path = Path(args.destination)
    if not source_path.is_dir():
        print(f"Помилка: Вихідний шлях '{source_path}' не є директорією або не існує.")
        return
    print(f"Вихідна директорія: {source_path}")
    print(f"Директорія призначення: {destination_path}")
    copy_and_sort_files(source_path, destination_path)

# example:
# python task_1.py .\dir --destination .\dist

if __name__ == "__main__":
    main()
