import random
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
secret = random.choice(words)
secret_list = list(secret)
hidden = []
guesses = 0

for character in secret_list:
    hidden.append("_ ")

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

def restart():
    user_input = input("Do you want to play again?")
    if user_input == "yes":
        restart()
    if user_input == "no":
        print("Goodbye, You stink at Hangman!!")
    

