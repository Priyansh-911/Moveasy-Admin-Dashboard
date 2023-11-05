# from flask import Flask, render_template, request,session, redirect, url_for
import json

import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("locationapp-25208-firebase-adminsdk-y0b6s-33be61cc2b.json")
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
