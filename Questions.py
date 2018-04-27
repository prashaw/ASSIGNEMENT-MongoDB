from pymongo import MongoClient
client = MongoClient()
db = client.Demo
print("********************SELECT OPTION***********************")
print("1.Find the genre associated with any movie, for Copycat, enter Copycat")
print("2.Find number of movies in each genre")
print("3.Find user defined tags associated with a movie")
print("4.Find average rating of top 5 movie")
print("5.Find the number of movies a user has rated")
print("6.Find similar users")
print("7.Find tag with highest count")
choice = int(input("Choose an option:"))


def avgRating():
    result = db.ratings.aggregate([
        {
            "$group": {"_id": "$movie_id", "Avg": {"$avg": "$ratings"}}
        },
        {
            "$sort": {"Avg": -1}
        },
		{ 
			"$limit" : 5 
		}
    ])
    for line in result:
        print("Movie ID:", line["_id"], "|", "Avg Rating:", line["Avg"])


def similarUser(user):
    array = list()
    array2 = list()
    result = db.ratings.find(
        {"user_id": user},
        {"_id": 0, "movie_id": 1})
    for record in result:
        array.append(record['movie_id'])
    finalResult = db.ratings.find(
        {"movie_id": {"$in": array}},
        {"_id": 0, "user_id": 1})
    for rec in finalResult:
        array2.append(rec['user_id'])
    ans = set(array2)
    print("User similar to ", user, "are as below:")
    for l in ans:
        print(l)


def noMoviesinGenre():
    genreName = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                 "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    print("Genre", "|", "Count")
    print("-------------------")
    for line in genreName:
        count = db.movies.count({"genre": {"$regex": line}})
        print(line, "|", count)


def tagsinMovie(movieid):
    result = db.tags.find(
        {"movie_id": movieid},
        {"_id": 0, "tag": 1}
    )
    finalResult = list()
    print("The", movieid, "is associated with the following tags")
    for record in result:
        finalResult.append(record["tag"])
    finalResult = set(finalResult)
    print(finalResult)


def noofMoviesUserRated(userid):
    result = db.ratings.find(
        {"user_id": userid},
    ).count()
    print("The number of movies rated by ", userid, "are", result)


def movieGenre(movieid):
    result = db.movies.find(
        {"movie_id": movieid},
        {"_id": 0, "movie_id": 0}
    )
    for record in result:
        print("The movie", record["title"], "is associated with the following genres:", record["genre"])
		
def tagcount():
	result = db.tags.aggregate([
	   {"$group": { "_id": "$tag", "count": {"$sum": 1}}},
	   {
            "$sort": {"count": -1}
        },
		{ 
			"$limit" : 1 
		}
	])
	print(" The top tag was found", result , "times")

if choice == 1:
    movieGenre(input("Enter a movie id:"))
elif choice == 2:
    noMoviesinGenre()
elif choice == 3:
	tagsinMovie(input("Enter a movie id:"))
elif choice == 4:
	avgRating()
elif choice == 5:
    noofMoviesUserRated(input("Enter a user id:"))
elif choice == 6:
    similarUser(input("Enter a User ID:"))
elif choice == 7:
	tagcount()
else:
	print("Invalid Choice.Exiting program.Run again")