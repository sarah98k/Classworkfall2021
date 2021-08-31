#LDL_analysis.py

def LDL_analysis():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("2 - LDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 2:
            LDL_Driver()
            
    print(choice)
    return choice

def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analyze(LDL_value)
    ldl_output(LDL_value, LDL_character)

def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value
    
def ldl_analyze(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very High"

def ldl_output(LDL_value, LDL_answer) :
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))





LDL_analysis()






