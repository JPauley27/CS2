'''
name: Jack Pauley
description: This is a code that goes through Hangman, but the user plays against the computer-selected word.
log: 12/19/24, 
bugs: prints, please enter a letter, nothing else, even when it doesn't need to. 
features: None
sources:

'''
import random #command to select a random selection from a list

hangman_pics = ['''              
+---+
    |
    |
    |
    ===''', '''
+---+
O   |
    |
    |
    ===''', '''
+---+
O   |
|   |
    |
    ===''', '''
+---+
O   |
/|   |
    |
    ===''', '''
+---+
O   |
/|\  |
    |
    ===''', '''
+---+
O   |
/|\  |
/    |
    ===''', '''
+---+
O   |
/|\  |
/ \  |
    ===''']
words = ["hello","world", "python","wolf","orange","purple","yellow","red","blue","pink","green","stinky","pinky","stink","top","bottem","left","right","up","down","around","here","people","help","very","berry","apple","fruit","meat","steak","chicken","food","water","global","desktop","nothing","else","enter","leter","console","terminal","ports","problems","output","input","file","welcome","view","selection","edit","search","walk","through","source","search","explorer","test","testing","accounts","hang","man","hangman","hello","world","globe","winter","summer","fall","syrup","work","energy","formula","football","soccer","lacrosse","popper","BOP","rizz","sigma","skibidi","toilet","bridge","bus","crack","car","frat","pledge","college","donkey","unit","exam",""]
secret = random.choice(words) # sets the value "secret" to a random choice from the list of words
secret_list = list(secret)# turns 
hidden = []
guesses = 0 # sets guesses to 0

for character in secret_list: # for the number of letters in the secret list
    hidden.append("_ ") # put the underscore

print("".join(hidden))
while "_ " in hidden and guesses < len(hangman_pics)-1:
    guess = str.lower(input("enter a letter: "))
    if guesses not in list("abcdefghijklmnopqrstuvwxyz"):
        print("please enter A letter, nothing else:")
    else:
        break

    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))
    else:
        print("not here.")
        guesses += 1
        print(hangman_pics[guesses])

if "_ " in hidden:
    print("You lost,the word was", secret)
else:
    print("you won!!")
