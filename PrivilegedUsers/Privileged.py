from .QueryADlibrary import searchAD

def start():
    username = "BCRInformatics"
    username = "csb003"

    userObject = searchAD(username)

    for row in userObject:
        print(row)

