import csv
import os

def filter():
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


if __name__ == "__main__":

    filter()
