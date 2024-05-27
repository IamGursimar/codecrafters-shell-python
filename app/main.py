import sys


def handle_input(user_argument):
    sys.stderr.write(f"{user_argument}: command not found\n")
    sys.stdout.flush()


def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_argument = input()
        handle_input(user_argument)


if __name__ == "__main__":
    main()
