from django.shortcuts import render
from django import db
from django.db import connection


def index(request):
    # client=MongoClient("mongodb+srv://Vaccine:jKGkRrzqrMUjsdPR@cluster0-59clr.mongodb.net/test?retryWrites=true")
    # vp_db=client.get_database('vaccine_project')
    # Country=vp_db.Country
    # Data=Country.find_one()
    # db_name = connection.settings_dict['NAME']
    # db_path = connection.settings_dict['HOST']
    # print("here")
    # print(db_path)
    return render(request, 'frontend/index.html')
# Create your views here.
