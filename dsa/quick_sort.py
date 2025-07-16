# def swap(start, end, elements):
#   if start != end:
#     tmp = elements[start]
#     elements[start] = elements[end]
#     elements[end] = tmp

# def partition(start, end, elements):
#   pivot_index = start
#   pivot = elements[pivot_index]

#   while start < end:
#     while start < len(elements) and elements[start] <= pivot:
#       start += 1
    
#     while elements[end] > pivot:
#       end -= 1
    
#     if start < end:
#       swap(start, end, elements)
    
#   swap(pivot_index, end, elements)

#   return end

# def quick_sort(elements, start, end):
#   if start < end:
#     pi = partition(start, end, elements)
#     quick_sort(elements, start, pi - 1)
#     quick_sort(elements, pi + 1, end)

# if __name__ == '__main__':
#   elements = [11, 2, 9, 7, 29, 28, 15]
#   quick_sort(elements, 0, len(elements) - 1)
#   print(elements)

# Quick sort exercises starts from here.
# Exercise 1
# Implement quick sort using lumoto partition scheme. This partition scheme is explained in the video tutorial, you need to write python code to implement it.

def swap(start, end, elements):
  if start != end:
    tmp = elements[start]
    elements[start] = elements[end]
    elements[end] = tmp

def partition(p_index, end, elements):
  pivot = elements[end]
  i = p_index - 1

  for j in range(p_index, end):
    if elements[j] <= pivot:
      i += 1
      swap(i, j, elements) 
  
  swap(i + 1, end, elements)

  return i + 1

def quick_sort(elements, start, end):
  if start < end:
    pi = partition(start, end, elements)
    quick_sort(elements, start, pi - 1)
    quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
  elements = [11, 2, 9, 7, 29, 28, 15]
  quick_sort(elements, 0, len(elements) - 1)
  print(elements)