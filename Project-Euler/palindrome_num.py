# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

list_of_nums = []
for i in range(100, 1000):
    for ii in range(100, 1000):
        num = i*ii
        if len(str(num)) % 2 == 0:
            if str(num)[:int(len(str(num))/2)] == ''.join(reversed(str(num)[int(len(str(num))/2):])):
                list_of_nums.append(num)

list_of_nums.sort()
print(list_of_nums[-1])
