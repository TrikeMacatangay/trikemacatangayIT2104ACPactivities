size = int(input("Enter the size of the array: "))

arr = [0.0] * size

print("Enter the elements of the array:")
for i in range(size):
  arr[i] = float(input())
x = int(input("Enter the index of the element to print: "))

try:
  print("Element at index", x, ":", "%.2f" % arr[x])
except IndexError:
  print("Index", x, "is invalid.")