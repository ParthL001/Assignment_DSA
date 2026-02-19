class MergeSort:
    def __init__(self):
        self.arr=[]
        self.n=0
        
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        
        mid=(len(arr))//2
        left=self.mergesort(arr[:mid])
        right=self.mergesort(arr[mid:])

        return self.merge(left,right)
    
    def merge(self,left,right):
        result=[]
        i=j=0

        while (i<len(left) and j<len(right)):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    def accept(self):
        self.n=int(input("enter no. of elements"))
        for i in range(0,self.n):
            val=int(input(f"enter dilevery time for {i+1} minutes"))
            self.arr.append(val)

    def disp(self,arr):
        for i in range (0,len(arr)):
            print(self.arr[i])

#main

m=MergeSort()
m.accept()
m.disp(m.arr)
print("sorted array : ")
print(m.mergesort(m.arr))







    
