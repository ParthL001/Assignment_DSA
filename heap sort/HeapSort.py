#heap Sort

class List:
    def __init__(self):
        self.lst=[0]
        self.n=0

    def accept(self):
        self.n=int(input("enter no of nodes"))
        for i in range(1,self.n+1):
            val=int(input(f"Enter {i} element"))
            self.lst.append(val)

    def disp(self):
        print(self.lst)

    def hsort(self):
        for i in range(self.n//2,0,-1):
            self.adjust(i,self.n)

        for i in range (self.n-1,0,-1):
            self.lst[1],self.lst[i+1]=self.lst[i+1],self.lst[1]

            self.adjust(1,i)

    def adjust(self,i,n):
        no=self.lst[i]
        j=2*i

        while  j<=n:
            if j<n and self.lst[j]<self.lst[j+1]:
                j+=1
            if no<self.lst[j]:
                self.lst[j//2]=self.lst[j]
                j=j*2
            else:
                break
        self.lst[j//2]=no



#main
l=List()
l.accept()
l.disp()
l.hsort()
l.disp()
        
