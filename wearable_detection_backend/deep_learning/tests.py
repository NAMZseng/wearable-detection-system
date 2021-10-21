from django.test import TestCase

# Create your tests here.


arr = [None] * 2
arr[0] = [1, 2, 3, 4]
arr[1] = [4, 3, 2, 1]

arr[0].extend(arr[1])

print(arr[0])
