import csv

def write_data():
	with open("data.csv", "w") as f:
		columns = ['x', 'y']
		writer = csv.DictWriter(f, fieldnames=columns)
		writer.writeheader()
		writer.writerow({'x': 1, 'y': 2})
		writer.writerow({'x': 2, 'y': 4})
		writer.writerow({'x': 4, 'y': 6})

def main():
    write_data()

if __name__ == "__main__":
    main()
