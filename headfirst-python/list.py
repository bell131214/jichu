# coding=utf-8
movies = ["The Holy Grail","The Life of Brian","zhang","The Meaning of Life"]
print movies
#计算长度
print len(movies)
print movies[1]
#增加数据到结尾
movies.append("zhang")
print movies
# pop删除末尾
movies.pop()
print movies
# remove（）删除特定的元素
movies.remove("zhang")
print movies
# insert()插入数据在特定位置
movies.insert(0,"LL")
print movies
movies.remove("LL")
print movies
#增加年份，放在影片名后面
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print movies

