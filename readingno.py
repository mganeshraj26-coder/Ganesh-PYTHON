while True:
    ch = input("Enter a character: ")

    if ch == 'L':
        print("Stopping the program...")
        break

    num = int(input("Enter how many times to print: "))

    for i in range(num):
        print(ch)