import time

def main():
	try:
		count = 0
		while True:
			time.sleep(1)
			count += 1
	except KeyboardInterrupt:
		print "%d" % (count)

if __name__ == "__main__":
	main()
