k = 4
l = [ 2,3,4,5,6,8]
b=0
n = len(l)
for i in n:
	if l[i]==k:
		print("it's index is "+i)
		b=1
		break
if b==0:
	print("Not found")

