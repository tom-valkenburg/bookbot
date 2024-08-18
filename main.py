def main():
    file_path = "books/frankenstein.txt"
    text = read_text_from_file(file_path)
    word_count = count_words_in_text(text)
    chars = count_characters_in_text(text)
    sorted_chars = convert_dict_to_sorted_list(chars)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")

    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def read_text_from_file(file_path):
    with open(file_path) as file:
        return file.read()
    
def count_words_in_text(text):
    words = text.split()
    count = len(words)
    return count
    
def count_characters_in_text(text):
    character_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def convert_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True,key = sort_on)
    return sorted_list

main()