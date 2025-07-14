from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
  for index, element in enumerate(numbers_list):
    if element == number_to_find:
      return index
  return -1
    

@time_it
def binary_search(numbers_list, number_to_find):
  left_index = 0
  right_index = len(numbers_list) - 1
  mid_index = 0

  while left_index <= right_index:
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
      return mid_index
    
    if mid_number < number_to_find:
      left_index = mid_index + 1
    else:
      right_index = mid_index - 1

  return -1

def find_all_occurances(numbers_list, number_to_find):
  index = binary_search(numbers_list, number_to_find)
  indices = [index]

  i = index - 1
  while i >= 0:
    if numbers_list[i] == number_to_find:
      indices.append(i)
    else:
      break
    i = i - 1

  i = index + 1
  while i < len(numbers_list):
    if numbers_list[i] == number_to_find:
      indices.append(i)
    else:
      break
    i = i + 1
  
  return sorted(indices)


def binary_recursive_search(numbers_list, number_to_find, left_index, right_index):
  if right_index < left_index:
    return -1
  
  mid_index = (left_index + right_index) // 2
  if mid_index >= len(numbers_list) or mid_index < 0:
    return -1
  
  mid_number = numbers_list[mid_index]
  if mid_number == number_to_find:
    return mid_index
  
  if mid_number < number_to_find:
    left_index = mid_index + 1
  else:
    right_index = mid_index - 1
  
  return binary_recursive_search(numbers_list, number_to_find, left_index, right_index)


if __name__ == "__main__":
  numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
  number_to_find = 34

  index = find_all_occurances(numbers_list, number_to_find)
  print(f'Number found at {index} in the binary search') 



# Binary search exercises starts from here...
# Exercise 1
# Because binary search only works on sorted list and the list you provided here is not sorted therefore it is returning -1 because in the logic if the mid number is greater than the target we will reduce the right index beside to the mid index.

# Exercise 2



