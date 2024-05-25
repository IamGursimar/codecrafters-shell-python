import sys


def main():

    sys.stdout.write("$ ")
    sys.stdout.flush()
    # Wait for user input
    argument = input()
    sys.stderr.write(f"{argument}: command not found\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
