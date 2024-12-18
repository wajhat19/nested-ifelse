while True:
    print('1.payment failed')
    print('2.profile and privacy')
    print('3.money transfer')
    print('4.exit')
    user_inp=int(input('enter your choice'))
    if user_inp==1:
        print('welcome tp payment failed')
        print('1.issue with payment failed')
        print('2.issue with pending payment')
        print('3.issue with succeful payment')
        print('4.back')
        user_inp=int(input('select payment issue'))
        if user_inp==1:
            print('issue with payment')
        elif user_inp==2:
            print('issue with pending payment')
        elif user_inp==3:
            print('issue with succeful payment')
        elif user_inp==4:
            print('back')
            break
    elif user_inp==2:
        print('welcome to profilr and privacy')
        print('1.my phonepe profile')
        print('2.payment methode')
        print('3.payment management')
        print('4.back')
        user_inp=int(input('select p&p option'))
        if user_inp==1:
            print('my phonpe profile')
        elif user_inp==2:
            print('payment methode')
        elif user_inp==3:
            print('payment methode')
        elif user_inp==4:
            print('back')    
    elif user_inp==3:
        print('welcome to money transfer')
    elif user_inp==4:
        print('exit')
        break            