fibonachi= [1,2]
while fibonachi[-1] <= 4000000:
	new_num = fibonachi[-1] + fibonachi[-2]
	fibonachi.append((new_num))
sum = 0 
for i in fibonachi:
	if i % 2 == 0:
		sum+=i
print(sum)
