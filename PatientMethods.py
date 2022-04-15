from ctypes import util
from re import X
from Patient import *
import utils
import curses


stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
GREEN_ON_BLACK = curses.color_pair(1)

patient_list = []
pa = Patient("P-123", "name", "sex", "dob", "phone")
patient_list.append(pa)

def add_patient(stdscr, color, patient_list):
    stdscr.clear()
    stdscr.refresh()

    new_patients = utils.input_num_to_add(stdscr, color, "patients")

    for i in range(new_patients):
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(10, 10, f"Enter info of patient No. {i+1}", curses.A_BOLD |color)
        id = utils.input_id(stdscr, GREEN_ON_BLACK, "P-XXX", patient_list, 11, 10)
        name = utils.input_data(stdscr, GREEN_ON_BLACK, "- Name: ", 12, 10)
        sex = utils.input_sex(stdscr, GREEN_ON_BLACK, 13, 10)
        dob = utils.input_data(stdscr, GREEN_ON_BLACK, "- DoB: ", 14, 10)
        phone = utils.input_data(stdscr, GREEN_ON_BLACK, "- Phone: ", 15, 10)
        patient = Patient(id, name, sex, dob, phone)
        patient_list.append(patient)
        return patient_list

patient_list = add_patient(stdscr, GREEN_ON_BLACK, patient_list)
print(patient_list)