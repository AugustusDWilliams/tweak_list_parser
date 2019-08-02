import os
import re
import csv
import sys
from pathlib import Path


def get_dst(src):
    filename = "tweak_list_parsed.csv"
    p = Path(src)
    dst = str(p.parent / filename)
    return dst

def read_file(filename):
    with open(filename, "r+") as file:
        return file.readlines()

def filter_data(data):
    data = [row.strip() for row in data if row != "\n"]
    return data

def split_data(data):
    i = 0
    output = list()
    while i <= len(data) - 3:
        repo_regex = r"\s(.+)"
        tweak_regex = r'(?:Visible name:\s)(.+)'
        version_regex = r'(?:Version:\s)(.+)'
        repo = re.search(repo_regex, data[i])[1]
        tweak = re.search(tweak_regex, data[i + 1])[1]
        version = re.search(version_regex, data[i + 2])[1]
        output.append([tweak, repo, version])
        i += 3
    return output

def sort_data(data):
    return sorted(data, key=lambda row: row[0])

def write_data(data, output_filename):
    header = ["Tweak", "Repo", "Version"]
    with open(output_filename, "w") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(header)
        writer.writerows(data)

def main(src=None):
    if not src:
        src = sys.argv[1]
    dst = get_dst(src)
    file_data = read_file(src)
    filtered_data = filter_data(file_data)
    tweak_data = split_data(filtered_data)
    sorted_tweak_data = sort_data(tweak_data)
    write_data(sorted_tweak_data, dst)
    print("Tweak List Generated at: {}".format(dst))

if __name__ == "__main__":
    src = sys.argv[1]
    main(src)

