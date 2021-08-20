from pymongo import MongoClient
import pprint

client=MongoClient()
print(client)
db=client.project0
print(db)

print(db.list_collection_names())

 #1
# for project0 in db.restaurantsp0.find():
#      pprint.pprint(project0)

 #2
# for project0 in db.restaurantsp0.find({},{'restaurants_id':1 , 'name': 1, 'borough': 1, 'cuisine': 1}):
#     pprint.pprint(project0)

#3
# for project0 in db.restaurantsp0.find({},{'restaurants_id':1 , 'name': 1, 'borough': 1, 'cuisine': 1, '_id' : 0}):
#      pprint.pprint(project0)

# #4
# for project0 in db.restaurantsp0.find({},{'restaurants_id':1 , 'name': 1, 'borough': 1, 'address.zipcode': 1, '_id' : 0}):
#      pprint.pprint(project0)

# #5 
# for project0 in db.restaurantsp0.find({},{'borough': 'Bronx'}):
#      pprint.pprint(project0)

# #6
# for project0 in db.restaurantsp0.find({},{'borough': 'Bronx'}).limit(5):
#      pprint.pprint(project0)

# #7
# for project0 in db.restaurantsp0.find({},{'borough': 'Bronx'}).skip(5).limit(5):
#      pprint.pprint(project0)

# #8
# for project0 in db.restaurantsp0.find({"grades.score" : {'$gt':90}}):
#      pprint.pprint(project0)

# #9
# for project0 in db.restaurantsp0.find({"grades.score":{'$gt':80 , '$lt':100}}):
#      pprint.pprint(project0)

# #10
# for project0 in db.restaurantsp0.find({"address.coord":{'$lt':-95.754168}}):
#      pprint.pprint(project0)

# #11
# for project0 in db.restaurantsp0.find({'$and':[{"cuisine":{'$ne':"American"}},{"grades.score":{'$gt':70}},{"address.coord":{'$lt':-65.754168}}]}):
#      pprint.pprint(project0)

# #12
# for project0 in db.restaurantsp0.find({"cuisine":{'$ne':"American"},"grades.score":{'$gt':70},"address.coord":{'$lt':-65.754168}}):
#      pprint.pprint(project0)

#13
# from pymongo import ASCENDING, DESCENDING
# for project0 in db.restaurantsp0.find({"$and":[{"cuisine" : {"$ne" :"American "}}, {"grades.grade" : {"$gte" : "A"}}, {"borough" : {"$ne" :"Brooklyn"}} ] } ).sort([('cuisine', DESCENDING)]):
#      pprint.pprint(project0)

#14
# for project0 in db.restaurantsp0.find({"name": {"$regex": "^Wil"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1}):
#      pprint.pprint(project0)

#15  
# for project0 in db.restaurantsp0.find({"name": {"$regex": "ces$"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1}):
#     pprint.pprint(project0)

#16
# for project0 in db.restaurantsp0.find({"name": {"$regex": ".*Reg.*"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1}):
#     pprint.pprint(project0)

# 17
# for project0 in db.restaurantsp0.find({"borough": "Bronx" ,  "$or" : [ { "cuisine" : "American " }, { "cuisine" : "Chinese" }]}):
#     pprint.pprint(project0)

# 18
# for project0 in db.restaurantsp0.find({"borough" :{"$in" :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 }):
#     pprint.pprint(project0)

# 19
# for project0 in db.restaurantsp0.find({"borough" :{"$nin" :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 }):
#     pprint.pprint(project0)

#20
# for project0 in db.restaurantsp0.find({"grades" : { "$elemMatch":{"score":{"$lt":10}}}},{ "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 }):
#     pprint.pprint(project0)

# 21
# for project0 in db.restaurantsp0.find({"$or": [{"name": "^Wil"},{"$and": [{"cuisine" : {"$ne" :"American "}},{"cuisine" : {"$ne" :"Chinees"}}]}]} ,{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
#     pprint.pprint(project0)

# 22
# for project0 in db.restaurantsp0.find({"grades.date.ISODate":{"ISODate":("2014-08-11T00:00:00Z")},"grades.grade":"A" ,"grades.score" : 11},{"restaurant_id" : 1,"name":1,"grades":1}):
#     pprint.pprint(project0)

# 23
# for project0 in db.restaurantsp0.find({"grades.1.date": "ISODate"("2014-08-11T00:00:00Z"),"grades.1.grade":"A" ,"grades.1.score" : 9},{"restaurant_id" : 1,"name":1,"grades":1}):
#     pprint.pprint(project0)

#24
# for project0 in db.restaurantsp0.find({"address.coord.1": {"$gt" : 42, "$lte" : 52}},{"restaurant_id" : 1,"name":1,"address":1,"coord":1}):
#     pprint.pprint(project0)

# 25
# from pymongo import  ASCENDING, DESCENDING
# for project0 in db.restaurantsp0.find().sort([('name', ASCENDING)]):
#     pprint.pprint(project0)

# 26
#from pymongo import  ASCENDING, DESCENDING
# for project0 in db.restaurantsp0.find().sort([('name', DESCENDING)]):
#     pprint.pprint(project0)

# 27
# from pymongo import  ASCENDING, DESCENDING
# for project0 in db.restaurantsp0.find().sort([("cuisine",ASCENDING),("borough",DESCENDING)]):
#     pprint.pprint(project0)

# 28
# for project0 in db.restaurantsp0.find({"address.street" :{ "$exists" : "true" }}):
#     pprint.pprint(project0)

# 29
# for project0 in db.restaurantsp0.find({"address.coord" :{"$type" : 1}}):
#     pprint.pprint(project0)

# 30
# for project0 in db.restaurantsp0.find({"grades.score" :{"$mod" : [7,0]}},{"restaurant_id" : 1,"name":1,"grades":1}):
#     pprint.pprint(project0)

# 31
# for project0 in db.restaurantsp0.find({"name" :{ "$regex": ".*mon.*"}},{"name":1,"borough":1,"address.coord":1,"cuisine" :1}):
#      pprint.pprint(project0)

# 32
# for project0 in db.restaurantsp0.find({"name":{ "$regex": "^mad"}},{"name":1,"borough":1,"address.coord":1,"cuisine" :1}):
#      pprint.pprint(project0)









