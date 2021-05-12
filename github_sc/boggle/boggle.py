"""
File: boggle.py
Name: Meng Lee
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global vars.
dict_lst =[]
letter_lst = []


def main():
	"""
	This program mocking the boggle game, searching all words according to user's input matrix
	"""
	read_dictionary(FILE)
	for i in range(1, 5):
		user_input = input(str(i)+' Row of letter: ')

		# To check if user's input is valid
		chk = check_input(user_input)
		if chk:
			user_input = user_input.lower()  # Turn all letters into lowercase
			user_input = user_input.split(' ')
			letter_lst.append(user_input)
		else:
			print('Illegal Input')
			break

	# When user inputted a 4X4 matrix, start the game
	if len(letter_lst) == 4:
		# Recursion function
		find_word(letter_lst)


def find_word(letter_lst):
	"""
	Find out valid words in matrix
	:param letter_lst: lst, the letter list contains 16 letters
	"""
	passed_index = []
	ans_lst = []
	# For every first letter
	for i in range(4):  # Row index
		for j in range(4):  # Column index
			find_word_helper(letter_lst, i, j, '', passed_index, ans_lst)
	print('There are '+str(len(ans_lst))+' words in total.')


def find_word_helper(letter_lst, i, j, current, passed_index, ans_lst):
	"""
	The recursion function to search all valid word in the matrix by matching with dictionary
	:param letter_lst: lst, the letter list contains 16 letters
	:param i: int, the current row index of the letter
	:param j: int, the current column index of the letter
	:param current: str, the current string
	:param passed_index: lst, containing the index that already tried
	:param ans_lst: lst, containing the words found
	"""
	# List of all possible position index to check for (i,j)
	neighbor_index = [[i, j], [i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1],
					[i + 1, j], [i + 1, j + 1]]
	for neighbor in neighbor_index:
		# Check if the index exists, valid range is in 0-3
		if neighbor[0] < 0 or neighbor[0] > 3 or neighbor[1] < 0 or neighbor[1] > 3:
			pass
		# Check if the index has used
		elif neighbor in passed_index:
			pass
		else:
			# Append letter
			ch = letter_lst[neighbor[0]][neighbor[1]]
			current += ch
			passed_index.append(neighbor)

			# Update current index
			now_i = neighbor[0]
			now_j = neighbor[1]

			# Check whether 'current' meets answer requirement, if yes, append to ans_lst
			if len(current) >= 4:
				if current in dict_lst:
					if current not in ans_lst:
						print('Found: '+current)
						ans_lst.append(current)
					# Word may contain with more than 4 letters, go into recursion and keep on searching
					find_word_helper(letter_lst, now_i, now_j, current, passed_index, ans_lst)
				# Un-choose
				passed_index.pop()
				current = current[:-1]

			# If 'current' does not meet requirement, check prefix and keep on searching
			else:
				check = has_prefix(dict_lst, current)
				if check:
					find_word_helper(letter_lst, now_i, now_j, current, passed_index, ans_lst)
				else:
					pass
				passed_index.pop()
				current = current[:-1]


def check_input(user_input):
	"""
	Check if input is meet the input requirements: 4 alphabet spacing with blank
	:param user_input: str, can be anything
	:return: bool, whether input passed the check
	"""
	if len(user_input) != 7:
		return False
	for i in (0, 2, 4, 6):
		if not user_input[i].isalpha():
			return False
	for i in (1, 3, 5):
		if user_input[i] != ' ':
			return False
	else:
		return True


def read_dictionary(filename):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(filename, 'r') as f:
		for word in f:
			word = word[:-1]
			dict_lst.append(word)


def has_prefix(dict_lst, sub_s):
	"""
	Check if dictionary contains at least one word whose prefix equal to sub_s
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	cnt = 0
	for i in range(len(dict_lst)):
		s = dict_lst[i]
		is_exist = s.startswith(sub_s)
		if is_exist:
			cnt += 1
	if cnt > 0:
		return True


if __name__ == '__main__':
	main()
