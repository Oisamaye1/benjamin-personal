from app import app
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
import smtplib
from email.message import EmailMessage

Education = [
  {
    "year": "2020 - 2021",
    "school": "African Regional Center for Space Science and Technology Education - English",
    "location": "Obafemi Awolowo University Campus Ile-Ife Nigeria",
    "degree": "Postgraduate Diploma in Remote Sensing and GIS"
  },
  {
    "year": "2019 - 2019",
    "school": "Environmental Safety Management Institute",
    "location": "Minna Niger State, Nigeria",
    "degree": "Professional Diploma in HSE 1,2 & 3"
  },
  {
    "year": "2016 - 2018",
    "school": "Federal Polytechnic",
    "location": "Auchi Edo State, Nigeria",
    "degree": "Higher National Diploma in Electrical Electronics Engineering"
  },
  {
    "year": "2013 - 2015",
    "school": "Federal Polytechnic",
    "location": "Auchi Edo State, Nigeria",
    "degree": "National Diploma in Electrical Electronics Engineering"
  },
  {
    "year": "2007 - 2013",
    "school": "Longevity Secondary School",
    "location": "Ajaokuta Kogi State, Nigeria",
    "degree": "Secondary School Certificate Examination (SSCE)"
  },
  {
    "year": "2001 - 2007",
    "school": "St Peter's Nursery/Primary School",
    "location": "Ajaokuta Kogi State, Nigeria",
    "degree": "First School Leaving Certificate"
  },
]

Experience = [
  {
    "year": "2021 - 2021",
    "role": "Computer Hardware Technician",
    "company": "WII Technologies",
    "location": "Akure Ondo State, Nigeria"
  },
  {
    "year": "2019 - 2020",
    "role": "National Youth Service Corps",
    "company": "Idris Legbo Science College",
    "location": "Kutigi Niger State, Nigeria"
  },
  {
    "year": "2016 - 2016",
    "role": "Industrial Trainee",
    "Company": "Geregu Power Plc.",
    "location": "Ajaokuta Kogi State, Nigeria"
  },
  {
    "year": "2014 - 2015",
    "role": "Student Industrial Work Experience Scheme (SIWES), Trainee",
    "Company": "Transmission Company of Nigeria",
    "location": "Ajaokuta Kogi State, Nigeria"
  }
]

Projects = [
  {
    "completion": "January 5th, 2023",
    "name": "Exercise App",
    "image": "Exercise App",
    "description": "The exercise app randomly suggests exercises for available list of exercise and also gives description about the exercise.",
    "link": "#"
  },

]

class Contactform(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    email = EmailField('Email Address', validators=[DataRequired(), Email(), Length(max=30)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def index():
  form = Contactform()
  education = Education
  experience = Experience

  name = form.name.data
  email = form.email.data
  message = form.message.data

  print(name, email, message)

  if request.method == 'POST' and form.validate():
     email_alert("New Message from contact form", 
     f"Message from {name} with email address {email}, \n {message}", 
     "Ovibenz@gmail.com")
     return redirect(url_for("index"))


  return render_template("index.html", form = form,
  education=education,
  experience=experience, 
  current_time = datetime.utcnow())


def email_alert(subject, body, to):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to

    userEmail = "oisamayebenjamin@gmail.com"
    message['from'] = userEmail
    password = ""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(userEmail, password)
    server.send_message(message)
    server.quit()
