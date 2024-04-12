import pymongo
import sys

# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.
uri = "mongodb+srv://gyazganoglu:Ko0k4iHSh2evm12N@cluster0.zqfjopx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
  client = pymongo.MongoClient(uri)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "myDatabase"
db = client.myDatabase

# use a collection named "recipes"
my_collection = db["recipes"]

"""recipe_documents = [{ "name": "elotes", "ingredients": ["corn", "mayonnaise", "cotija cheese", "sour cream", "lime"], "prep_time": 35 },
                    { "name": "loco moco", "ingredients": ["ground beef", "butter", "onion", "egg", "bread bun", "mushrooms"], "prep_time": 54 },
                    { "name": "patatas bravas", "ingredients": ["potato", "tomato", "olive oil", "onion", "garlic", "paprika"], "prep_time": 80 },
                    { "name": "fried rice", "ingredients": ["rice", "soy sauce", "egg", "onion", "pea", "carrot", "sesame oil"], "prep_time": 40 }]

# drop the collection in case it already exists
try:
  my_collection.drop()  

# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are your username and password correct in your connection string?")
  sys.exit(1)

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(recipe_documents)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("I inserted %x documents." %(inserted_count))

  print("\n")

# FIND DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 

result = my_collection.find()

if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print("%s has %x ingredients and takes %x minutes to make." %(my_recipe, my_ingredient_count, my_prep_time))
    
else:
  print("No documents found.")

print("\n")

# We can also find a single document. Let's find a document
# that has the string "potato" in the ingredients list.
my_doc = my_collection.find_one({"ingredients": "potato"})

if my_doc is not None:
  print("A recipe which uses potato:")
  print(my_doc)
else:
  print("I didn't find any recipes that contain 'potato' as an ingredient.")
print("\n")

# UPDATE A DOCUMENT
#
# You can update a single document or multiple documents in a single call.
# 
# Here we update the prep_time value on the document we just found.
#
# Note the 'new=True' option: if omitted, find_one_and_update returns the
# original document instead of the updated one.

my_doc = my_collection.find_one_and_update({"ingredients": "potato"}, {"$set": { "prep_time": 72 }}, new=True)
if my_doc is not None:
  print("Here's the updated recipe:")
  print(my_doc)
else:
  print("I didn't find any recipes that contain 'potato' as an ingredient.")
print("\n")

# DELETE DOCUMENTS
#
# As with other CRUD methods, you can delete a single document 
# or all documents that match a specified filter. To delete all 
# of the documents in a collection, pass an empty filter to 
# the delete_many() method. In this example, we'll delete two of 
# the recipes.
#
# The query filter passed to delete_many uses $or to look for documents
# in which the "name" field is either "elotes" or "fried rice".

my_result = my_collection.delete_many({ "$or": [{ "name": "elotes" }, { "name": "fried rice" }]})
print("I deleted %x records." %(my_result.deleted_count))
print("\n")
"""
db = client.sample_mflix

movies = db.movies
theaters = db.theaters

comments = db.comments

#print(list(movies.keys()))
#print(list(theathers.keys()))

filter_com = {'num_mflix_comments' : {"$gte" : 15}  }
print(db.movies.count_documents(filter_com))


filter_com_year = {'num_mflix_comments': {"$gte" : 15},
                   'year' :{'$gte':2000}
                   }

print(db.movies.count_documents(filter_com_year))

filter_com_year_nomovies = {'num_mflix_comments': {"$gte" : 1},
                   'year' :{'$gte':2000},
                   'type' :{'$ne' :'movie'}
                   }
print(db.movies.count_documents(filter_com_year_nomovies))

filter_tomato = {'genres': "Western",
                   'year' :{'$gte':2000},
                   'tomatoes.viewer.rating' :{'$gt' :4.0}
                   }
print(db.movies.count_documents(filter_tomato))


filter_fantasy = {'year': 1990,
                  'genres': 'Fantasy'}

movies_fantasy = db.movies.find(filter_fantasy).limit(3)

for movie in movies_fantasy:
  print(movie['title'])

print(db.movies.count_documents(filter_fantasy))

filter_sort = {
  'genres':{'$in':['Action','Thriller']},
  'year':{'$lt':2000},
  'tomatoes.viewer.rating':{'gte':4},
  'num_mflix_comments':{'&gt':1}
}
movies_sorted = db.movies.find(filter_sort).sort('year', -1)

for mov in movies_sorted:
  print(mov['title'])

print(db.movies_sorted.count_documents(filter_sort))

# 1= ASC, -1= DESC
filtro8 = {'genres':{'$in':['Action', 'Thriller']},
           'year':{'$lt':2000},
           'tomatoes.viewer.rating':{'$gt':4},
           'num_mflix_comments':{'$gt':1}}
 
#print(db.movies.count_documents(filtro8))
 
#for movie in db.movies.find(filtro8).sort("tomatoes.viewer.rating",-1):
  #  print(movie["title"])
 
best_ratted_movie = db.movies.find(filtro8).sort("tomatoes.viewer.rating",-1)
 
for movie_ratted in best_ratted_movie:
    print(movie_ratted["title"])
