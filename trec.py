#!/usr/bin/python

import time
import optparse
import sys
import os

version = "0.1"

def getopts():
	parser = optparse.OptionParser("usage: %prog [arguments]")
	parser.add_option("-v", "--version", help="print version info", action="store_true", dest="show_version", default=False)
	(options, remainder) = parser.parse_args()
	return options

def start_timer():
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		print "%d" % (count)

def show_version():
	print "%s v%s" % (os.path.basename(sys.argv[0]), version)

def main():
	options = getopts()
	if options.show_version:
		show_version()
		sys.exit()

	start_timer()

if __name__ == "__main__":
	main()
