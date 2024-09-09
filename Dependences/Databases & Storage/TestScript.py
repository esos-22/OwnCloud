from pymongo import MongoClient

# Set up the MongoDB client
client = MongoClient('mongodb://admin:password@localhost:27017/')

# Connect to the 'test' database
db = client['test']

# Insert a document into 'test_collection'
collection = db['test_collection']
document = {'name': 'Alice', 'age': 25}
result = collection.insert_one(document)

# Print the ID of the inserted document
print(f"Document inserted with ID: {result.inserted_id}")

# Retrieve and print the document
retrieved_document = collection.find_one({'name': 'Alice'})
print("Retrieved Document:", retrieved_document)
