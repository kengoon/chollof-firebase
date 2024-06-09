import firebase_admin
from firebase_admin import credentials
from os import environ
from firebase_admin import firestore
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.query import Query

cred = credentials.Certificate(environ["SERVICE_ACCOUNT"])
firebase_app = firebase_admin.initialize_app(cred)


def on_snapshot(doc_snapshot, changes, read_time):
    print(changes, read_time)
    for change in changes:
        if change.type.name == "ADDED":
            print(f"New city: {change.document.to_dict()}")
        elif change.type.name == "MODIFIED":
            print(f"Modified city: {change.document.to_dict()}")


db_ref = firestore.client(firebase_app).collection("user")
db_ref.on_snapshot(on_snapshot)

while True:
    pass
