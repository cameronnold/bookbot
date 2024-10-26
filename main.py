
def main():
  path_to_file = "books/frankenstein.txt"
  with open(path_to_file) as f:
    file_contents = f.read()
    print(file_contents)



if __name__ == "__main__":
  main()