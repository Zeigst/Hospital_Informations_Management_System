import curses

def input_num_to_add(stdscr, color, obj_type):
    """
    Get a number n to input n object into a list
    """
    while True:
        try:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10, 10, f"Enter number of {obj_type} to add: ", curses.A_BOLD |color)
            x = int(stdscr.getstr(10, 45, 10))
            if x <= 0:
                stdscr.addstr(11, 10, "Invalid Input: Input must be greater than 0!", curses.A_BOLD |color)
                stdscr.refresh()
                stdscr.getch()
            else:
                break
        except ValueError:
            stdscr.addstr(11, 10, "Invalid Input: Input must be an integer!", curses.A_BOLD |color)
            stdscr.refresh()
            stdscr.getch()
    return x
    
def input_data(stdscr, color, prompt, y_axis, x_axis):
    """
    Get Input from user
    """
    while True:
        try:    
            stdscr.addstr(y_axis + 1, x_axis, f"                    ", curses.A_BOLD | color)
            stdscr.addstr(y_axis, x_axis, f"{prompt}", curses.A_BOLD | color)
            x = str(stdscr.getstr(y_axis, x_axis + len(prompt), 20), "utf-8", errors = "ignore")
            if len(x) == 0:
                stdscr.addstr(y_axis + 1, x_axis, f"Invalid Input", curses.A_BOLD | color)
            else: break
        except False:
            pass
    return x

def dup_check(list, id):
    """
    Check if an ID already exist in a list
    """
    flag = 0
    for item in list:
        if item.get_id() == id:
            flag += 1
            break
    if flag == 1: return True
    else: return False

def input_id(stdscr, color, id_format, list, y_axis, x_axis):
    """
    Input ID methods with validation check & dup check
    """
    while True:
        try:
            stdscr.addstr(y_axis+1, x_axis, f"                              ", curses.A_BOLD | color)
            stdscr.addstr(y_axis, x_axis + len(id_format) + 11, f"                                              ", curses.A_BOLD | color)
            id = input_data(stdscr, color, f"- ID ( {id_format} ): ", y_axis, x_axis)
            id_num = int(id[-3:])
            if id[:2] != id_format[:2] or len(id) != len(id_format):
                stdscr.addstr(y_axis+1, x_axis, f"Invalid ID !", curses.A_BOLD | color)
                stdscr.refresh()
                stdscr.getch()           
            else:
                if dup_check(list, id):
                    stdscr.addstr(y_axis+1, x_axis, f"This ID already exist!", curses.A_BOLD | color)
                    stdscr.refresh()
                    stdscr.getch()
                else: break
        except ValueError:
            stdscr.addstr(y_axis+1, x_axis, f"Invalid ID!", curses.A_BOLD | color)
            stdscr.refresh()
            stdscr.getch()
    return id
            
def input_sex(stdscr, color, y_axis, x_axis):
    """
    Input sex methods with validation check (F/M)
    """
    while True:
        try:
            stdscr.addstr(y_axis+1, x_axis, f"                ", curses.A_BOLD | color)
            stdscr.addstr(y_axis, x_axis + 13, f"                    ", curses.A_BOLD | color)
            sex = input_data(stdscr, color, "- Sex (F/M): ", y_axis, x_axis)
            if sex != "F" and sex != "M":
                stdscr.addstr(y_axis+1, x_axis, f"Invalid Input!", curses.A_BOLD | color)
                stdscr.refresh()
                stdscr.getch()
            else: break
        except False:
            pass
    return sex


