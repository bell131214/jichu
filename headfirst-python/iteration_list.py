# coding=utf-8
fav_movies = ["The Holy Grail",1975,"Terry Jones & Terrt Gilliam",91,
              ["Graham chapman",
               ["Michael palin","John cleese","Teyyy Gilliam","Eric Idle","tERRY Jones"]]]
print fav_movies
for text in fav_movies:
    print text

count = 0
while count<len(fav_movies):
    print fav_movies[count]
    count = count+1