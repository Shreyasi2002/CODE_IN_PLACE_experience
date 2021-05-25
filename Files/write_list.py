import json

def write_data():
	data = ["Rorschach", "Silk Spectre"]
	with open("data.json", "w") as f:
		json.dump(data, f, indent=4)

def main():
    write_data()

if __name__ == "__main__":
    main()
