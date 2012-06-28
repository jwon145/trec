#!/usr/bin/python

import time
import argparse
import sqlite3
import sys
import os

default_db = "hours.db"
table_id = "12s1"
weeks = ['wk01', 'wk02', 'wk03', 'wk04', 'wk05', 'wk06', 'wk07', 'mdsm', 'wk08', 'wk09', 'wk10', 'wk11', 'wk12', 'stvc', 'exm1', 'exm2', 'exm3']

def load_db():
	return sqlite3.connect(default_db)

class init_db(argparse.Action):
	def __call__(self, parser, namespace, values, opt_str):
		conn = load_db()
		with conn:
			cur = conn.cursor()
			cur.execute("DROP TABLE IF EXISTS courses%s" % (table_id))
			cur.execute("DROP TABLE IF EXISTS times%s" % (table_id))
			cur.execute("DROP TABLE IF EXISTS weeks%s" % (table_id))

			cur.execute("CREATE TABLE courses%s (id integer primary key asc autoincrement, name string)" % (table_id))
			init_classes = []
			for c in values:
				init_classes.append((None, c))
			cur.executemany("INSERT INTO courses%s VALUES(?, ?)" % (table_id), init_classes)

			cur.execute("CREATE TABLE weeks%s (id integer primary key asc autoincrement, name string)" % (table_id))
			init_weeks = []
			for week in weeks:
				init_weeks.append((None, week))
			cur.executemany("INSERT INTO weeks%s VALUES(?, ?)" % (table_id), init_weeks)

			cur.execute("CREATE TABLE times%s (cid integer, date integer, time integer, week integer, foreign key(cid) references courses%s(id), foreign key(week) references weeks%s(id))" % (table_id, table_id, table_id))
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
