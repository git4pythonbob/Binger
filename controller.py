inp = []

choice = None
first_var = None
first_var_comp = False

def reset():
    global choice, first_var, first_var_comp
    choice = None
    first_var = None
    first_var_comp = False

def toggle_sign():
    global inp

    if inp and inp[0] != '-':
        inp.insert(0, '-')
    elif inp and inp[0] == '-':
        inp.pop(0)


def set_choice(new_choice):
    global choice
    global first_var
    global first_var_comp

    choice = new_choice
    first_var = float(''.join(map(str, inp)))
    first_var_comp = True
    inp.clear()

def calculate_result(entry_widget):
    global inp, choice, first_var, first_var_comp

    if first_var_comp and inp:
        second_var = float(''.join(map(str, inp)))
        if choice == '+':
            result = first_var + second_var
        elif choice == '-':
            result = first_var - second_var
        elif choice == '*':
            result = first_var * second_var
        elif choice == '/':
            if second_var != 0:
                result = first_var / second_var
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operator"
        
        inp.clear()
        choice = None
        first_var = result
        first_var_comp = True
        entry_widget.delete(0, "end")
        entry_widget.insert(0, result)
    else:
        result = None

    return result