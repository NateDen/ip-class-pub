from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for, json, jsonify
import records
import json
import psycopg2
#import collections

app = Flask(__name__, static_url_path='')
db = records.Database('postgresql://denpna01:@knuth.luther.edu/denpna01')  
conn = psycopg2.connect(database="denpna01",user="denpna01",host='knuth.luther.edu',port='5432')
cursor = conn.cursor()

#this function is for finding out the results and displaying it properly  
@app.route('/save',methods = ['POST'])
def save(): 
    table = request.get_json()  
    
    # check if database already has these items or not 
    # (user saves list containing 5 apples previously, then makes a new list, with 
    # top entry having 10 apples, then last entry having 20 apples)
    for row in table:
        db_row = db.query("SELECT * FROM shopping_list_1 WHERE item_name='" + row['name'] + "'" + " AND store='"  + row['store'] + "'" + " AND section='" + row['section'] + "'" " AND price='" + row['price'] + "';")           
        for item in db_row:
            if item['item_name'] == row['name'] and item['store'] == row['store'] and item['section'] == row['section'] and item['price'] == row['price']:
                new_quantity = item['quantity'] + row['quantity']                
                cursor.execute("UPDATE shopping_list_1 SET quantity = (%s) WHERE price = (%s) AND name = (%s) AND section = (%s) AND store = (%s)", (new_quantity, row['price'], row['name'], row['section'], row['store']));
                conn.commit()
            else:
                cursor.execute("INSERT INTO movies (item_name, item_quantity, store, section, price) VALUES (%s, %s, %s, %s, %s)", (row['name'], row['store'], row['section'], row['price']));
        
    cursor.close()         

@app.route('/get',methods = ['POST', 'GET'])
def get():
    table = db.query('SELECT * FROM shopping_list_1') 
    for row in table:
        send_to_client = row.export('json')
        return send_to_client                    
  
@app.route('/')
def hello_world():    
    return app.send_static_file('SL.html')

if __name__ == '__main__':
    app.debug = True
    debug = True
    app.run(debug = True)