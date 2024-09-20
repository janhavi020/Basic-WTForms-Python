from flask import Flask, render_template, request
from wtforms import Form, validators, StringField, BooleanField, DateTimeField, SelectField, PasswordField
from wtforms.fields import DateField
from wtforms.widgets import html5 as h5widgets
from wtforms.widgets import TextArea


app = Flask(__name__)

class UserRegistrationForm(Form):
    uName = StringField("Name:", validators=[validators.InputRequired(), validators.Length(min=4, max=10)])
    uGender = SelectField("Gender: ", validators=[validators.InputRequired()], choices=[(1,"Male"),(2,"Female"),(3,"Other")])
    uPass = PasswordField("Password:", validators=[validators.InputRequired(), validators.Length(min=4, max=10)])
    uEmail = StringField("Email", validators=[validators.InputRequired()])
    isGetEmails = BooleanField("Get promotional Emails:", default=False)
    uDob = DateTimeField("Date of Birth:", validators=[validators.Optional()], format='%Y-%m-%d')
    uPhone = StringField('Phone', validators=[validators.InputRequired(),validators.Length(min=10, max=15),validators.Regexp(r'^\+?\d{10,15}$', message="Enter a valid phone number")])

@app.route("/", methods=["GET","POST"])
def index():
    form = UserRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        if not form.uName.data[0].isalpha():
            form.uName.errors.append("Username should start with an alphabet!!")
        print(form.uName.data)
        print(form.uDob.data)
        print(form.uPhone.data)
    return render_template("home.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)