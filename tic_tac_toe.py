table=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def print_table(table):
    for i in range(3):
        print(" | ".join(table[i]))
        if i<2:
            print("----------")

def checking_winner(table):
    for i in range(3):
        if (table[i][0]==table[i][1]==table[i][2] !=" "):
            return table[i][0]

    for j in range(3):
        if (table[0][j]==table[1][j]==table[2][j] != " "):
            return table[0][j]

    if (table[1][1]==table[2][2]==table[0][0] !=" "):
        return table[1][1]

    if (table[0][2]==table[1][1]==table[2][0]!=" "):
        return table[1][3]

    return None

def checking_draw(table):
    for row in table:
        for cell in row:
            if cell == " ":
                return False
    return True


import random
def c_random_selection(table):
    while True:
        row=random.randint(0,2)
        column=random.randint(0,2)

        if table[row][column]==" ":
            table[row][column]="O"
            break


while True:
    
    print_table(table)

    row=int(input("Enter row number:"))
    column=int(input("Enter column number:"))

    if (row<=2) and (column<=2):
        if table[row][column]==" ":
            table[row][column]="X"
            
        else:
            print("Invalid Input")
            continue
        
    else:
        print("Invalid Input")
        continue
    
    c_random_selection(table)

    if (checking_winner(table)=="X"):
        print("'X' wins")
        print_table(table)
        break
    elif(checking_winner(table)=="O"):
        print("'O' wins" )
        print_table(table)
        break
    else:
        if checking_draw(table):
            print("Match Draw")
            print_table(table)
            break
    


    



