import sys
import csv
import subprocess
import os
import argparse

from ffprobe import FFProbe

#Initialize variables start_dir; csv_path; output_table; nomp4; nomov; and args
start_dir = ""
csv_path = ""
output_table = []

nomp4 = False
nomov = False

args = None

#Function creates and writes to an output file
def output_csv():

    with open(csv_path, "wb") as file:
        writer = csv.writer(file)
        writer.writerows(output_table)


def walk_tree(path):
    #Loop through files in start_dir and generate file names
    for root, dirs, files in os.walk(path):
        for file in files:
            #Call helper function check_extension to check if file types match (.mp4 or .mov)
            if check_extension(file):
                pathname = os.path.join(root, file)
                metadata = FFProbe(pathname)
                #Time the length of the file in seconds
                try:
                    length = metadata.streams[0].durationSeconds()
                #Throw exception if error is encountered so that the code does not break
                except (IndexError):
                    print os.path.join(root, file) + " was a problem file. skipped."
                    continue
                #Append the times to a table corresponding to the pathname or the file being timed
                output_table.append((pathname, length))

#Helper function that checks if the file type (mp4 or mov) is suitable
def check_extension(filename):
    if filename.endswith(".mp4"):
        return False if nomp4 else True
    if filename.endswith(".mov"):
        return False if nomov else True
    else:
        return False

#Adds print statements
def print_usage():
    print "\nUSAGE:\n"
    print "$: python vidlengths.py directory output_csv [-nomp4] [-nomov]\n"

if __name__ == "__main__":

    print_usage()

    start_dir = sys.argv[1]
    csv_path = sys.argv[2]

    #Set variable nomp4 and nomov to True or False based on the presense of "-nomp4" or "-nomov" in the argument
    if "-nomp4" in sys.argv:
        nomp4 = True
    if "-nomov" in sys.argv:
        nomov = True

    walk_tree(start_dir)
    output_csv()
