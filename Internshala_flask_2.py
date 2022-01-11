# internshala
# import the flask class
from flask import Flask, session, render_template, request,make_response,redirect,flash
from flask_mysqldb import MySQL
from flask import g

# instatiating flask class 
app = Flask(__name__)

# configuring MySQL for the web application
app.config['MYSQL_USER'] = 'root'    # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_PASSWORD'] = '' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DB'] = 'flask'  # Database name to be replaced with appropriate database name
app.config['MYSQL_HOST'] = 'localhost' # default database host of MySQL to be replaced with appropriate database host

#initialise mySQL
mysql = MySQL(app)

#CHOOSE Skills:
@app.route('/chooseskills')
def choosebrand():
    return render_template('chooseskills.html')

# Search Internship (also displays feature matching results):
@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    #displays dropdown info inputted by user
    selected_Skills_required =  "%" + request.form['Skills_required'] + "%"
    selected_Duration_in_months = request.form['Duration_in_months']
    selected_Location = request.form['Location']

    cursor = mysql.connection.cursor()

    if selected_Skills_required != '%SELECT%' and selected_Duration_in_months=='SELECT' and selected_Location == 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Skills_required_1 like %s"
        args = (selected_Skills_required,)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required != '%SELECT%' and selected_Duration_in_months!='SELECT' and selected_Location == 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Skills_required_1 like %s AND Duration_in_months like %s"
        args = (selected_Skills_required,selected_Duration_in_months)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required != '%SELECT%' and selected_Duration_in_months=='SELECT' and selected_Location != 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Skills_required_1 like %s AND Location_1 like %s"
        args = (selected_Skills_required,selected_Location)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required != '%SELECT%' and selected_Duration_in_months!='SELECT' and selected_Location != 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Skills_required_1 like %s AND Duration_in_months like %s AND Location_1 like %s"
        args = (selected_Skills_required,selected_Duration_in_months,selected_Location)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required == '%SELECT%' and selected_Duration_in_months !='SELECT' and selected_Location == 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Duration_in_months like %s"
        args = (selected_Duration_in_months,)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required == '%SELECT%' and selected_Duration_in_months !='SELECT' and selected_Location != 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Duration_in_months like %s AND Location_1 like %s"
        args = (selected_Duration_in_months,selected_Location)
        cursor.execute(query,args)
        rows = cursor.fetchall()
    elif selected_Skills_required == '%SELECT%' and selected_Duration_in_months =='SELECT' and selected_Location != 'SELECT':
        query = "SELECT DISTINCT Internship_title,Company,Location,Duration_in_months,Stipend_per_month,Skills_required FROM internshala3 WHERE Location_1 like %s"
        args = (selected_Location,)
        cursor.execute(query,args)
        rows = cursor.fetchall()

    #print(rows)
    #print(selected_Skills_required)
    #print(selected_Duration_in_months)
    #print(selected_Location)
    #cursor.close()
    #con.close()

    return render_template('searchresult1.html', rows=rows)

if __name__ == '__main__':
    app.run(host='localhost', port=5000,debug = True)
