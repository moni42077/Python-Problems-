sum = 0
square_start = 0
for i in range(101):
	sum+= i**2
	square_start+=i
square_final = square_start**2
difference = square_final - sum
print(difference)