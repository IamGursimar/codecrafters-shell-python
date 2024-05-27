import sys


def handle_input(user_argument):
    if user_argument == "exit 0":
        return False
    elif "echo" in user_argument:
        sys.stdout.write(f"{user_argument.replace("echo", "")}\n")
    else:
        sys.stderr.write(f"{user_argument}: command not found\n")
        sys.stdout.flush()


def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_argument = input()
        handle_response = handle_input(user_argument)
        if handle_response == False:
            break


if __name__ == "__main__":
    main()
