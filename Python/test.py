count = 0
lucky_num = '6'
while count < 10:
    count = count + 1
    guess_num = input("num:")
    if guess_num != lucky_num:
        print('plz try again:')
    elif guess_num == lucky_num:
        print('congratulations')
        break