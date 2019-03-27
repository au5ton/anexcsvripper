#!/usr/bin/env python3

import csv
import argparse
import requests
import json

# cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("courses_txt", help="The path to the courses.txt file. (Default: courses.txt)")
args = parser.parse_args()

courses = []

with open(args.courses_txt) as f:
	for line in f:
		line = line.rstrip()
		courses.append(line)
		dept = line.split(" ")[0]
		number = line.split(" ")[1]
		r = requests.post("https://anex.us/grades/getData/", data={"dept": dept, "number": number})
		try:
			json.loads(r.text)
		except Exception:
			print(f'Course {dept}-{number} failed: invalid json')
			continue
		data = json.loads(r.text)

		output_rows = []
		output_rows.append(list(data["classes"][0].keys()))
		#print(output_rows[0])
		for row in data["classes"]: # iterate over objs
			new_row = []
			for key in list(data["classes"][0].keys()): # iterate over keys
				new_row.append(row[key])
			#print(new_row)
			output_rows.append(new_row)

		#print(output_rows)
		with open(f'grades-{dept}-{number}.csv', "w") as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows(output_rows)
