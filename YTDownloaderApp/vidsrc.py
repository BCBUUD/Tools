import imdb
import webbrowser
import time 


def movien():
    movie = input("\nMovie: ")
    MovieCrawler = imdb.IMDb() # imdb api 
    results = MovieCrawler.search_movie(movie) # searching...
    mv = results[0] #First result
    URL = MovieCrawler.get_imdbURL(mv) #URL for first result
    imdurl = URL
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf 
    print("\n[L] Link \n[B] Browser")
    option = input("\n")
    if option == "l":
        print("\nMovie Link: ", x)
    if option == "b":
        print("Playing in WebBrowser...")
        webbrowser.open(x)



def series():
    seris = input("\nSeries: ")
    MovieCrawler = imdb.IMDb()
    results = MovieCrawler.search_movie(seris)
    mv = results[0] #First result
    URL = MovieCrawler.get_imdbURL(mv) #URL for first result
    imdurl = URL
    seasonx = input("Season (in 01-15 format): ")
    episodex = input("Episode (in 01-15 format): ") 
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf + seasonx + "-" + episodex 
    print("\n[L] Link \n[B] Browser")
    option = input("\n")
    if option == "l":
        print("\nShow Link: ", x)
    if option == "b":
        print("Playing in WebBrowser...")
        webbrowser.open(x)

                

print("\n[1] Movie \n[2] Series")
decis = int(input("\n>> "))
if decis == 1:
    movien()
if decis == 2:
    series()

for i in range(30):
    print("(r)Reselect")
    print("(q)Quit")
    rangeinput = input(">> ")
    while True:
        while True:
            answer = str(input('Anything else? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")

        if answer == 'y':
            print("\n[1] Movie \n[2] Series")
            decis = int(input("\n>> "))
            if decis == 1:
                movien()
            if decis == 2:
                series()
        if answer == 'n':
            exit()
        else:
            print(" ")
            break
    
    if rangeinput == "q":
        exit()
