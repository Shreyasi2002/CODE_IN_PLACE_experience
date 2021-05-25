import json

def get_ages():
	with open("ages.json") as f:
		ages = json.load(f)

		age = ages["Brahm"]
		print("Brahm is " + str(age))

def main():
    get_ages()

if __name__ == "__main__":
    main()
