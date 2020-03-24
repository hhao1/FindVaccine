import sqlite3

conn = sqlite3.connect('db.sqlite3')


# 如果是yellow fever，就添上notice
# curr = conn.cursor()
# curr.execute("""Update leads_vaccine
# SET notice='test short of this Vaccine, call pharmacy to order in advance if you need it'
# Where name='Yellow Fever - Country Entry Requirements'""")
# conn.commit()

# 如果疫苗存在
curr = conn.cursor()
Vaccine = "Hepatitis"
query = """SELECT *
FROM leads_vaccine
Where name='{0}'"""
print(query)
curr.execute(query.format(Vaccine))
result = curr.fetchone()
print(result)
print(type(result))

# 插入疫苗
# curr = conn.cursor()
# curr.execute("""INSERT INTO leads_vaccine(name,notice,detail)
# VALUES ("testname","notice","detail")""")
# conn.commit()


# 如果国家存在
# curr = conn.cursor()
# country = 'China'
# query = """SELECT *
# FROM leads_lead
# Where Country_Name={0}"""
# query.format(country)
# curr.execute(query.format(country))

# result = curr.fetchone()
# if (result != None):
#     print(result[0])
# print(isinstance(result, tuple))

# 插入国家
# curr = conn.cursor()
# curr.execute("""INSERT INTO leads_lead(Country_Name)
# VALUES("testname")""")
# conn.commit()


# 更新列表关系
# curr = conn.cursor()
# curr.execute("""INSERT INTO leads_lead_Vaccines(lead_id,vaccine_id)
# VALUES (231,14)""")
# conn.commit()
