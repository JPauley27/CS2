import random

col1_row1=" "
col1_row2=" "
col1_row3=" "
col2_row1=" "
col2_row2=" "
col2_row3=" "
col3_row1=" "
col3_row2=" "
col3_row3=" "
user = 1
print ("Welcome to Tic-Tac-Toe!!!")
start = input(str.lower("You will start as X. Type 'go' if you want to start:"))
if start == 'go':

    while True:
        print(col1_row1,"|", col2_row1, "|", col3_row1)
        print("------------")
        print(col1_row2,"|", col2_row2,"|", col3_row2)
        print("------------")
        print(col1_row3,"|", col2_row3,"|", col3_row3)
        if user == 1:
            try:
                ycolumn = int(input("which column would you like to place your X?"))
                xrow = int(input("which row would you like to place your X?"))
                if ycolumn > 0 and ycolumn < 4 and xrow > 0 and xrow < 4:
                    if ycolumn == 1:
                        if xrow == 1:
                            if col1_row1 == " ":
                                col1_row1 = "X"
                                user = 2
                    else:
                        print ("This spot is already taken")   
                if xrow == 3:
                    if col1_row3 == "":
                        col1_row3 == "X"
                        user = 2
                    else:
                        print("This spot is already taken")
                if xrow == 2:
                    if col1_row2 == "":
                        col1_row2 == "X"
                        user = 2
                    else: 
                        print("This spot is already taken.")
                if ycolumn == 2:
                    if xrow == 1:
                        if col2_row1 == "":
                            col2_row1 == "X"
                            user = 2
                    else:
                        print ("That spot is already taken.")
                if xrow == 2:
                    if col2_row2 == "":
                        col2_row2 == "X"
                        user = 2
                    else:
                        print ("That spot is already taken.")
                if ycolumn == 2:
                    if xrow == 3:
                        if col2_row3 == "":
                            col2_row3 == "x"
                            user =2 
                    else:
                        print("That spot is already taken.")
                if ycolumn == 3:
                    if xrow == 1:
                        if col3_row1 == "":
                            col3_row1 == "X"
                            user = 2
                    else:
                        print("That spot is already taken.")
                if ycolumn == 3:
                    if xrow == 2:
                        if col3_row2 == "":
                            col3_row2 == "X"
                            user = 2
                    else:
                        print ("That spot is already taken.")
                if ycolumn == 3:
                    if xrow == 3:
                        if col3_row3 =="":
                            col3_row3 =="X"
                    else:
                        print ("That spot is already taken.")
                else:
                 print("Incorrect input.")
            except:
                print("You didnt enter the correct value.")