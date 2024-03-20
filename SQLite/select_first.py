import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('SQLite/salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT ROUND(AVG(p.total), 2) AS average_total, e.post
FROM payments AS p
LEFT JOIN employees AS e ON p.employee_id = e.id
GROUP BY e.post;
"""

print(execute_query(sql))

# average_total|post                       |
# -------------+---------------------------+
#       5424.36|Careers information officer|
#       5754.32|Exhibition designer        |
#        5275.0|Occupational psychologist  |
#       5338.55|Site engineer              |
#       5776.46|Technical sales engineer   |

# [(5424.36, 'Careers information officer'), (5754.32, 'Exhibition designer'), (5275.0, 'Occupational psychologist'), (5338.55, 'Site engineer'), (5776.46, 'Technical sales engineer')]
