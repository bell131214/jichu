#coding=utf-8
#name = ["zhang","ling"]
#res = isinstance(name,list)
#print res
movies = ["The Holy Grail",1975,"Terry Jones & Terrt Gilliam",91,
         ["Graham chapman",
         ["Michael palin","John cleese","Teyyy Gilliam","Eric Idle","tERRY Jones"]]]
for text in movies:
    if isinstance(text,list):
        for text1 in text:
            print text1
    else:
        text