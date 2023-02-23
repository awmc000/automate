
while True:
    print('Enter your age.')
    global age
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    global password
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

print(f'username: {age}, password: {password}')