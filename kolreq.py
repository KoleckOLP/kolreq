import os
from getch import getch  # py-getch


# ==========Multiplatform Clear========== #
def clear():
    if(os.name == 'nt'):  # Windows
        os.system('cls')
    elif(os.name == 'posix'):  # Linux,Mac,BSD,haiku,android
        os.system('clear')


# ==========Multiplatform Readkey========== #
def readchar(o=""):  # multiplatform readchar
    print(o, end="", flush=True)  # writes text before the getch, no new line, flush output
    x = getch()
    if isinstance(x, bytes):  # fix if returned in bytes, need to fix when input is arrow keys
        try:  # fixes bug where one key sending multiple characters caused decode error
            x = x.decode("UTF-8")
        except UnicodeDecodeError:
            x = ' '
    x = x.lower()
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
