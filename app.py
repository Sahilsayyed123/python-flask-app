from flask import Flask, render_template, request
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))


def calculate_age_in_days(birthdate):
    # Convert the birthdate string to a datetime object
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference between the current date and the birthdate
    age_in_days = (current_date - birthdate).days

    return age_in_days


# Example usage


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        fn=request.form["first"]
        ln=request.form["last"]
        age = request.form["age"]
        gender = request.form["gender"]
        height = request.form["height"]
        weight = request.form["weight"]
        ap_hi = request.form["ap_hi"]
        ap_lo = request.form["ap_lo"]
        cholesterol = request.form["cholesterol"]
        glucose = request.form["glucose"]
        active = request.form["active"]
        height = float(height)
        weight = float(weight)
        ap_hi = float(ap_hi)
        ap_lo = float(ap_lo)
        # cholesterol = int(cholesterol)
        # glucose = int(glucose)
        # active = int(active)
        age=calculate_age_in_days(age)
#----------------------------------------------------------------------------------------------------------#           
        cholesterol=int(cholesterol)
        glucose=int(glucose)

#----------------------------------------------------------------------------------------------------------#           
  
#----------------------------------------------------------------------------------------------------------#           

        if(active=="yes"):
            active=1
        else:
            active=0    
#----------------------------------------------------------------------------------------------------------#             
        if(gender=="male"):
            gender=1
        else:
            gender=0
#----------------------------------------------------------------------------------------------------------#            

        # return [{"age":age,"glucose":glucose,"active":active,"gender":gender,"height":height,"weight":weight,"ap_lo":ap_lo,"ap_hi":ap_hi,"cholesterol":cholesterol}]
        
        
      	
        prediction = model.predict(
            [[age, gender, height, weight, ap_hi, ap_lo, cholesterol, glucose, active]])
        if (prediction[0] == 1):
            return "<h1>"+fn+" "+ln+" has a high possibility of cardiovascular disease<h1>"
        else:
            return "<h1>"+fn+" "+ln+" does not have cardiovascular disease<h1>"


# @app.route("/<usr>")
# def user(usr):
#     return f"<h2>{usr}</h2>"


if __name__ == '__main__':
    app.run(debug=True)
