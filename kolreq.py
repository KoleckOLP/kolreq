import os
from getch import getch  # py-getch


# ==========Multiplatform Clear========== #
def clear():
    if(os.name == 'nt'):  # Windows
        os.system('cls')
    elif(os.name == 'posix'):  # Linux,Mac,BSD,haiku,android
        os.system('clear')


# ==========Multiplatform Readkey========== #
def readchar(shell="", enter=False):  # multiplatform readchar
    print(shell, end="", flush=True)  # writes text before the getch, no new line, flush output
    x = []
    while(True):
        x.append(getch())
        if x[0] != b'\xe0':  # checks if first byte is the not arrow keys
            x = x[0]
            if enter:
                if x == b'\r':
                    return "enter"
            try:
                x = x.decode("UTF-8")  # does fail at "ěščřžýáíé"
            except UnicodeDecodeError:
                x = "error"
            return x

        if len(x) == 2:  # this implementation is probably not multiplatform
            x = x[0]+x[1]
            if x == b'\xe0H':
                x = "up_arrow"
            elif x == b'\xe0P':
                x = "down_arrow"
            elif x == b'\xe0K':
                x = "left_arrow"
            elif x == b'\xe0M':
                x = "right_arrow"
            return x


# ==========Removing .0 from floats========== #
def n(a=""):
    if(isinstance(a, float)):
        a = str(a)
        if(a[-2:] == ".0"):  # if last 2 characters are .0 remove then
            return(a[:-2])
        else:
            return(a)  # if not return the number in original form
    else:
        return(a)
