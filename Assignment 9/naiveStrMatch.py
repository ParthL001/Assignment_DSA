class Mystring:
    def __init__(self,string s):
        self.str=s
        self.l=len(s)
    def N_S_M(self,pattrn_obj):
        mainstr=self.str
        pattern=pattern_obj.str
        i=0
        while (i<=self.l-pattern_obj.l):
            j=0
            while (j<pattern_obj.l):
                if (mainstr[i+j]==pattern[j]):
                    j+=1
                else:
                    break
                if (j==pattern_obj.l):
                    print("pattern found at ",i)
                    i+=pattern_obj.l-1

            i+=1

#main
text=MyString("ABCABCDABC")
pattern=MyString("ABC")
text.N_S_M(pattern)