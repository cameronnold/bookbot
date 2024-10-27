def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    chars_count = char_count(text)
    new_list = chars_dict_to_sorted_list(chars_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document.\n")
    
    for item in new_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
   
def char_count(text):
    chars = {}
    lower_text = text.lower()
    for i in lower_text:
        if i.isalpha():
          if i in chars:
              chars[i] += 1
          else:
              chars[i] = 1
    return chars



def sort_on(dict):
    return dict["num"]

# my original function
def create_list_of_dicts(dict):
   new_list = zip(dict.keys(), dict.values())
   new_list = list(new_list)
   return new_list

# solution function - note I tried doing something like this at first but couldn't figure out line "sorted_list.append({"char": key, "num": dict[key]})"
# this line is going to each key and for each key a new dict is created with the key set as "char" and the value set as "num"
# for example if the dict is {"a: 5, b: 2, c:8"} and we loop through the dict we start with for key in dict at a
# we then create a dict at a and set its key which we called char "char" to a because we do "char" : key making the key we are at 'a' and we then make the "num" the value of the key we are at
def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()