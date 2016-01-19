import sys
import csv
import subprocess
import os
import argparse

from ffprobe import FFProbe

start_dir = ""
csv_path = ""
output_table = []

nomp4 = False
nomov = False

args = None

def output_csv():

    with open(csv_path, "wb") as file:
        writer = csv.writer(file)
        writer.writerows(output_table)

def walk_tree(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if check_extension(file):
                pathname = os.path.join(root, file)
                metadata = FFProbe(pathname)
                try:
                    length = metadata.streams[0].durationSeconds()
                except (IndexError):
                    print os.path.join(root, file) + " was a problem file. skipped."
                    continue
                output_table.append((pathname, length))

def check_extension(filename):
    if filename.endswith(".mp4"):
        return False if nomp4 else True
    if filename.endswith(".mov"):
        return False if nomov else True
    else:
        return False

def print_usage():
    print "\nUSAGE:\n"
    print "$: python vidlengths.py directory output_csv [-nomp4] [-nomov]\n"

if __name__ == "__main__":

    print_usage()

    start_dir = sys.argv[1]
    csv_path = sys.argv[2]

    if "-nomp4" in sys.argv:
        nomp4 = True
    if "-nomov" in sys.argv:
        nomov = True

    walk_tree(start_dir)
    output_csv()
