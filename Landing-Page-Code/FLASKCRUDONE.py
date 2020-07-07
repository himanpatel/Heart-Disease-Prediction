from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../2098_health')
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskcruddb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    height = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    ap_high = db.Column(db.String(100))
    ap_low = db.Column(db.String(100))
    cholesterol = db.Column(db.String(100))
    glucose = db.Column(db.String(100))
    smoke = db.Column(db.String(100))
    alcohol = db.Column(db.String(100))
    physical_activity = db.Column(db.String(100))
    cardio_disease = db.Column(db.String(100))



    def __init__(self, age, gender,height,weight,ap_high,ap_low,cholesterol,glucose,smoke,alcohol,physical_activity,cardio_disease ):
        self.age= age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.ap_high = ap_high
        self.ap_low = ap_low
        self.cholesterol = cholesterol
        self.glucose = glucose
        self.smoke = smoke
        self.alcohol = alcohol
        self.physical_activity = physical_activity
        self.cardio_disease = cardio_disease



# This is the index route where we are going to
# query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("first.html", employees=all_data)


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':

        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight= request.form['weight']
        ap_high = request.form['AP_high']
        ap_low = request.form['Ap_low']
        cholesterol = request.form['cholesterol']
        glucose = request.form['glucose']
        smoke = request.form['smoke']
        alcohol = request.form['alcohol']
        physical_activity = request.form['physical_activity']
        cardio_disease = request.form['cardiodisease']


        my_data = Data(age, gender,height, weight,ap_high,ap_low,cholesterol,glucose,smoke,alcohol,physical_activity,cardio_disease)
        db.session.add(my_data)
        db.session.commit()

        flash("Patient Inserted Successfully")

        return redirect(url_for('Index'))


# this is our update route where we are going to update our employee
@app.route('/update', methods=[ 'POST'])
def update():
    #my_data = Data.query.get_or_404(id)
    #my_data = Data.query.get(id)
    my_data = Data.query.get(request.form.get('id'))
    if request.method == 'POST':
        #
        #print("data is ",my_data)


        my_data.age = request.form['age']
        my_data.gender = request.form['gender']
        my_data.height = request.form['height']
        my_data.weight = request.form['weight']
        my_data.ap_high = request.form['aphigh']
        my_data.ap_low = request.form['aplo']
        my_data.cholesterol = request.form['cholesterol']
        my_data.glucose = request.form['glucose']
        my_data.smoke = request.form['smoke']
        my_data.alcohol = request.form['alcohol']
        my_data.physical_activity = request.form['physicalactive']
        my_data.cardio_disease = request.form['cardiodisease']

        #my_data = Data(AGE, GENDER, HEIGHT, WEIGHT, AP_HIGH, AP_LOW, CHOLESTEROL, GLUCOSE, SMOKE, ALCOHOL,
                     #  PHYSICAL_ACTIVIY, CARDIO_DISEASE)
        #db.session.add(my_data)

        db.session.commit()
        flash("Patient Updated Successfully")

        return redirect(url_for('Index'))


# This route is for deleting our employee
@app.route('/delete/<id>/',methods = ['GET','POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Patient Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True,port=8053)