import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create an empty DataFrame to store the data
dfs = []
