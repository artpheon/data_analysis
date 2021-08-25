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

dtxt.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
dcsv.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
djson.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
dxlsx.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

query_all = pandas.read_sql_query('SELECT * FROM mystaff.allstaff', engine)
query_count = pandas.read_sql_query('SELECT COUNT (*) FROM mystaff.allstaff', engine)
total_employees = query_count.iloc[0][0]

query_depts = pandas.read_sql_query('SELECT COUNT (DISTINCT "Department") FROM mystaff.allstaff', engine)
total_depts = query_depts.iloc[0][0]

query_epd = pandas.read_sql_query('SELECT "Department", COUNT ("LastName") FROM mystaff.allstaff GROUP BY "Department"', engine)
query_epd.set_index("Department", inplace = True)

log_emp = query_epd.loc['Logistics', 'count']
mar_emp = query_epd.loc['Marketing', 'count']
sal_emp = query_epd.loc['Sales', 'count']

salary_avg = query_all['Salary'].mean()
epd_avg = query_epd['count'].mean()


summary = [
    ['Total number of employees', int(total_employees)],
    ['Total number of departments', int(total_depts)],
    ['Employees in Logistics', int(log_emp)],
    ['Employees in Marketing', int(mar_emp)],
    ['Employees in Sales', int(sal_emp)],
    ['Average salary', int(salary_avg)],
    ['Average employees in departments', int(epd_avg)]
]

summary_html = pandas.DataFrame(summary, columns = ['Stat', 'Value'])

with open('/var/www/hrobbin/result.html', 'w') as f:
    summary_html.to_html(f, index = False, justify='center')