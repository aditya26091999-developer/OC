from flask import Flask,request,jsonify,Response
import sqlite3



app = Flask(__name__)

@app.route('/')
def home():
    return {'message':'Welcome to the online-community-api'}

@app.route('/login',methods=['POST'])
def login():
    conn = sqlite3.connect('oc.db')
    cur = conn.cursor()
    print('\n*****************Connected to the Online-Community Database!*********************\n')
    s_email = request.form['s_email']
    s_password = request.form['s_password']
    try:
        sql = """SELECT sid FROM student WHERE s_email=? AND s_password=?;"""
        values = (s_email,s_password)
        cur.execute(sql,values)
        row = cur.fetchone()
        if row==None:
            return Response("{'error':'Check your credentials'}", status=404, mimetype='application/json')
        else:
            return Response("{'success':'Login Succesfull'}", status=200, mimetype='application/json')
    except Exception as e:
        return Response("{'error':'%s'}"%(e),  status=400, mimetype='application/json')


@app.route('/register',methods=['POST'])
def register():
    conn = sqlite3.connect('oc.db')
    cur = conn.cursor()
    print('\n*****************Connected to the Online-Community Database!*********************\n')

    s_name = request.form['s_name']
    s_email = request.form['s_email']
    s_phone = request.form['s_phone']
    s_password = request.form['s_password']
    try:
        sql = """INSERT INTO student(s_name,s_email,s_phone,s_password) VALUES(?,?,?,?);"""
        values = (s_name,s_email,s_phone,s_password)
        cur.execute(sql,values)
        conn.commit()
        return Response("{'success':'Registration Succesfull'}", status=201, mimetype='application/json')
    except Exception as e:
        return Response("{'error':'%s'}"%(e),  status=400, mimetype='application/json')




@app.route('/forgot',methods=['POST'])
def forgot():
    return {'message':'Forgot'}

@app.route('/logout',methods=['POST'])
def logout():
    return {'message':'Logout'}

app.run(debug=True)