# Hackerrank Python>Collections>DefaultDict Tutorail Challange Soulution by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
size=input()
size=size.split(" ")

A=[0]*int(size[0])
B=[0]*int(size[1])

for c in range(0,len(A)):
    char=input()
    A[c]=char
for c in range(0,len(B)):
    char=input()
    B[c]=char

result=""
 
for char in B:   
    if(char in A):
        for c in range(0,len(A)):
            if(A[c]==char):
              result+=str(c+1)+" "
    else:
        result+="-1"
    result+="\n"
    
print(result)
   
