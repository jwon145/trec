#!/usr/bin/python

import time
import optparse
import sys
import os

version = "0.1"

def start_timer(subject):
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		print "%s: %d" % (subject, count)

def show_version(args, i, dont, use):
	print "%s v%s" % (os.path.basename(sys.argv[0]), version)
	sys.exit()

def getopts():
	parser = optparse.OptionParser("usage: %prog [class] [week]")
	parser.add_option("-v", "--version", help="print version info", action="callback", callback=show_version)
	(options, args) = parser.parse_args()
	if len(args) != 2:
		parser.print_help()
		sys.exit()
	return (options, args)

def main():
	(options, args) = getopts()
	subject = args[0]
	week = args[1]

	start_timer(subject)

if __name__ == "__main__":
	main()
