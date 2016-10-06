#! /usr/bin/env/python3
import argparse
import re
import os

parser = argparse.ArgumentParser(
    description="Add or replace copyright informatin in files.")
parser.add_argument("copyright", help="The file which holds the copyright")
parser.add_argument(
    "filename", help="The folder or file that the operation should work on")
parser.add_argument(
    "-f", help="Choose which exstension the operation should work on")
parser.add_argument("-r", help="Choose file extension for the result.")
args = parser.parse_args()


#regex pattern to capture everything after BEGIN COPYRIGHT and everything before END COPYRIGHT. 
pattern = "(?<=BEGIN COPYRIGHT)(.|\n)*?(?=END COPYRIGHT)"


def add_copyright(filename):
    # read the copyright file
    copyright_text = read_file(args.copyright)
    
    #read current file contents
    old_f = read_file(filename)
    #use regex to change everything between the markers in the file contents.
    new_f = re.sub(pattern, "\n" + copyright_text, old_f)
    #save the file with the new changes
    return save_file(filename, new_f)


def get_files():
    """
        Gets the file/files, and runs them through the copyright function.
    """
    #if the path given is a directory
    if os.path.isdir(args.filename):
        #if the path does NOT end with "/" then we should add it.
        if not args.filename.endswith("/"):
            args.filename = args.filename + "/"
        #for each file in the directory
        for ffile in os.listdir(args.filename):
            #if user specified an extension, only change the files that have the extension specified.
            if args.f and ffile.endswith(args.f):
                add_copyright(args.filename + ffile)
            #otherwise change all files in directory
            else:
                add_copyright(args.filename + ffile)
    else:
        #change file specified
        add_copyright(args.filename)


def read_file(filename):
    """
        Returns file contents.
    """
    with open(filename) as f:
        file_contents = f.read()
    return(file_contents)


def save_file(filename, edited_content):
    """
        Saves changes to file.
    """
    #if user specifed a different extenstion to save to
    if args.r:
        #get filename and extension from os.path - easy way to split the filename from the extension        
        org_filename, extension = os.path.splitext(filename)

        file_new_name = org_filename + args.r
        
        #write changes to file
        with open(file_new_name, "w") as f:
            f.write(edited_content)
    else:
        #write changes to file
        with open(filename, "w") as f:
            f.write(edited_content)


if __name__ == "__main__":
    #if module is runned as program
    get_files()
