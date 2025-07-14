for index, element in enumerate(numbers_list):
    if element == number_to_find:
      duplicate_arr.append(index)
    else:
      duplicate_arr = []
      break