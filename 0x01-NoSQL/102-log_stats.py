#!/usr/bin/env python3
'''Task 15's module.
'''
from pymongo import MongoClient
from bson.son import SON

def top_students(mongo_collection):
    # MongoDB aggregation pipeline to calculate the average score and sort by it
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {
            "$sort": SON([("averageScore", -1)])
        }
    ]
    
    # this will run the aggregation pipeline
    results = list(mongo_collection.aggregate(pipeline))
    
    return results

# usage
if __name__ == "__main__":
    # MongoDB connection string and database/collection
    uri = "mongodb://belloabdulmujib:my_password@localhost:27017"
    client = MongoClient(uri)
    db = client['belloabdulmujib']
    collection = db['js_students']
    
    # this will get top students
    top_students_list = top_students(collection)
    
    # Prints the top students
    for student in top_students_list:
        print(student)
    
    # Close the connection
    client.close()
