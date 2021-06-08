#Passoword Checker

username = input('Please enter username: ')
password = input('Please enter the password: ')
hidden_pass = '*' * len(password)
pass_len = len(password)

print(f'{username}, Your password {hidden_pass} is {pass_len} letters long')