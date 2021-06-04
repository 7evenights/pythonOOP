class BOOK:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices



def main():
    book1 = BOOK("Conan", 40)
    print(book1.name)
main()

