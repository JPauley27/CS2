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
    """
    prompts the user to pick which function he would like to go into sorted by numbers and prompts the user for their name

    Args:
        choice (name): prompts the user to choose which function they would like to run and prompts the user for their name

    Returns:
        variable,middle_name: takes the user to the function they selected to run

    Raises:
        ValueError: If the choice of function is not in the list of functions.

    """
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
    choice = input("choose a function numbered through 1- 12")
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
    """
    Reads the inputed name and returns a count of the vowels in the name

    Args:
        name (variable):Creates a vowel_count and creates a all lowercase list of the vowels converts the user input into all lowercase(.lower). then checks if the vowels in the vowel list appear in the name inputed if so raises the vowel count +1

    Returns:
        variable,find_vowels: returns a vowel count of the amount of vowels in the inputed name.

    Raises:
        ValueError: If the inputed name is not letters or doesnt include vowels or to many vowels.

    """
    name.lower()
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
        return vowel_count

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
    """
    Reads the inputed name and prompts the user on which one he would like to print 

    Args:
        name (variable): The inputed name by the user that is being read by the code and splits it by the first middle last name and asks the user which one they want to print

    Returns:
        variable,firstlast_name: prints the name selected by the user.

    Raises:
        ValueError: If the inputed name is not letters or doesnt include a first, middle, and last name.

    """
    full_name = name("Enter your full name?")
    name_list = full_name.split
    name_choice = print("Do you want to print the first name(1), middle name(2), or last name(3)")
    if name_choice == 1:
        print("first name:", name_list [0])
    elif name_choice == 2:
        print ("middle name:", name_list[1])
    elif name_choice == 3:
        print ("last name:", name_list[2])

def get_first_name(name):
    """
    Reads the inputed name and returns only the first name

    Args:
        name (variable): The inputed name by the user that is being read by the code and splits it by the first middle last name to print one of those induvidually 

    Returns:
        variable,middle_name: returns the first name inputed by the user.

    Raises:
        ValueError: If the inputed name is not letters or doesnt include a first name.

    """
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names == 0:
        first_name = FMLnames 
        return first_name
    
def get_last_name(name):
    """
    Reads the inputed name and returns only the last name

    Args:
        name (variable): The inputed name by the user that is being read by the code and splits it by the first middle last name to print one of those induvidually 

    Returns:
        variable,middle_name: returns the last name inputed by the user.

    Raises:
        ValueError: If the inputed name is not letters or doesnt include a last name.

    """
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names >= 2:
        last_name = FMLnames[1::-1]
        return last_name

def get_middle_name(name):
    """
    Reads the inputed name and returns only the middle name

    Args:
        name (variable): The inputed name by the user that is being read by the code and splits it by the first middle last name to print one of those induvidually 

    Returns:
        variable,middle_name: returns the middle name inputed by the user.

    Raises:
        ValueError: If the inputed name is not letters or doesnt include a middle name.

    """
    FMLnames = name.split()
    num_of_names = len(FMLnames)
    if num_of_names >= 3:
        middle_name = FMLnames [1::-1]
        return middle_name
        
def hyphen(name):
    """
    Returns a boolean if a hyphen is in the inputed name 

    Args:
        name (variable): if there is a hyphen in the user name return a boolean

    Returns:
        variable,hyphen: returns false if there is a hyphen in the inputed name

    Raises:
        ValueError: If the input name is not a letter or there is no hyphen.

    """
    if '-'  in name:
        return False
    else:
        print("There is no hyphen in "(name))
    
def upper(name):
    """
    Returns the inputed name in all uppercases

    Args:
        name (variable): The inputed name by the user that is used to find those letters on ascii table to convert them to uppercase

    Returns:
        variable,lower: returns the name in all uppercase using the ascii table to find the uppercase letters by there numbered place.

    Raises:
        ValueError: If the input name is not a letter.

    """
    num = ord(name)
    if num > 65 and num <96:
        letter= chr(num)
        output = output+letter

def lower(name):
    """
    Returns the inputed name in all lowercases

    Args:
        name (variable): The inputed name by the user that is used to find those letters on ascii table to convert them to lowercase

    Returns:
        variable,lower: returns the name in all lowercase using the ascii table to find the lowercase letters by there numbered place.

    Raises:
        ValueError: If the input name is not a letter.

    """
    num = ord(name)
    if num > 97 and num <122:
        letter= chr(num)
        output = output+letter
        print (output)

def consonants(name):
    """
    Returns the inputed name with a count of the consonants 

    Args:
        name (variable): The inputed name by the user that is used to count the variables

    Returns:
        variable,consonant_count: returns the number of consonants in the inputed name .

    Raises:
        ValueError: If the input name is a number or does not include any consonants.

    """
    consonant_count = (0)
    consonant_list = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y","z")
    if consonant_list in name:
        consonant_count =+ 1
    print [consonant_count]

def rand(name):
    """
    Returns the inputed name in a random order

    Args:
        name (variable): The inputed name by the user that is randomly shuffled

    Returns:
        variable,shuffle: returns the inputed name in a random order.

    Raises:
        ValueError: If the input name is a number or is not longer than one letter.

    """
    randinput =(name)
    random.shuffle(randinput)
    print (randinput)

def reverse(name):
    """
    Returns the inputed name backwards

    Args:
        name (variable): The inputed name by the user that is reversed

    Returns:
        variable,reverse: returns the name in reversed order.

    Raises:
        ValueError: If the input name is a number.

    """
    return name [::-1]
    

def palindrome(name):
    """
    if there is a palidrome returns a boolean, if the palidrome works returns true if not false

    Args:
        name (variable): The inputed name used in the function to check if its a palidrome

    Returns:
        palidrome: returns true and the flipped palidrome

    Raises:
        ValueError: If the input is a number or not a palidrome.

    """
    
    name = "".join(name.split()).lower()
    if (len(name)<= 1): return True
    if name[0] != [-1]: return False
    return palindrome[1::-1]

def initials(name):
    """
    Finds the intials of the inputed name

    Args:
        name (join): splits the name then joins the intials with a comma

    Returns:
        split initials: returns the intials of the inputed name with commas spacing them

    Raises:
        ValueError: If the input is a number or does not include spaces

    """

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
