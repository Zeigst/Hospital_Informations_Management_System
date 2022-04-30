class Pa_Med:
    """
    A pair of Patient and Medicine assigned to each other.\n
    Used in a list to represent which medicine are being taken by the patient.
    """
    def __init__(self, PatientID, MedicineID):
        self.__PatientID = PatientID
        self.__MedicineID = MedicineID

    def get_PatientID(self):
        return self.__PatientID

    def get_MedicineID(self):
        return self.__MedicineID

    def set_PatientID(self, id):
        self.__PatientID = id

    def set_MedicineID(self, id):
        self.__MedicineID = id

class Pa_Doc:
    """
    A pair of Patient and Doctor assigned to each other.\n
    Used in a list to represent which doctor assigned to which patient.
    """
    def __init__(self, PatientID, DoctorID):
        self.__PatientID = PatientID
        self.__DoctorID = DoctorID

    def get_PatientID(self):
        return self.__PatientID

    def get_DoctorID(self):
        return self.__DoctorID

    def set_PatientID(self, id):
        self.__PatientID = id

    def set_DoctorID(self, id):
        self.__DoctorID = id