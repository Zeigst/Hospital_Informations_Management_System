import pickle 
import os

def save_doctor(doctors):
    with open("doctors.pkl", "wb") as f:
        pickle.dump(doctors, f, pickle.HIGHEST_PROTOCOL)

def load_data():
    doctor_list = []
    if(os.path.exists("doctors.pkl")):
        with open("doctors.pkl", "rb") as f:
            doctor_list = pickle.load(f)

    return (doctor_list)