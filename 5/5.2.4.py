import os, sys


def execute(cmd, args):
    """
        Executes the right function
    """
    if args:
        if cmd == "cd":
            return cd(args)
        elif cmd == "cat":
            return cat(args)
    else:
        if cmd == "pwd":
            print(pwd())
        elif cmd == "ls":
            return ls()
        elif cmd == "exit":
            return exit()
        else:
            return "No such command"

def exit():
    """
        Exits the shell
    """
    sys.exit(0)


def cat(filename):
    """
        Displays the content of a file.
    """
    filename = filename[0]
    with open(filename) as f:
        for line in f:
            print(line, end="")

def ls():
    """
        Lists all files in the current directory.
    """
    list_of_files = [obj for obj in os.listdir(pwd())]
    for item in list_of_files:
        if os.path.isdir(pwd() + "/"  + item):
            index_of_item = list_of_files.index(item)
            list_of_files[index_of_item] = list_of_files[index_of_item] + "/"
            print(list_of_files[index_of_item])
            continue

        print(item)


def pwd():
    """
        Prints out the current working directory.
    """
    return os.getcwd()

def cd(path):
    if len(path) > 1:
        return "Command 'c' only takes in one argument!"

    path = path[0]
    try:
        os.chdir(path)
        pwd()
    except:
        return "No such directory!"


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
