import sys

builtin_commands = ["exit", "echo", "type"]

def handle_input(user_argument):
    if "type" == user_argument.split(" ")[0]:
        if user_argument.split(" ")[1] in builtin_commands:
            sys.stdout.write(f"{user_argument.split(" ")[1]} is a shell builtin\n")
        else:
            sys.stdout.write(f"{user_argument.split(" ")[1]} not found\n")

    elif user_argument == "exit 0":
        return False
    elif "echo" == user_argument.split(" ")[0]:
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
