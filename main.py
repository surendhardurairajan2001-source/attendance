from flask import Flask,render_template,request,url_for,session,redirect
import sqlite3
import os
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException 
import zipfile
from zipfile import BadZipfile 
from datetime  import datetime


app =Flask(__name__)
app.secret_key ='Surendhar@123'
base_dir = os.path.dirname(os.path.abspath(__file__))
DB_path = os.path.join(base_dir, "db_path")

def check_user(username,password):                              
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?",(username,password))
    user = cursor.fetchone()
    conn.close()
    return user


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])

def login():
    username = request.form['username']
    password =request.form['password']

    if check_user(username,password):
        session['username'] = username

        return redirect(url_for('attedance'))
    else:
        return "<h2> invalid username and password </h2>"
@app.route('/attedance',methods=['GET','POST'])  
def attedance():
    if request.method == 'POST':
        start_time = request.form['Start Time']
        End_time =request.form['End Time']
        date = datetime.now().strftime("%Y-%m-%d")

        file_path ='attendance.xlsx'
        try:
            if os.path.exists(file_path):
                 wb = openpyxl.load_workbook(file_path)
                 ws= wb.active
            else:
                 raise FileNotFoundError
        except(FileNotFoundError,InvalidFileException,zipfile.BadZipFile):
            wb = openpyxl.Workbook()
            ws=wb.active
            ws.tittle = 'Attedance'
            ws.append(["Username","Start Time","End Time","Date"])
        username = session.get('username','Guest')
        ws.append([username,start_time,End_time,date])
        wb.save(file_path)
        return render_template('attedance.html',username=username,start=start_time,end=End_time,date=date)
    else:
        username = session.get('username','Guest')
        return render_template('attedance.html',username=username)
              
   


if __name__ =='__main__':
    app.run(debug=True)


