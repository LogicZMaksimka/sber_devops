from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def fill_db(connection, cursor):
    cursor.execute("""
        drop table if exists cacti_table;

        create table if not exists cacti_table (
            family text,
            subtype text,
            spines_length integer
        );

        insert into cacti_table values ('rebutia', 'senilis', 3);
        insert into cacti_table values ('rebutia', 'albiflora', 3);
        insert into cacti_table values ('rebutia', 'miniscula', 1);
        insert into cacti_table values ('echinopsis', 'amblayensis', 3);
        insert into cacti_table values ('echinopsis', 'albispinosa', 4);
        insert into cacti_table values ('mammillaria', 'bocasana', 4);
    """)
    connection.commit()

def read_db(cursor):
    cursor.execute("""select * from cacti_table;""")
    return cursor.fetchall()

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(dbname='cacti', user='postgres', host='db', port=5432, password='123456')
    except:
        return "Unable to connect to the database"
    cur = conn.cursor()
    fill_db(conn, cur)
    filtered_cacties = []
    for row in read_db(cur):
        if row[2] >= 3:
            filtered_cacties.append(row)
    return f"Cacti with spike length >= 3: {str(filtered_cacties)}"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)