#!/usr/bin/python

import time
import optparse
import sqlite3
import sys
import os

version = "0.1"
default_db = "hours.db"
table_id = "12s1"
db_conn = None

def init_db(args, i, dont, use):
	print "CREATE TABLE courses%s(id integer primary key asc autoincrement, name string);" % (table_id)
	classes = list(raw_input("List your class tags delimited by spaces (eg \"cs3901 cs4141 cs9242 en1811\"):\n").rsplit())
	for c in classes:
		print "INSERT INTO courses%s VALUES(null, \"%s\")" % (table_id, c)
	sys.exit()

def start_timer(subject, week):
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		print "%s %s: %d" % (subject, week, count)

def show_version(args, i, dont, use):
	print "%s v%s" % (os.path.basename(sys.argv[0]), version)
	sys.exit()

def args_handler():
	parser = optparse.OptionParser("usage: %prog [class] [week]")
	parser.add_option("-i", "--init", help="initialise a new table", action="callback", callback=init_db)
	parser.add_option("-v", "--version", help="print version info", action="callback", callback=show_version)
	return parser.parse_args()[1] # returns only the positional arguments (ie. class and week) in a list

def main():
	args = args_handler()
	if len(args) != 2:
		sys.stderr.write("Error: Not enough arguments.\n\nSee `%s --help` for more information.\n" % (os.path.basename(sys.argv[0])))
		sys.exit()

	subject = args[0]
	week = args[1]
	start_timer(subject, week)

if __name__ == "__main__":
	main()
