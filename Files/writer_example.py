import csv

def write_data():
	with open("data.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerow(["x", "y"])
		writer.writerows([
			[1,2],
			[2,4],
			[4,6]
		])

def main():
    write_data()

if __name__ == "__main__":
    main()

