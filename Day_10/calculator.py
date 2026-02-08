def add(num_1, num_2):
    '''
    Add two numbers

    :param num_1: first number
    :param num_2: second number
    '''
    return num_1 + num_2


def subtract(num_1, num_2):
    '''
    Subtract two numbers

    :param num_1: first number
    :param num_2: second number
    '''
    return num_1 - num_2


def multiply(num_1, num_2):
    '''
    Multiply two numbers

    :param num_1: first number
    :param num_2: second number
    '''
    return num_1 * num_2


def devide(num_1, num_2):
    '''
    Devide two numbers

    :param num_1: first number
    :param num_2: second number
    '''
    return num_1 / num_2


def main():
    logo = '''
            _____________________
            |  _________________  |
            | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
            | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
            |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
            | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
            | |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
            | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
            | |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
            | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
            | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
            | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
            | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
            |_____________________|
            '''

    print(logo)
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': devide
    }
    start_task = True
    continue_task = 'n'
    while start_task:
        if continue_task == 'n':
            first_num = int(input("What's the first number?: "))
        if continue_task == 'y':
            first_num = result
        for i in operations:
            print(i)
        picked_operation = input("Pick an operation: ")
        second_num = int(input("What's the next number?: "))
        result = 0

        if picked_operation in operations:
            result = operations[picked_operation](first_num, second_num)
            print(f" {first_num} {picked_operation} {second_num} = {result}")

        else:
            print("Wrong \'operation\' selected. Please select the correct operation")

        continue_task = input(
            f"Type \'y\' to continue calculating with {result}, type \'n\' to start a new calculation or type '\'stop\' to exit: ")

        if continue_task == 'stop':
            start_task = False


if __name__ == '__main__':
    main()
