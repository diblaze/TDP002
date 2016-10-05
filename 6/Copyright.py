#! /usr/bin/env python3
import argparse, os

parser = argparse.ArgumentParser(
    description="Add or replace copyright information in files.")
parser.add_argument(
    "copyright", help="The file which holds the copyright data.")
parser.add_argument(
    "files", help="The folder or files that the operation should work on.")
parser.add_argument(
    "-f", help="Choose which extensions the operation should work on.")
parser.add_argument("-r", help="Choose file extension for the result file.")
args = parser.parse_args()


def get_files(f, extension=None):
    if os.path.isdir(f):
        files = []
        for file in os.listdir(f):
            # Recursive, first param is the folder + filename
            files.append(get_files(f + file, extension))
        return files
    else:
        try:
            file_buffer = open(f)
            lines = file_buffer.readlines()
            print(lines)
            return lines
        except:
            raise IOError
            
def get_indexes(file_to_read, string_to_find):
    return [i for i, line in enumerate(file_to_read) if string_to_find in line ]

def remove_copyright(f):
    """
        Removes everything between copyright markers.
    """

    begin_indexes = get_indexes(f, "BEGIN COPYRIGHT")
    end_indexes = get_indexes(f, "END COPYRIGHT")

    for x in range(len(begin_indexes) - 1):
        f[begin_indexes[x]: end_indexes[x]] = ""
    return f

filesss = get_files("Search.py")

filesss = remove_copyright(filesss)
print(filesss)