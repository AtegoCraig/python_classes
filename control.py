while True:
    print('menu')
    print('1. Add a new student')
    print('2. View all students')
    choice = input('Enter your choice: ')

    if choice == '1':
        print('Adding a new student...')
    elif choice == '2':
        print('Viewing all students...')
        break
    else:
        print('Invalid choice, please try again.')
    