#!/usr/bin/python

import time
import argparse
import sqlite3
import sys
import os

default_db = "hours.db"
table_id = "12s1"
db_conn = None

class init_db(argparse.Action):
	def __call__(self, parser, namespace, values, opt_str):
		print "CREATE TABLE courses%s (id integer primary key asc autoincrement, name string);" % (table_id)
		for c in values:
			print "INSERT INTO courses%s VALUES(null, \"%s\")" % (table_id, c)
		print "CREATE TABLE times%s (cid integer, date integer, time integer, foreign key(cid) references courses%s(id));" % (table_id, table_id)
		sys.exit()

def start_timer(subject, week):
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		print "%s %s: %d" % (subject, week, count)
		# print "INSERT INTO times%s VALUES(%d, strftime('\%s', 'now'), %d)" % (, count, )

def args_handler():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.1')
	parser.add_argument('-i', help="initialise a new table with classes c1, c2, etc.", nargs='+', metavar=('c1', 'c2'), action=init_db)
	parser.add_argument("klass", help="class to record", metavar="class")
	parser.add_argument("week", help="week to record")
	return parser.parse_args()

def main():
	args = args_handler()
	start_timer(args.klass, args.week)

if __name__ == "__main__":
	main()
