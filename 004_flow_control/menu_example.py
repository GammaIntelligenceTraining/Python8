user_input = None
while True:
    if not user_input:
        ###################################################
        while True:
            user_input = input('Enter id: ')
            try:
                int(user_input)
                if len(user_input) != 11:
                    raise UserWarning
            except ValueError:
                print('Code is not numeric')
            except UserWarning:
                if len(user_input) > 11:
                    print('Code is too long')
                else:
                    print('Code is too short')
            else:
                print(user_input)
                break
        ######################################################
    user_choice = input('Please choose:\n'
                        '1.Get gender\n'
                        '2.Get date of birth\n'
                        '3.Get region of birth\n'
                        '4.Validate ID\n'
                        '5.Change ID\n'
                        '0.Exit\n'
                        '--> ')
    if user_choice == '1':
        if int(user_input[0]) in range(1, 9):
            if int(user_input[0]) % 2 == 0:
                print('You are Female')
            else:
                print('You are Male')
        else:
            print('Can\'t determine Gender')
    elif user_choice == '2':
        if user_input[0] in ['1', '2']:
            bcent = '18'
        elif user_input[0] in ['3', '4']:
            bcent = '19'
        elif user_input[0] in ['5', '6']:
            bcent = '20'
        elif user_input[0] in ['7', '8']:
            bcent = '21'
        else:
            bcent = None
        print(f'You were born in {user_input[5:7]}.{user_input[3:5]}.{bcent}{user_input[1:3]}')
    elif user_choice == '3':
        pass
    elif user_choice == '4':
        pass
    elif user_choice == '5':
        user_input = None
    elif user_choice == '0':
        print('Good bye!')
        break
    else:
        print('Choice is out of range!')