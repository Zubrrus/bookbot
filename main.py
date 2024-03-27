def main():
    book_path = "books/frankenstein.txt"
    report = create_report(book_path)
    print(report)


def count_words(string):
    return len(string.split())


def count_chars(string):
    dict = {}
    for char in string.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict.update({char: 1})
    return dict


def dict2list(dict):
    list = []
    for item in dict:
        list.append({"name": item, "num": dict[item]})
    return list


def sort_on(dict):
    return dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def create_report(book_path):
    string = get_book_text(book_path)
    num_words = count_words(string)
    num_chars_dict = count_chars(string)
    num_char_list = dict2list(num_chars_dict)
    num_char_list.sort(reverse=True, key=sort_on)
    
    text = f"--- Begin report of {book_path} ---"
    text += f"\n{num_words} words found in the document"
    text += "\n"
    for item in num_char_list:
        if item["name"].isalpha():
            text += f"\nThe '{item["name"]}' " \
                    f"character was found {item["num"]} times"
    text += "\n--- End report ---"
    return text


main()
