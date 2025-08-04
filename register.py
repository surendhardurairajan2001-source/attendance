import flask
from flask import request,redirect,render_template
import sqlite3
import os
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException
import zipfile 

app=flask(__name__)

@app.route('/register',methods=['GET','POST'])

def register():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'user.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO user(username,password) VALUES(?,?)",(username,password))
            conn.commit
        except sqlite3.IntegrityError:
            return "User name Already exits"
        finally:
            conn.close()
        return f"user'{username}'registered successfully!"

    return render_template('register.html')

if __name__ =='__main__':
    app.run(debug=True)

 

