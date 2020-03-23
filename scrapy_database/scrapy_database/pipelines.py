# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import os


class ScrapyDatabasePipeline(object):
    def __init__(self):

        self.create_connection()

    def create_connection(self):
        pathofTest = "../../db.sqlite3"
        pathofReal = "../../leadmanager/db.sqlite3"
        self.conn = sqlite3.connect(pathofReal)
        self.curr = self.conn.cursor()

    def store_db(self, item):
        if self.isCountryExist(item):
            if self.isVaccineExist(item):
                if self.isRelationExist(item):
                    pass
                else:
                    self.insertRelation(item)
            else:
                self.insertVaccine(item)
                self.insertRelation(item)
        else:
            if self.isVaccineExist(item):
                self.insertCountry(item)
                self.insertRelation(item)
            else:
                self.insertCountry(item)
                self.insertVaccine(item)
                self.insertRelation(item)

    def isRelationExist(self, item):
        self.curr = self.conn.cursor()
        CountryId = -1
        VaccineId = -1
        if self.isCountryExist(item):
            CountryId = self.getCountryId(item)
        if self.isVaccineExist(item):
            VaccineId = self.getVaccineId(item)
        query = """SELECT *
        FROM leads_lead_Vaccines
        Where lead_id={} AND vaccine_id={}"""
        self.curr.execute(query.format(CountryId, VaccineId))
        result = self.curr.fetchone()
        if result == None:
            return False
        else:
            return True

    def isCountryExist(self, item):
        self.curr = self.conn.cursor()
        Country = item['country']
        query = """SELECT *
        FROM leads_lead
        Where Country_Name='{0}'"""
        self.curr.execute(query.format(Country))
        result = self.curr.fetchone()
        if result == None:
            return False
        else:
            return True

    def isVaccineExist(self, item):
        self.curr = self.conn.cursor()
        Vaccine = item['name'][0]
        query = """SELECT *
        FROM leads_vaccine
        Where name='{0}'"""
        self.curr.execute(query.format(Vaccine))
        result = self.curr.fetchone()
        if result == None:
            return False
        else:
            return True

    def getCountryId(self, item):
        self.curr = self.conn.cursor()
        Country = item['country']
        query = """SELECT *
        FROM leads_lead
        Where Country_Name='{0}'"""
        self.curr.execute(query.format(Country))
        result = self.curr.fetchone()
        return result[0]

    def getVaccineId(self, item):
        self.curr = self.conn.cursor()
        Vaccine = item['name'][0]
        query = """SELECT *
        FROM leads_vaccine
        Where name='{0}'"""
        self.curr.execute(query.format(Vaccine))
        result = self.curr.fetchone()
        return result[0]

    def insertRelation(self, item):
        self.curr = self.conn.cursor()
        country_id = self.getCountryId(item)
        vaccine_id = self.getVaccineId(item)
        query = """INSERT INTO leads_lead_Vaccines(lead_id,vaccine_id)
        VALUES ({},{})"""
        self.curr.execute(query.format(country_id, vaccine_id))
        self.conn.commit()

    def insertVaccine(self, item):
        self.curr = self.conn.cursor()
        Vaccine_Name = item['name'][0]
        Vaccine_Detail = ""
        Vaccine_Notice = ""
        if item['name'][0] == "Yellow Fever - Country Entry Requirements":
            Vaccine_Notice = "There is currently a shortage of yellow fever vaccine in Canada, attributed to the difficulty of producing the yellow fever vaccine, Call pharmacy to order in advance if you need it"
        for i in item['details']:
            Vaccine_Detail += i
        qurey = """INSERT INTO leads_vaccine(name,notice,detail)
VALUES('{}','{}','{}')"""
        self.curr.execute(qurey.format(
            Vaccine_Name, Vaccine_Notice, Vaccine_Detail))
        self.conn.commit()

    def insertCountry(self, item):
        self.curr = self.conn.cursor()
        Country_Name = item['country']
        qurey = """INSERT INTO leads_lead(Country_Name)
VALUES('{0}')"""
        self.curr.execute(qurey.format(Country_Name))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)

        # return item
