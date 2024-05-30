import os
import sys

builtin_commands = ["exit", "echo", "type", "pwd"]
def handle_input(user_argument):
    command_initial = user_argument.split(" ")[0]
    if len(user_argument.split(" ")) > 1:
        command_argument = user_argument.split(" ")[1]
    if "type" == command_initial:
        if command_argument in builtin_commands:
            sys.stdout.write(f"{command_argument} is a shell builtin\n")
        else:
            paths = os.getenv("PATH").split(":")
            for path in paths:
                if os.path.exists(f"{path}/{command_argument}"):
                    sys.stdout.write(f"{command_argument} is {path}/{command_argument}\n")
                    break
            else:
                sys.stdout.write(f"{command_argument} not found\n")
    elif user_argument == "exit 0":
        return False
    elif "echo" == command_initial:
        sys.stdout.write(f"{user_argument.replace("echo", "")}\n")
    elif os.path.exists(f"{command_initial}"):
        sys.stdout.write(os.popen(user_argument).read())        
    elif command_initial == "pwd":
        cwd = os.getcwd()
        abs_path = os.path.abspath(cwd)
        sys.stdout.write(f"{abs_path}\n")
        sys.stdout.flush()
    else:
        sys.stderr.write(f"{user_argument}: command not found\n")
        sys.stdout.flush()


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_argument = input()
        handle_response = handle_input(user_argument)
        if handle_response == False:
            break

if __name__ == "__main__":
    main()
