import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("locationapp.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def itemsInStore():
    locs = db.collection("location")
    doc = locs.stream()

    res_location = []

    for i in doc:
        location_dict = i.to_dict()
        resLoc = {'lats': location_dict["latitude"], 'long': location_dict["longitude"],
                  "VehicleID": f'{location_dict["name"]}'}

        res_location.append(resLoc)
    return res_location
