import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# # Recursive function to print the data structure of a collection and all subcollections
# def print_collection_data(collection):
#     print(f'Collection: {collection.id}')
#     docs = collection.get()
#     for doc in docs:
#         print(f'Document ID: {doc.id}')
#         doc_data = doc.to_dict()
#         if doc_data:
#             for field_name, field_value in doc_data.items():
#                 print(f'{field_name}: {field_value}')
#         for subcollection in doc.reference.collections():
#             print_collection_data(subcollection)

# # Loop through all top-level collections in the database
# for collection in db.collections():
#     print_collection_data(collection)

# Retrieve the data from a Firestore collection
collection_ref = db.collection('products')
docs = collection_ref.stream()

# Create a list of dictionaries containing the field values for each document
data = []
for doc in docs:
    doc_dict = doc.to_dict()
    if doc_dict:
        data.append(doc_dict)

# Create a Pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# saving the dataframe
df.to_csv('products.csv')