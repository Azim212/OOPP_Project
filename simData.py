from wtforms import SubmitField, StringField, SelectField, Form, validators


class simData(Form):
    led = StringField('LED', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired(), validators.Length(max=2)], default=0)
    cfl = StringField('CFL', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired(), validators.Length(max=2)], default=0)
    inc = StringField('Incandescent', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired(), validators.Length(max=2)], default=0)
    toish = StringField('How many toilets do you have?', [validators.Regexp(regex="^\d+$", message='Please enter a number'), validators.DataRequired(), validators.Length(max=2)], default=1)
    toitype = SelectField('What type of toilets do you use?', choices=[('Old', 'Old'), ('Conventional ', 'Conventional '), ('High Efficiency', 'High Efficiency')])
    submit = SubmitField('Submit')
