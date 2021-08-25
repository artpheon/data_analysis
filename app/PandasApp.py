from sqlalchemy import create_engine
import pandas


dtxt = pandas.read_csv("./app_src/my_employees.txt")
dcsv = pandas.read_csv("./app_src/my_employees.csv")
djson = pandas.read_json("./app_src/my_employees.json")
dxlsx = pandas.read_excel("./app_src/my_employees.xlsx", sheet_name=0)

engine = create_engine('postgresql+psycopg2://artur:python@127.0.0.1:5432/staff')

dsql = pandas.read_sql_table('employees', engine, schema='mystaff')

dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "department": "Department", "phone": "Phone", "address": "Address", "salary": "Salary"},
            axis = 'columns', inplace = True)