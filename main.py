#!/usr/bin/python3

import os
import re
import shutil
import argparse


def copy_presets_with_textures(basic_presets, custom_presets):

    # Очищаем директорию custom_presets
    if os.path.exists(custom_presets):
        shutil.rmtree(custom_presets)
    os.makedirs(custom_presets, exist_ok=True)

    # Шаблоны для поиска в файлах
    patterns = [
        re.compile(r'^warp_\d+=\`sampler\s', re.MULTILINE),
        re.compile(r'^comp_\d+=\`sampler\s', re.MULTILINE)
    ]

    total_files = 0
    copied_files = 0

    # Рекурсивно обходим директорию basic_presets
    for root, dirs, files in os.walk(basic_presets):
        for file in files:
            if file.endswith('.milk'):
                total_files += 1
                src_path = os.path.join(root, file)
                
                # Проверяем содержимое файла
                try:
                    with open(src_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if any(pattern.search(content) for pattern in patterns):
                            # Создаем относительный путь
                            rel_path = os.path.relpath(root, basic_presets)
                            dst_dir = os.path.normpath(os.path.join(custom_presets, rel_path))
                            
                            # Создаем директории, если их нет
                            os.makedirs(dst_dir, exist_ok=True)
                            
                            # Копируем файл
                            dst_path = os.path.join(dst_dir, file)
                            shutil.copy2(src_path, dst_path)
                            copied_files += 1
                except UnicodeDecodeError:
                    print(f"Ошибка чтения файла (не UTF-8): {src_path}")
                except Exception as e:
                    print(f"Ошибка при обработке файла {src_path}: {str(e)}")

    return total_files, copied_files


def main():
    parser = argparse.ArgumentParser(description='Копирование и преобразование .milk файлов')
    parser.add_argument('--basic', required=True, help='Путь к директории с исходными пресетами')
    parser.add_argument('--custom', required=True, help='Путь к директории для преобразованных пресетов')
    
    args = parser.parse_args()

    # Проверяем существование базовой директории
    if not os.path.isdir(args.basic):
        print(f"Ошибка: Директория {args.basic} не существует!")
        return

    total, copied = copy_presets_with_textures(args.basic, args.custom)
    print(f"Найдено .milk-файлов: {total}")
    print(f"Скопировано файлов, работающих с текстурами: {copied}")


if __name__ == "__main__":
    main()
    
