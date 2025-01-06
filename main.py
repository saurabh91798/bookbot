def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    character_counts = count_chars(text)
    print("\nCharacter counts:")
    for char, count in character_counts.items():
        print(f"This {char}: Appears {count} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_chars(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalnum() or char.isspace():
            char_counts[char] = char_counts.get(char, 0) + 1
    
    return char_counts
        

main()