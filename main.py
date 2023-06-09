from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

try:
    conn = psycopg2.connect("dbname='myduka' user='postgres' host='localhost' port='5433' password='softwaredeveloper'")
    print('connected successfuly')
except Exception as e:
    print ("I am unable to connect to the database", e)

@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/products')
def products():
    

    cur = conn.cursor()
    cur.execute("SELECT * from products;")
    rows = cur.fetchall()
    print (rows)
    return render_template('index2.html', rows=rows)

@app.route('/sales')
def sales():
    

    cur = conn.cursor()
    cur.execute("SELECT * from sales;")
    row = cur.fetchall()
    print (row)
    return render_template('index2.html', row=row)

@app.route('/save-product', methods=['POST'])
def save_product():
    name=request.form['name']
    bp=request.form['bp']
    sp=request.form['sp']
    quantity=request.form['quantity']
    print(name, bp, sp, quantity)
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name, buying_price, selling_price, quantity)values(%s, %s, %s, %s)",(name, bp, sp, quantity))
    conn.commit()

    return redirect("/products")

@app.route('/save-sales',methods=['POST'])
def save_sales():
    pid=request.form['pid']
    quantity=request.form['quantity']
    print(pid,quantity)
    cur=conn.cursor()
    cur.execute("INSERT INTO sales(pid,quantity,created_at)VALUES (%s, %s,%s)",(pid,quantity,"now()"))
    conn.commit()

    return redirect("/sales")

app.run(debug=True)

