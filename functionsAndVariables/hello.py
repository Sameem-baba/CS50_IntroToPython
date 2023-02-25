def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(name="World"):
    print("Hello,", name)


main()
