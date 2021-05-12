"""
File: anagram.py
Name: Meng Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global vars.
dict_lst = []


def main():
    """
    Find out anagrams based on user's input
    """
    print('Welcome to StanCode "Anagram Generator" (or -1 to quit)')
    s = input('Find Anagrams for: ')
    while s != EXIT:
        find_anagrams(s)
        s = input('Find Anagrams for: ')


def read_dictionary(filename):
    """
    Read a dictionary file and put words in a dict_lst
    :param filename: txt, the file to be read
    """
    with open(filename, 'r') as f:
        for word in f:
            word = word[:-1]
            dict_lst.append(word)


def find_anagrams(s):
    """
    To find anagrams of s and print them out
    :param s: str, the user's input
    """
    used_index = []
    ans_lst = []
    read_dictionary(FILE)
    find_anagrams_helper(s, '', used_index, ans_lst)
    num_found = len(ans_lst)
    print(str(num_found)+' anagrams: '+str(ans_lst))


def find_anagrams_helper(s, current, used_index, ans_lst):
    """
    To find the anagrams of s
    :param s: str, the word to be reorder
    :param current: str, the word to be searched in dict_lst
    :param used_index: list, a list contains character's index that is in 'current'
    :param ans_lst: list, a list contains anagrams found
    """
    if len(s) == len(current):
        if current in ans_lst:  # To prevent from printing same anagrams more than once
            pass
        else:
            ans_lst.append(current)
            print('Searching...')
            print('Found: '+current)
    else:
        for i in range(len(s)):
            if i in used_index:  # If the character already used in current, pass
                pass
            else:
                # Choose
                ch = s[i]
                current += ch
                used_index.append(i)
                # Check prefix for current, if yes, go on appending character; else, quit search and pop last character
                check = has_prefix(dict_lst, current)
                if check:
                    # Explore
                    find_anagrams_helper(s, current, used_index, ans_lst)
                else:
                    pass
                # Un-choose: back to last pick point
                used_index.pop()
                current = current[0:-1]


def has_prefix(dict_lst, sub_s):
    """
    Check if dictionary contains at least one word whose prefix equal to sub_s
    :param dict_lst: list, a list contains all word from dictionary
    :param sub_s: str, the word to be checked
    :return: bool, if there are any word whose prefix equal to sub_s
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
