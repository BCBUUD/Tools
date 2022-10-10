import imdb
import webbrowser

def movien():
    movie = input("\nMovie: ")
    ia = imdb.IMDb() # imdb api 
    results = ia.search_movie(movie) # searching...
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf 
    print("Playing in You Webbrowser...")
    webbrowser.open(x)
    print("\nMovie Link: ", x)



def series():
    seris = input("\nSeries: ")
    ia = imdb.IMDb()
    results = ia.search_movie(seris)
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    seasonx = input("Season (in 01-15 format): ")
    episodex = input("Episode (in 01-15 format): ") 
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf + seasonx + "-" + episodex 
    print("Playing in You Webbrowser...")
    webbrowser.open(x)

print("\033[1;32m\n                Visit: https://isg32.github.io/Home                     \n")

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
