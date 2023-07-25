from flask import Flask, request, render_template, send_file
import random

app = Flask(__name__)

@app.route('/')
def booking():
    return render_template('index.html')

@app.route('/bil',methods = ['GET','POST'])
def bil():
    if request.method == 'POST':
        movie = request.form.get('movie')
        number = int(request.form.get('number'))
        show_time = request.form.get('movie_time')
        bil_verification_id = random.randint(150, 500)
        seats = random.randint(150,500);sets_are = ''
        for i in range(seats ,seats + number):
            sets_are = sets_are +' '+ str(i)

        rate = rates(movie)
        file_path = 'bil.txt'
        bil = amount(number,rate)
        bil_content = f'\n--------------------------------------------------------------------------------------------------------------------\n                                           ABC Restaurant\n                                        Tirupur, Tamil Nadu\n                                       GSTIN: PK78ASIN6H78WQ1\n Phone Number: 9300230011                                           Inovice Number: TN0067Q9\n E-Mail: ABCcenima@gmail.com                                        Your Ticket verification id : {bil_verification_id}\n Your Seat number are : '+ sets_are +'                                Show Time : '+ show_time +f'\n--------------------------------------------------------------------------------------------------------------------\n\n\n\n    Movie                  Qty                     Rate                   Sub total\n\n    {movie}                  {number}                     {rate}                   {bil}\n--------------------------------------------------------------------------------------------------------------------\n\n\n                                                                            Total Qty  : {number}\n                                                                            Sub Total  : {bil}\n                                                                            CGST   IN  : {0}\n                                                                            SGST   IN  : {0}\n                                                                            GRAND TOTAL: {bil}\n--------------------------------------------------------------------------------------------------------------------\n     WARINING DONOT CHANGE ANYTHING IN THE BILL IF YOU CHANGED ANYTHING BILL BECOME INVALID'


        write_bil(bil_content, file_path)

        return send_file(file_path, as_attachment=True)

def amount(number, rate):
    return rate*number
    
def rates(movie):
    if movie == 'Sardar':
        return 150
    elif movie == 'Varisu':
        return 180
    elif movie == 'Vikram':
        return 220
    else:
        return 160

def write_bil(content,file_path):
    with open(file_path, 'w') as f:
        f.write(content)

if __name__=='__main__':
    app.run(debug=True)