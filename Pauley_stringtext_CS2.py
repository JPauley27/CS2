'''
name: Jack Pauley
description: I have created a code that offers the user to input a list of numbers and each number is tied to a function that is prompted when the user inputs said number. the different functions do plethorea of different things from printing the users name back randomized or printing just the first name
log: 2/26/25
bugs: consonants list doesnt work
features: None
sources: none used

'''
from collections import Counter
import random
def main():
    print ("1. Reverse and display")
    print ("2. Determine the number of vowels. You can prompt user for a particular vowel or create subtotals of each.")
    print ("3. Consonant frequency. Bonus: Subtotals of each consonant")
    print ("4. Return first name.")
    print ("5. Return last name.")
    print ("6. Return middle name(s)")
    print("7. Return boolean if last name contains a hyphen")
    print("8. Function to convert to lowercase")
    print("9. Function to convert to uppercase")
    print("10. Modify array to create a random name (mix up letters)")
    print("11. Return boolean if first name is a palindrome")
    print("12. Make initials from name")
    print("13. COME UP WITH YOUR OWN! (Bonus)")
    choice = input("choose a function numbered through 1- 18")
    if choice == "1":
        print(reverse(name))
    elif choice == "2":
        print(find_vowels(name))
    elif choice == "3":
        print(consonants(name))
    elif choice == "4":
        print(get_first_name(name))
    elif choice == "5":
        print(get_last_name(name))
    elif choice == "7":
        print(get_middle_name(name))
    elif choice == "7":
        print(hyphen(name))
    elif choice == "8":
        print(lower(name))
    elif choice == "9":
        print(upper(name))
    elif choice == "10":
        print(rand(name))
    elif choice == "11":
        print(palindrome(name))
    elif choice == "12":
        print(initials(name))


    name =input("hello what is your first and last name?")
    number_vowels = find_vowels(name)
    print (f" hello, the number of vowels in {name} is {number_vowels}")
    print ("hello,", name [::-1]+"!!")
    data = name
    reoccuring = Counter(data).most_common(1)[0][0]
    print(reoccuring)


def find_vowels(name):
    name.lower(input)
    vowel_count = (0)
    vowels = ("o","e","u","i","a",)
    if "o" in name:
        vowel_count [+1]
    elif "e" in name:
        vowel_count [+1]
    elif "u" in name:
        vowel_count [+1]
    elif "i" in name:
        vowel_count [+1]
    elif "a" in name:
        vowel_count [+1]

    '''
    for i in range(len(name)):
        if name[i] in vowels:
            count = 0
    vowels = ("o","e","u","i","a")
    for charicters in name:
        if charicters in vowels:
            count = +1
            return count
            
name =input("hello what is your first and last name?")
number_vowels = find_vowels(name)
print (f" hello, the number of vowels in {name} is {number_vowels}")
print ("hello,", name [::-1]+"!!")
data = name
reoccuring = Counter(data).most_common(1)[0][0]
print(reoccuring)
        '''

def get_firstlast_name(name):
    full_name = name("Enter your full name?")
    name_list = full_name.split
    print("first name:", name_list [0])
    print ("middle name:", name_list[1])
    print ("last name:", name_list[2])

def get_first_name(name):
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names == 0:
        first_name = FMLnames 
        return first_name
def get_last_name(name):
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names >= 2:
        last_name = FMLnames[1::-1]
        return last_name

def get_middle_name(name):
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names >= 3:
        middle_name = FMLnames [1::-1]
        return middle_name

        
def hyphen(name):
    if '-'  in name:
        return False
    
def upper(name):
    num = ord(name)
    if num > 65 and num <96:
        letter= chr(num)
        output = output+letter

def lower(name):
    num = ord(name)
    if num > 97 and num <122:
        letter= chr(num)
        output = output+letter

def consonants(name):
    consonant_count = (0)
    consonant_list = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y","z")
    if consonant_list in name:
        consonant_count =+ 1
    print [consonant_count]

def rand(name):
    randinput =(name)
    random.shuffle(randinput)
    print (randinput)

def reverse(name):
    return name [::-1]

def palindrome(name):
    name = "".join(name.split()).lower()
    if (len(name)<= 1): return True
    if name[0] != [-1]: return False
    return palindrome[1::-1]
def initials(name):

    split_name = name.split()
    split_initials= "".join([part[0]+ "." for part in split_name[:-1]]) +""+ split_name[-1]
    print(split_initials)

find_vowels()
get_firstlast_name()
get_first_name()
get_last_name()
get_middle_name()
hyphen()
upper()
lower()
consonants()
rand()
reverse()
palindrome()
initials()
main()
