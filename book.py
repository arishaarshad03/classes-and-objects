class Book:
    def __init__ (self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info (self):
        print (self.author, "wrote the book", self.title, "and it has", self.pages, "pages")


    def length (self):
        if self.pages> 300:
            print(self.title, "is a long book")
        else:
            print(self.title,"is a short book")


kiteRunner = Book("the kite runner", "Khaled Hosseni", 200)
littleLife = Book("a little life", "Hanya Yanagihara", 700)
vinciCode = Book("The DaVinci code", "Dan Brown", 500)


books = [kiteRunner, littleLife, vinciCode]

for favs in books:
    favs.info()

total =0
for kitaab in books:
    total += kitaab.pages

print ("total pages to read:", total)




# kiteRunner.info()
# kiteRunner.length()
# littleLife.info()
# littleLife.length()
# vinciCode.info()
# vinciCode.length()

