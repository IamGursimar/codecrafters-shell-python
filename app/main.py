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
                    sys.stdout.write(
                        f"{command_argument} is {path}/{command_argument}\n"
                    )
                    break
            else:
                sys.stdout.write(f"{command_argument} not found\n")
    elif user_argument == "exit 0":
        return False
    elif "echo" == command_initial:
        sys.stdout.write(f"{user_argument.split(" ",1)[1]}\n")
    elif command_initial == "pwd":
        cwd = os.getcwd()
        abs_path = os.path.abspath(cwd)
        sys.stdout.write(f"{abs_path}\n")
        sys.stdout.flush()
    elif command_initial == "cd":
        if os.path.exists(command_argument):
            os.chdir(command_argument)
        elif command_argument == "~":
            os.chdir(os.environ['HOME'])
        else:
            sys.stderr.write(f"{command_argument}: No such file or directory\n")
        """
        if not any([os.path.exists(os.path.join(p, executable) for p in os.environ["PATH"].split(os.pathsep)]):
        print "can't find %s" % executable

        """
    elif any([os.path.exists(os.path.join(p, command_initial)) for p in os.environ["PATH"].split(os.pathsep)]):
        sys.stdout.write(os.popen(user_argument).read())
    # elif os.path.exists(f"{command_initial}"):
    #     print(os.environ["PATH"])
    #     sys.stdout.write(os.popen(user_argument).read())
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
