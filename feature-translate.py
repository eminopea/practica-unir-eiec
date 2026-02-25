import sys

def sort_list(words):
    print("Original list:", words)
    words.sort()
    print("Sorted list:", words)

def read_file(filename):
    try:
        with open(filename, "r") as f:
            words = [line.strip() for line in f.readlines()]
        return words
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Correct usage: python feature-translate.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    words = read_file(filename)
    sort_list(words)

if __name__ == "__main__":
    main()
