#! /usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description="Add or replace copyright information in files.")
parser.add_argument("copyright", help="The file which holds the copyright data.")
parser.add_argument("files", help="The folder or files that the operation should work on.")
#parser.add_argument("-f", help="Choose which extensions the operation should work on.")
#parser.add_argument("-r", help="Choose file extension for the result file.")
args = parser.parse_args()

print(args.copyright)