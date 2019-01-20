from wtforms import SubmitField, StringField, SelectField, Form, validators


class simData(Form):
    led = StringField('LED', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired()], default=0)
    cfl = StringField('CFL', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired()], default=0)
    inc = StringField('Incandescent', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired()], default=0)
    toish = StringField('How many toilets do you have?', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired()], default=1)
    toitype = SelectField('What type of toilets do you use?', choices=[('Old', 'Old'), ('Ultra Low Flush', 'Ultra Low Flush'), ('High Efficiency', 'High Efficiency'), ('Dual Flush', 'Dual Flush')])
    submit = SubmitField('Submit')
