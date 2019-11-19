from ADqueryUser import QryUser

username = "BCRInformatics"
username = "csb003"

userObject = QryUser(username)

for row in userObject:
    print(row)
