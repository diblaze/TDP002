import os


def execute(cmd, args):
    commands = ["pwd", "cd", "ls", "cat"]
    if cmd in commands:
        if args:
            if cmd == "cd":
                return cd(args)
            elif cmd == "cat":
                return cat(args)
        else:
            if cmd == "pwd":
                return pwd()
            elif cmd == "ls":
                return ls()
    else:
        return "No such command"


def pwd():
    """
        Prints out the current working directory.
    """
    print(os.getcwd())

def cd(path):
    try:
        os.chdir(path)
    except:
        print("There is no such directory!")


def main():
    """
        Main loop for program.
    """
    while True:
        cmd = input("command > ").split(" ")
        cmd, args = cmd[0], cmd[1:]
        execute(cmd, args)

if __name__ == "__main__":
    main()
