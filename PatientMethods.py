from Patient import *
import utils
import curses

def add_patient(stdscr, color, patient_list):
    stdscr.clear()
    stdscr.refresh()

    new_patients = utils.input_num_to_add(stdscr, color, "patients")

    for i in range(new_patients):
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(10, 10, f"Enter info of patient No. {i+1}", curses.A_BOLD |color)
        id = utils.input_id(stdscr, color, "P-XXX", patient_list, 11, 10)
        name = utils.input_data(stdscr, color, "- Name: ", 12, 10)
        sex = utils.input_sex(stdscr, color, 13, 10)
        dob = utils.input_data(stdscr, color, "- DoB: ", 14, 10)
        phone = utils.input_data(stdscr, color, "- Phone: ", 15, 10)
        patient = Patient(id, name, sex, dob, phone)
        patient_list.append(patient)
    return patient_list
