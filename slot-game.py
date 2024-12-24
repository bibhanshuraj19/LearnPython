import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = { 
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
def get_slot_machine_spin(rows,cols,symbols) :
    all_symbols = []
    for symbol , symbol_count in symbols.items() : 
        for  i in range (symbol_count) : 
            all_symbols.append(symbol)
    columms = [[],[],[]]

    for col in range(cols) :
        columm = []
        current_symbols = all_symbols[:]
        for row in range(rows) :
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columm.append(value)
        columms.append(columm)
    return columms

def print_slot_machine (columns) :
    for row in range (len(columns[0])) : 
        for i , column in columns :
            if i != len(columns) - 1 :
                print(column[row], "   ", "|")
            else : 
                print(column[row])
def deposit() :
    while True :
        amount = input("What ammount would you like to deposit in $ : ")
        if amount.isdigit() :
            amount = int(amount)
            if amount > 0 : 
                break
            else : 
                print("amount must be greater than 0 $")
        else :
            print("Enter a number")
    return amount 
def bet_lines () : 
    while True :
        lines = input("How many lines do you want to bet on (1 - " + str(MAX_LINES) + ") ? ")
        if lines.isdigit() :
            lines = int(lines)
            if  1 <= lines <= MAX_LINES : 
                break
            else : 
                print(" Lines out of range Enter valid lines ")
    return lines
def bet_per_lines () :
    while True :
        amount = input("How many money do you want to bet : ")
        if amount.isdigit() :
            amount = int(amount)
            if  MIN_BET <=amount <= MAX_BET :
                break
            else :
                print(f"amount must be {MIN_BET}$ - {MAX_BET}$ ")
        else : 
            print("enter a number ")
    return amount
def main() :
    balance = deposit()
    lines = bet_lines()
    while True : 
        bet = bet_per_lines()
        total_bet = lines * bet

        if total_bet > balance :
            print("Your bet amount is more than your deposit ")
        else :
            break

    print(f"You are betting {bet}$ on {lines} lines and the total bet is : {total_bet}")    
main()
