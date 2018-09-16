numbers=input().split(',')
rational=[]
whole=[]
natural=[]
even=[]
odd=[]
prime=[]
a=len(numbers)

for i in range(a):
	numbers[i]=complex(numbers[i])
	x=numbers[i].real
	if numbers[i].imag==0:
		rational.append(x)
		if x-int(x)==0:
			whole.append(x)
			if x>0:
				natural.append(x)
			if x%2==0:
				even.append(x)
			else:
				odd.append(x)
			for j in range (2,int(x)+1):
				if x%j==0:
					break
				else:
					prime.append(x)

print("комплексные:  ", numbers)
print("вещественные: ", rational)
print("рациональные: ", rational)
print("целые:        ", whole)
print("натуральные:  ", natural)
print("четные:       ", even)
print("нечетные:     ", odd)
print("простые:      ", prime)