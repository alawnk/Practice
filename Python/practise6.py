count_user_name = 0
count_passwd = 0
name = 'alawn'
passwd = '123'
print (name)

while count_user_name < 3:
    count_user_name = count_user_name + 1
    user_name = input('plz input youre name:')
    if user_name != name and count_user_name==3:
        print('sorry')
    elif user_name != name :
        print('plz try again!')
    else:
        while count_passwd < 3:
            count_passwd = count_passwd + 1
            user_passwd = input('plz input youre passwd:')
            if user_passwd != passwd and count_passwd == 3:
                print('passwd is not correct')
                break
            elif user_passwd != passwd:
                print('plz try again!')
            else:
                print ('Welcome',name)
                break
        break