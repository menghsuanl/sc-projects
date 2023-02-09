"""
File: largest_digit.py
Name: Meng Lee
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
# Global var. the current maximum digit
max_num = 0


def main():
	"""
	Print out the largest digit of the input number
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	Find out the largest digit in an integer
	:param n: int, the number to be found
	:return: int, the largest digit in n
	"""
	global max_num
	max_num = 0
	# Turn all digits to positive
	if n < 0:
		n = -n
	find_largest_digit_helper(n)
	return max_num


def find_largest_digit_helper(n):
	"""
	Find out the largest digit in an integer
	:param n: int, the number to be found
	"""
	global max_num
	# When n is a one digit number, reaches base case
	if n//10 == 0:
		max_num = max(n, max_num)
	else:
		current = n % 10  # Get digit by acquiring reminder after dividing 10
		n = n//10  # Reset n
		max_num = max(current, max_num)  # Update current maximum digit
		find_largest_digit_helper(n)


if __name__ == '__main__':
	main()
