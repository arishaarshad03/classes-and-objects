class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def get_details (self):
        return f"title: {self.title}\ndirector: {self.director},\nduration: {self.duration}"
    
    def set_details(self, new_title, new_dir, new_duration):
        self.title = new_title
        self.director= new_dir
        if new_duration > 0:
            self.duration = new_duration
        else:
            print("duration should be a positve number")
    

    def summary(self):
        print(self.title, "is directed by", self.director, "and it runs for", self.duration, "mins")
    
    def length (self):
        if self.duration > 150:
            print(self.title, "is a long movie")
        else:
            print(self.title ,"is a short movie")


interstellar = Movie("interstellar", "Christopher Nolan", 180)
apart= Movie("5 feets apart","justin baldoni", 120)
inception = Movie("inception", "cristopher nolan", 150)

fav_movies = [interstellar, apart, inception]

for m in fav_movies:
    print(m.get_details())
   
for time in fav_movies:
    time.length()

total = 0
for film in fav_movies:
    total = total + film.duration

print ("total watch time: ", total ,"mins")


