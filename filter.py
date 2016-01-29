import csv
import os

def filter_prefix():
    with open("subject_files.csv", "rU") as input_file:
        with open("subject_files_filtered.csv", "wb") as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            writer.writerow(["file", "length(s)"])
            for row in reader:
                path = row[0]
                split_path = path.split("/")

                new_path = split_path[5:]
                print new_path
                joined_path = os.path.join(*new_path)
                writer.writerow([joined_path, row[1]])
                # path = os.path.split(row[0])

def filter_name():
    with open("subject_files.csv", "rU") as input_file:
        with open("subject_files_filtered.csv", "wb") as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            reader.next()
            writer.writerow(["file", "length(s)"])
            for row in reader:
                path = row[0]
                filename = os.path.split(path)[1]
                if "_video.mp4" in filename:
                    writer.writerow([path, row[1]])
                else:
                    continue

if __name__ == "__main__":

    # filter_prefix()
    filter_name()


