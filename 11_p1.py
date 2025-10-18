class aa:
	a = 1
    
class bb(aa):
    b = 2
    a = 10
    
class cc(bb):
	c = 3
    
anshu = cc()
print(anshu.a,anshu.b,anshu.c)
    

str2 = ""
str1 = input("enter name : ")

for i in range(len(str1)-1,-1,-1):
    str2 += str1[i]

print(str2)