import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('SQLite/salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT c.company_name, e.employee, e.post, p.total
FROM companies c
    LEFT JOIN employees e ON e.company_id = c.id
    LEFT JOIN payments p ON p.employee_id = e.id
WHERE p.total > 5000
    AND  p.date_of BETWEEN  '2021-07-10' AND  '2021-07-20'
"""

print(execute_query(sql))

# company_name             |employee             |post                       |total|
# -------------------------+---------------------+---------------------------+-----+
# Thomas and Sons          |Alexandria Montgomery|Careers information officer| 9213|
# Thomas and Sons          |Amy Hudson           |Careers information officer| 6907|
# Thomas and Sons          |Donald Diaz          |Exhibition designer        | 7917|
# Thomas and Sons          |Sheri Barrera        |Occupational psychologist  | 9268|
# Thomas and Sons          |Victor Miller        |Exhibition designer        | 9412|
# Thomas and Sons          |Zachary Williams     |Site engineer              | 5601|
# Moran, Johnson and Miller|Matthew Campbell     |Technical sales engineer   | 8001|
# Moran, Johnson and Miller|Sarah Hunter         |Site engineer              | 6672|
# Moran, Johnson and Miller|Steven Briggs        |Exhibition designer        | 9810|
# Moran, Johnson and Miller|William Robbins      |Careers information officer| 6864|
# Warner PLC               |Curtis Hanson        |Exhibition designer        | 8062|
# Warner PLC               |Douglas Montoya      |Site engineer              | 6048|
# Warner PLC               |Dustin Proctor       |Occupational psychologist  | 5041|
# Warner PLC               |Joanna Perkins       |Technical sales engineer   | 6484|
# Warner PLC               |Michelle Reid        |Site engineer              | 6204|
# Warner PLC               |Paula Cantu          |Exhibition designer        | 8799|

# [('Thomas and Sons', 'Alexandria Montgomery', 'Careers information officer', 9213), ('Thomas and Sons', 'Amy Hudson', 'Careers information officer', 6907), ('Thomas and Sons', 'Donald Diaz', 'Exhibition designer', 7917), ('Thomas and Sons', 'Sheri Barrera', 'Occupational psychologist', 9268), ('Thomas and Sons', 'Victor Miller', 'Exhibition designer', 9412), ('Thomas and Sons', 'Zachary Williams', 'Site engineer', 5601), ('Moran, Johnson and Miller', 'Matthew Campbell', 'Technical sales engineer', 8001), ('Moran, Johnson and Miller', 'Sarah Hunter', 'Site engineer', 6672), ('Moran, Johnson and Miller', 'Steven Briggs', 'Exhibition designer', 9810), ('Moran, Johnson and Miller', 'William Robbins', 'Careers information officer', 6864), ('Warner PLC', 'Curtis Hanson', 'Exhibition designer', 8062), ('Warner PLC', 'Douglas Montoya', 'Site engineer', 6048), ('Warner PLC', 'Dustin Proctor', 'Occupational psychologist', 5041), ('Warner PLC', 'Joanna Perkins', 'Technical sales engineer', 6484), ('Warner PLC', 'Michelle Reid', 'Site engineer', 6204), ('Warner PLC', 'Paula Cantu', 'Exhibition designer', 8799)]