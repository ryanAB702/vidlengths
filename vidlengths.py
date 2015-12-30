import sys
import csv
import subprocess
import os

from ffprobe import FFProbe

start_dir = ""
csv_path = ""
output_table = []

def output_csv():

    with open(csv_path, "wb") as file:
        writer = csv.writer(file)
        writer.writerows(output_table)

def walk_tree(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp4"):
                pathname = os.path.join(root, file)
                metadata = FFProbe(pathname)
                length = metadata.streams[0].durationSeconds()
                output_table.append((pathname, length))
                       
if __name__ == "__main__":
    
    start_dir = sys.argv[1]
    csv_path = sys.argv[2]
    
    walk_tree(start_dir)
    output_csv()

    
