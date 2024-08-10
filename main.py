def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_characters = character_count(text)

    print_report(num_characters, num_words, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(string):
    return len(string.split())


def character_count(string):
    lowered_string = string.lower()
    counter = {}
    character_list = []

    for char in lowered_string:
        if not char in counter:
            counter[char] = 0

        counter[char] += 1

    for char in counter:
        if char.isalpha():
            dictionary = {"letter": char, "num": counter[char]}
            character_list.append(dictionary)

    character_list.sort(reverse=True, key=sort_on)

    return character_list


def sort_on(dict):
    return dict["num"]


def print_report(list, word_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for entry in list:
        print(f"The {entry["letter"]} character was found {entry["num"]} times")

    print()
    print("--- End report ---")


main()