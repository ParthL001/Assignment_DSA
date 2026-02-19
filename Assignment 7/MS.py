class MergeSort:
    def __init__(self):
        self.arr = []
        self.n = 0

    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])   # ✅ add element to result
                j += 1

        # ✅ Correct extend syntax
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def accept(self):
        self.n = int(input("Enter number of elements: "))
        for i in range(self.n):
            val = int(input(f"Enter delivery time for element {i+1}: "))
            self.arr.append(val)

    def disp(self, arr):
        print("Array:", arr)


# main
m = MergeSort()
m.accept()
print("Original array:")
m.disp(m.arr)

print("Sorted array:")
print(m.mergesort(m.arr))
