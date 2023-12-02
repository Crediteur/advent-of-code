import os
import json
import requests
import argparse


# https://github.com/wesleywchang/AdventOfCodeScraper/blob/main/scraper_tools.py
def make_request_aoc(url: str, cookie: str) -> str:
    try:
        # http response
        raw = requests.get(f"{url}", timeout=3, cookies={"session": cookie}).content
        data = raw.decode("utf8")
    except:
        raise ValueError(f"Error requesting data from {url}")

    return data


# go to local directory and check if folder exists
# otherwise create the folder and data file
def create_aoc_dir(new_dir: str, data: str) -> None:
    # name of text file to be created
    FILENAME = "input.txt"

    # check if directory folders exist
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"new folder created at: {new_dir}")

    # check if data file exists
    exists = False
    if os.path.exists(f"{new_dir}/{FILENAME}"):
        exists = True

    # https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
    f = open(f"{new_dir}/{FILENAME}", "w")  # open file in write mode
    f.write(data.rstrip("\r\n"))
    f.close()

    if exists:
        print(f"updated {FILENAME} at: {new_dir}/{FILENAME}")
    else:
        print(f"new {FILENAME} created at: {new_dir}/{FILENAME}")


# make file available to run from cli
parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", type=int)
parser.add_argument("-d", "--day", type=int)
args = parser.parse_args()

# get env variables from data.json
main_dir = json.load(open("./data.json"))["directory"]
cookie = json.load(open("./data.json"))["cookie"]

# variables
year = args.year
day = args.day
url = f"https://adventofcode.com/{year}/day/{day}/input"

# create directory of folder and file location
new_dir = f"{main_dir}/{year}/day{day:02d}"

create_aoc_dir(new_dir, make_request_aoc(url, cookie))
