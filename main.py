def main():
    with open('books/frankenstein.txt') as f:
        file_content = f.read()
        word_count = count_words(file_content)
        char_dict = character_count_dict(file_content)
        print(f"{word_count} words found in the document\n")
        character_count_report(char_dict)

def count_words(file_content):
    words = file_content.split()
    return len(words)

def character_count_dict(file_content):
    file_content_lowered = file_content.lower()
    count_dict = {}
    for char in file_content_lowered:
        if char.isspace():
            continue

        if (not char.isalpha()):
            continue

        if (char not in count_dict):
            count_dict[char] = 1
            continue

        if (char in count_dict):
            count_dict[char] += 1

    return count_dict

def character_count_report(character_count_dict):
    for w in sorted(character_count_dict, key=character_count_dict.get, reverse=True):
        print(f"The '{w}' character was found {character_count_dict[w]}")


main()
