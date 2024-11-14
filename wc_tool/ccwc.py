#!/usr/bin/env python3
import argparse
import sys

def count_lines(text):
    return text.count('\n')

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_bytes(text):
    return len(text.encode('utf-8'))


def main():
    parser = argparse.ArgumentParser(description="Custom ccwc tool")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help="File to process (default: standard input)")
    parser.add_argument('-l', '--lines', action='store_true', help="Count lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count words")
    parser.add_argument('--chars', action='store_true', help="Count characters")
    # parser.add_argument('-m', '--chars', action='store_true', help="Count characters (supports multibyte)")
    # parser.add_argument('-c', '--bytes', action='store_true', help="Count bytes in the file")
    parser.add_argument('-m', action='store_true', help="Count characters (supports multibyte)")
    parser.add_argument('-b', '--bytes', action='store_true', help="Count bytes in the file")


    args = parser.parse_args()

    # # Read text from file
    # try:
    #     with open(args.file, 'r', encoding='utf-8') as file:
    #         text = file.read()
    # except FileNotFoundError:
    #     print(f"File {args.file} not found.")
    #     sys.exit(1)

    # Read text from file or stdin -> changes made for piped commands/ read from standard input if no filename is specified
    text = args.file.read()

    # Calculate counts based on the flags
    results = []
    if args.lines:
        results.append(f"Lines: {count_lines(text)}")
    if args.words:
        results.append(f"Words: {count_words(text)}")
    if args.chars:
        results.append(f"Characters: {count_chars(text)}")
    if args.bytes:
        byte_count = count_bytes(text)
        results.append(f"{byte_count} {args.file}")

    # Default: if no flags are given, show all
    if not (args.lines or args.words or args.chars or args.bytes):
        results = [
            f"Lines: {count_lines(text)}",
            f"Words: {count_words(text)}",
            f"Characters: {count_chars(text)}",
            f"Bytes: {count_bytes(text)}\n{args.file}"
        ]

    print("\n".join(results))

if __name__ == "__main__":
    main()
