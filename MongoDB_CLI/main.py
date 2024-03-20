import os

# Accessing environment variables and connect to MongoDB
connect = os.getenv("CONNECT_TO_MONGODB")

# Create a new folder collection in the database:
command = 'db.createCollection("trees")'


# Insert a new document into the collection:
command = """db.trees.insertOne({
    "name": "Trees",
    "description": "Collection of information about trees",
    "contents": ["Oak", "Maple", "Pine", "Birch"]
})"""

# Insert documents for trees with properties
command = """db.trees.insertMany([
    {"name": "Oak", "age": 50, "features": ["tall", "strong wood"]},
    {"name": "Maple", "age": 40, "features": ["colorful leaves", "syrup production"]},
    {"name": "Pine", "age": 30, "features": ["evergreen", "pine cones"]},
    {"name": "Birch", "age": 35, "features": ["distinct bark", "graceful appearance"]}
])"""


# Find a tree document by its name:
command = 'db.trees.findOne({"name": "Oak"})'

# Find all documents in the collection:
command = "db.trees.find({})"

# Update the age of a tree document:
command = 'db.trees.updateOne({"name": "Oak"}, {"$set": {"age": 50}})'

# Add a new feature to the list of features for a tree by its name:
command = 'db.trees.updateOne({"name": "Oak"}, {"$push": {"features": "thrives in acidic soil"}})'

# Delete a tree document by its name:
command = 'db.trees.deleteOne({"name": "Oak"})'

# Delete all documents from a collection:
command = "db.trees.deleteMany({})"
