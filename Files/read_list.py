import json

def get_shopping_list():
	with open("to_buy.json") as f:
		shopping_list = json.load(f)
		print(shopping_list)
		print(len(shopping_list))

def main():
    get_shopping_list()

if __name__ == "__main__":
    main()
