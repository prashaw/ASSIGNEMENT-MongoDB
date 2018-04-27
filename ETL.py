import codecs
from pymongo import MongoClient
client = MongoClient()
db = client.Demo
print("**************SELECT OPTION*****************")
print("1.Extract data from movies.dat into mongoDB")
print("2.Extract data from ratings.dat into mongoDB")
print("3.Extract data from tags.dat into mongoDB")
choice = input("Chose an option:")


def loadMovies():
    f = codecs.open(r'C:\Users\work\Downloads\movies.dat', 'r', 'utf8')
    for line in f:
        line.strip()
        movieid, title, genre = line.split('::')
        movieid = int(movieid)
        db.movies.insert_one(
            {"movie_id": movieid,
             "title": title,
             "genre": genre
             }
        )
        print(line)
    f.close()


def loadRatings():
    f = codecs.open(r'C:\Users\work\Downloads\ratings.dat', 'r', 'utf8')
    for line in f:
        line.strip()
        userid, movieid, ratings, timestamp = line.split('::')
        userid = int(userid)
        movieid = int(movieid)
        ratings = float(ratings)
        db.ratings.insert_one(  
		   {"user_id": userid,
             "movie_id": movieid,
             "ratings": ratings,
             "timestamp": timestamp
            }
        )
    f.close()


def loadTags():
    f = codecs.open(r'C:\Users\work\Downloads\tags.dat', 'r', 'utf8')
    for line in f:
        line.strip()
        userid, movieid, tag, timestamp = line.split('::')
        userid = int(userid)
        movieid = int(movieid)
        db.tags.insert_one(
            {"user_id": userid,
             "movie_id": movieid,
             "tag": tag,
             "timestamp": timestamp
             }
        )
    f.close()
if choice == "1":
    loadMovies()
elif choice == "2":
    loadRatings()
elif choice == "3":
    loadTags()
else:
    print("Invalid Choice, run again")
