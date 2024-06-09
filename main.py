import firebase_admin
from firebase_admin import credentials
from os import environ
from firebase_admin import firestore
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.query import Query

cred = credentials.Certificate(environ["SERVICE_ACCOUNT"])
firebase_app = firebase_admin.initialize_app(cred)

#firestore.client(firebase_app).collection("user").add(document_data={"name": "ifedi-mummy", "age": 20})

data = firestore.client(firebase_app).collection("user").stream()
i: DocumentSnapshot
print(data)
for i in data:
    print(i.get("name"))