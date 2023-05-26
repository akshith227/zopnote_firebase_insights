import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

merchant_data = []

merchants = db.collection("merchants")
merchant_snapshots = merchants.get()

for merchant in merchant_snapshots:
    # dictionary to be added to merchant_data
    merchant_obj = {}

    # process to treat the individual merchant as a new path to get collections from
    merchant_ref = merchant.reference
    subcollections = merchant_ref.collections()

    #get head level document data of the merchant
    merchant_docs = merchant_ref.get().to_dict()
    if 'ownerName' in merchant_docs:
      merchant_obj['ownerName'] = merchant_docs['ownerName']
    else:
      merchant_obj['ownerName'] = None
    if 'name' in merchant_docs:
      merchant_obj['name'] = merchant_docs['name']
    else:
      merchant_obj['name'] = None

    if 'billed' in merchant_docs:
      merchant_obj['billed'] = merchant_docs['billed']
    else:
      merchant_obj['billed'] = None

    if 'pending' in merchant_docs:
      merchant_obj['pending'] = merchant_docs['pending']
    else:
      merchant_obj['pending'] = None

    if 'paidCash' in merchant_docs:
      merchant_obj['paidCash'] = merchant_docs['paidCash']
    else:
      merchant_obj['paidCash'] = None  

    if 'paidOnline' in merchant_docs:
      merchant_obj['paidOnline'] = merchant_docs['paidOnline']
    else:
      merchant_obj['paidOnline'] = None

    merchant_obj['id'] = merchant.id
    # merchant_data.append(merchant_obj)
    if merchant.id == "6a77e0b1-6491-4afe-8f62-af84ebebb0c1":
      for subcollection in subcollections:
          subcollection_docs = subcollection.get()
          scname = subcollection.id
          if scname == "brrr":
            for doc in subcollection_docs:
              data = doc.to_dict()
          elif scname == "customers":
            for doc in subcollection_docs:
              data = doc.to_dict()
              if 'firstName' in data:
                firstName = data['firstName']
              if 'addressLine2' in data:
                addressline2 = data['addressLine2']
              cid = data.id

# print(merchant_data[4])