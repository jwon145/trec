#!/usr/bin/python

import time
import argparse
import sqlite3
import sys
import os

default_db = "hours.db"
semm_tag = "12s1"
weeks = ['wk01', 'wk02', 'wk03', 'wk04', 'wk05', 'wk06', 'wk07', 'mdsm', 'wk08', 'wk09', 'wk10', 'wk11', 'wk12', 'stvc', 'exm1', 'exm2', 'exm3']

def load_db():
	return sqlite3.connect(default_db)

class init_db(argparse.Action):
	def __call__(self, parser, namespace, values, opt_str):
		conn = load_db()
		with conn:
			cur = conn.cursor()
			cur.execute("DROP TABLE IF EXISTS courses%s" % (semm_tag))
			cur.execute("DROP TABLE IF EXISTS times%s" % (semm_tag))
			cur.execute("DROP TABLE IF EXISTS weeks%s" % (semm_tag))

			cur.execute("CREATE TABLE courses%s (id integer primary key asc autoincrement, name string)" % (semm_tag))
			init_classes = []
			for c in values:
				init_classes.append((None, c))
			cur.executemany("INSERT INTO courses%s VALUES(?, ?)" % (semm_tag), init_classes)

			cur.execute("CREATE TABLE weeks%s (id integer primary key asc autoincrement, name string)" % (semm_tag))
			init_weeks = []
			for week in weeks:
				init_weeks.append((None, week))
			cur.executemany("INSERT INTO weeks%s VALUES(?, ?)" % (semm_tag), init_weeks)

			cur.execute("CREATE TABLE times%s (course_id integer, date integer, time integer, week_id integer, foreign key(course_id) references courses%s(id), foreign key(week_id) references weeks%s(id))" % (semm_tag, semm_tag, semm_tag))
		sys.exit()

def start_timer(course, week):
	conn = load_db()
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		#print "%s %s: %d" % (course, week, count)
		with conn:
			cur = conn.cursor()
			cur.execute("INSERT INTO times%s VALUES(%d, strftime('%%s', 'now'), %d, %d)" % (semm_tag, get_id(conn, "course", course), count, get_id(conn, "week", week)))

def get_id(conn, table, tag):
	with conn:
		cur = conn.cursor()
		cur.execute("SELECT * from %ss%s where name = '%s'" % (table, semm_tag, tag))
		return cur.fetchone()[0]

def args_handler():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.1')
	parser.add_argument('-i', help="initialise a new table with courses c1, c2, etc.", nargs='+', metavar=('c1', 'c2'), action=init_db)
	parser.add_argument("course", help="class to record")
	parser.add_argument("week", help="week to record")
	return parser.parse_args()

def main():
	args = args_handler()
	start_timer(args.course, args.week)

if __name__ == "__main__":
	main()
