from pymongo import MongoClient
from pymongo.server_api import ServerApi


# Connect to the MongoDB server
def connect_to_mongodb():
    client = MongoClient(
        "mongodb+srv://prysiazhnyi:K0kkV2hzS9bu3gZH@cluster0.xak5nml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi("1"),
    )
    return client.book


"""-------------------------------------------------------------------------------"""


# Insert a new document into the collection
def insert_cat(db):
    result = db.cats.insert_one(
        {
            "name": "Moon",
            "age": 3,
            "features": [
                "walks in slippers",
                "allows himself to be stroked",
                "redhead",
            ],
        }
    )
    return result.inserted_id


"""-------------------------------------------------------------------------------"""


# Find a cat document by its name
def find_cat_by_name(db, cat_name):
    result = db.cats.find_one({"name": cat_name})
    return result


# Find all documents in the collection
def find_all_cats(db):
    result = db.cats.find({})
    return result


"""-------------------------------------------------------------------------------"""


# Update the age of a cat document
def update_cat_age(db, cat_name, new_age):
    db.cats.update_one({"name": cat_name}, {"$set": {"age": new_age}})


"""-------------------------------------------------------------------------------"""


# Add a new feature to the list of features for a cat by its name
def add_feature_to_cat(db, cat_name, new_feature):
    # Find the cat document by its name
    cat = db.cats.find_one({"name": cat_name})

    # If the cat is found
    if cat:
        # Add the new feature to the list of features
        cat["features"].append(new_feature)

        # Update the cat document with the new feature
        db.cats.update_one({"_id": cat["_id"]}, {"$set": {"features": cat["features"]}})

        return True  # Return True to indicate success
    else:
        return False  # Return False if the cat is not found


"""-------------------------------------------------------------------------------"""


# Delete a cat document by its name
def delete_cat_by_name(db, cat_name):
    db.cats.delete_one({"name": cat_name})


# Delete all documents from a collection
def delete_all_documents(db, collection_name):
    # Get the collection object
    collection = db[collection_name]

    # Delete all documents from the collection
    result = collection.delete_many({})

    # Return the number of deleted documents
    return result.deleted_count


"""-------------------------------------------------------------------------------"""


# Main function to execute the operations
def main():
    # Connect to MongoDB
    db = connect_to_mongodb()

    # Insert a new cat document
    inserted_id = insert_cat(db)
    print("Inserted cat document ID:", inserted_id)

    # Find a cat document by name
    cat_name = "Moon"
    cat = find_cat_by_name(db, cat_name)
    print("Found cat by name:", cat)

    # Find all cat documents
    all_cats = find_all_cats(db)
    print("All cat documents:")
    for cat in all_cats:
        print(cat)

    # Update the age of a cat document
    new_age = 4
    update_cat_age(db, cat_name, new_age)
    print("Updated cat age to", new_age)

    # Add a new feature to the list of features for a cat by its name
    new_feature = "likes to nap in the sun"
    add_feature_to_cat(db, cat_name, new_feature)
    print("Added new feature to cat:", new_feature)

    # Delete a cat document by name
    delete_cat_by_name(db, cat_name)
    print("Deleted cat by name:", cat_name)

    # Delete all documents from the collection
    collection_name = "cats"
    deleted_count = delete_all_documents(db, collection_name)
    print("Deleted all documents from the collection. Total count:", deleted_count)


if __name__ == "__main__":
    main()


# output:
# Inserted cat document ID: 65f83e5fc150417a35c430c9
# Found cat by name: {'_id': ObjectId('65f83e5fc150417a35c430c9'), 'name': 'Moon', 'age': 3, 'features': ['walks in slippers', 'allows himself to be stroked', 'redhead']}
# All cat documents:
# {'_id': ObjectId('65f83e5fc150417a35c430c9'), 'name': 'Moon', 'age': 3, 'features': ['walks in slippers', 'allows himself to be stroked', 'redhead']}
# Updated cat age to 4
# Added new feature to cat: likes to nap in the sun
# Deleted cat by name: Moon
# Deleted all documents from the collection. Total count: 0
