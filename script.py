#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import csv
import argparse

# cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("courses_txt", help="The path to the courses.txt file. (Default: courses.txt)")
args = parser.parse_args()

classes = []

with open(args.courses_txt) as f:
	line = f.readline()
	line = line.rstrip()
	classes.append(line)
	course = line.split(" ")[0]
	code = line.split(" ")[1]
	cmd = f'curl \"https://anex.us/grades/?dept={course}&number={code}\" -o table-{course}-{code}.html'
	print(cmd)
	os.system(cmd)



for str in classes:
	course = str.split(" ")[0]
	code = str.split(" ")[1]

	html = open(f'table-{course}-{code}.html').read()
	soup = BeautifulSoup(html, features="html.parser")
	table = soup.find("table")
	print(table)

	output_rows = []
	for table_row in table.findAll("tr"):
		columns = table_row.findAll("td")
		output_row = []
		for column in columns:
			output_row.append(column.text)
			output_rows.append(output_row)

	with open(f'grades-{course}-{code}.csv', "wb") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(output_rows)
