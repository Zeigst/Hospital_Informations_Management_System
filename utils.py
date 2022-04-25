def invalid_id(id, para: str):
    """
    Return 1 if invalid | 0 if valid\n
    Exp: ("D-123", "D-") => Valid\n
        ("s-12", "D-")  => Invalid
    """
    while True:
        try:
            id_num = int(id[-3:])
            if id[:2] != para or len(id) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1

def invalid_gend(gend):
    if gend != "M" and gend != "F":
        return 1
    else: return 0

def invalid_dob(dob):
    while True:
        try:
            dd_check = int(dob[:2])
            mm_check = int(dob[:5][-2:])
            yyyy_check = int(dob[-4:])
            check1 = dob[:3][-1:]
            check2 = dob[:6][-1:]
            if len(dob) != 10:
                return 1
            elif check1!="/" or check2!="/":
                return 1
            else: return 0
        except ValueError:
            return 1
