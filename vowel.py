a=raw_input()
n=len(a)
c=0
for i in range(0,n):
  if(a[i]=='a' or 'e' or 'i' or 'o' or 'u'):
    c+=1
if(c>=1):  
    print("yes")
else:
   print("no")
