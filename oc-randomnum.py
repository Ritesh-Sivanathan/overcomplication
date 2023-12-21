import string
import sys

l_ower_c_ase_l_etters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
u_pper_c_ase_l_etters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = 0
transfer_number = 0
correct = False

for _ in range(1):
    for i in range(1, 5):
        if i not in l_ower_c_ase_l_etters:
            if i not in u_pper_c_ase_l_etters:
                transfer_number = i
                if transfer_number != number:
                    number = transfer_number

user_input = input("Guess the number: ")
print(number)
if number == int(str(user_input)) and int(str(user_input)) not in l_ower_c_ase_l_etters and int(str(user_input)) not in u_pper_c_ase_l_etters and __name__ == "__main__":
    print("Correct")
    if correct != True:
        correct = True
    else:
        correct = True
else:
    while correct is False:
        print("Incorrect")
        user_input = input("Guess the number")
        if int(user_input) == number:
            correct = True
            break

print("Game is over")
exit = input("Exit?: ")

def exit():
    sys.exit()
    

if str(exit) == "Yes" or str(exit) == "YES" or str(exit) == "yes" or str(exit) == "YeS" or str(exit) == "yEs" or str(exit) == "yES" or str(exit) == "Yes":
    print("okay")
    exit_yes_or_no_boolean_variable = True
    if exit_yes_or_no_boolean_variable is True:
        exit()
    else:
        exit_yes_or_no_boolean_variable = True
        if exit_yes_or_no_boolean_variable is True:
            for my_counter_variable_for_the_exit_loop in range(1):
                exit()