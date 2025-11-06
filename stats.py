def get_word_count(text):
  return len(text.split())

def get_character_count(text):
  char = {}
  for i in text.lower():
    if i not in char:
      char[i] = 1
    else:
      char[i] += 1
  return char

def get_data_report(dict):
  sorted_list = []
  def sort_on(items):
    return items["num"]

  for word in dict:
    count = dict[word]
    new_dict = {"char": word, "num": count}
    sorted_list.append(new_dict)

  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list