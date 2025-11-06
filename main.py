import sys
from stats import get_word_count, get_character_count, get_data_report

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  num_char = get_character_count(text)
  sorted_list = get_data_report(num_char)
  
  # PRINT AREA
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for char in sorted_list:
    if char["char"].isalpha():
      print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
main()
  