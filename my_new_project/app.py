from flask import Flask, render_template, request , redirect, url_for , session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "Gowtham@123"

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "Gowtham@123",
    database = "my"
)

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/managerLogin.html')
def managment():
    return render_template('managerLogin.html')


@app.route('/manager.html/selectplayers.html')
def selectplayers():
    cursor = db.cursor()
    query11 = f'SELECT * FROM PLAYERS'#intha eadethel manager choose pangra player tha varanum
    cursor.execute(query11)#iapothiku ellathium fletch pandikuram
    row = cursor.fetchall()

    return render_template('selectplayers.html',row = row)

@app.route('/manager.html/<string:id>',methods = ['GET','POST'])
def manager(id):
    team = session.get('team')
    table = session.get('table')
    cursor = db.cursor()

    query11 = f'SELECT * FROM PLAYERS WHERE ID = {id};'#intha eadethel manager choose pangra player tha varanum
    cursor.execute(query11)#iapothiku ellathium fletch pandikuram
    row = cursor.fetchall()

    query12 = f'SELECT BUDGET FROM {table} WHERE teamName = "{team}";'
    cursor.execute(query12)
    balance = cursor.fetchone();amount = row[0][-1]
    if request.method == 'POST':
        if request.form.get('sold'):
            if team is None:
                return redirect(url_for('selectplayers'))
            query14 = f"UPDATE A1 SET {team[0]} = {id} WHERE NUMBERS = {id}"
            cursor.execute(query14)
            db.commit()

            return redirect(url_for('selectplayers'))
        
    return render_template('manager.html',row = row, team = team, amount = amount)

@app.route('/tabel.html', methods = ['GET', 'POST'])
def table():
    team = session.get('team')
    table = session.get('table')
    cursor = db.cursor()

    query11 = f'SELECT * FROM PLAYERS'#intha eadethel manager choose pangra player tha varanum
    cursor.execute(query11)#iapothiku ellathium fletch pandikuram
    row = cursor.fetchall()

    query12 = f'SELECT BUDGET FROM {table} WHERE teamName = "{team}";'
    cursor.execute(query12)
    balance = cursor.fetchone();amount = row[0][-1]
    if request.method == 'POST':
        amount = amount + int(request.form.get('bit'))


    return render_template('tabel.html',row = row, team = team, amount = amount)

@app.route('/game.html',methods = ['GET', 'POST'])
def game():
    table = session.get('table')
    count = session.get('count')
    cursor = db.cursor();row = []
    for i in range(1,count[0] - 1 ):
        quert9 = f"SELECT teamName FROM {table} WHERE NUMBERS = {i}"
        cursor.execute(quert9)
        team_name = cursor.fetchone()
        row.append(team_name)
    r = []
    if request.method == 'POST':
        password = session.get('password')
        if request.form.get('team') == 'manager' and request.form.get('pass') == password[0]:
            return redirect(url_for('selectplayers'))

        r.append(request.form.get('team'))
        quert10 = f'SELECT PASS FROM {table} WHERE teamName = "{request.form.get("team")}"'
        cursor.execute(quert10)
        t = cursor.fetchone()
        for i in range(0, len(row)):
            if(r[0] in row[i][0]) and (request.form.get('pass') == t[0]):
                session['team'] = t
                return redirect(url_for('table'))
    
    return render_template('game.html',row = row)

@app.route('/contest.html',methods = ['GET','POST'])
def contest():
    if request.method == 'POST':
        cursor = db.cursor();table = request.form.get('id')
        query4 = f'SHOW TABLES LIKE "{table}"'
        cursor.execute(query4)
        result = cursor.fetchone()

        if result:
            query5 = f'SELECT COUNT(*) FROM information_schema.columns WHERE table_name = "{table}"'
            cursor.execute(query5)
            count = cursor.fetchone()
            query6 = f'SELECT PASS FROM {table} WHERE NUMBERS = {count[0] - 3};'
            cursor.execute(query6)
            password = cursor.fetchone()
            if request.form.get('pass') == password[0]:
                session['table'] = table
                session['count'] = count
                session['password'] = password
                query16 = f'UPDATE {table} SET soldPlayers = 0 WHERE NUMBERS = {count[0] - 3};'
                cursor.execute(query16)
                db.commit()
                return redirect(url_for('game'))
            else:
                return redirect(url_for('contest'))
            


    return render_template('contest.html')

@app.route('/teams.html',methods = ["GET","POST"])
def teams():
    if request.method == 'POST':
        if (request.form.get('gamePassword') != request.form.get('conformGamepassword')) or (request.form.get('managerPassword') != request.form.get('comformManagerpassword')):
            return redirect(url_for('teams'))
        d = int(request.form.get('budget'))
        if d > 100:
            #innum budget innu oru coloum open pand atakull 
            #ellam teams uadiya babget and balence amount podanum

            return redirect(url_for('teams'))

        cursor = db.cursor()
        a = '';b = '';c = ''
        n = int(request.form.get('no'))
        for i in range(0, n+1):
            x = request.form.get('team'+str(i))
            y = request.form.get('teampass'+str(i))
            if x and y is not None:
                a = a + x + ' INT,'
                b = b +',CONSTRAINT FK_PLAYERS_'+ x +'  FOREIGN KEY('+ x +')  REFERENCES PLAYERS(id)'
                c = c + "('"+ y +"'),"
                query = 'CREATE TABLE A1(NUMBERS INT AUTO_INCREMENT PRIMARY KEY , '+ a +' PASS VARCHAR(50), BUDGET INT, teamName VARCHAR(50), soldPlayers int'+ b +');'
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            return redirect(url_for("teams"))
        
        query1 = "INSERT INTO A1 (PASS) VALUES"+ c[:-1] +";"
        cursor.execute(query1)

        query2 = "INSERT INTO A1 (PASS) VALUES ('"+ request.form.get('gamePassword')+ "'),('"+ request.form.get('managerPassword') + "');"
        cursor.execute(query2)

        for i in range(0,n):
            query3 = "UPDATE A1 SET BUDGET = "+ str(d) +";"
            cursor.execute(query3)
            x = request.form.get('team'+str(i))
            query8 = f"UPDATE A1 SET teamName = '{x}' WHERE NUMBERS = {i+1}"
            cursor.execute(query8)
            db.commit()
        return redirect(url_for('login'))

    return render_template('teams.html')



if __name__=='__main__':
    app.run(debug=True)