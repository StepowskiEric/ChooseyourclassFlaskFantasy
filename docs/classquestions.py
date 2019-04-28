#choose your class through real life actions. Fantasy edition
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

Crusader = 0
Thief = 0
Beserker = 0
Mage = 0


class InfoForm(FlaskForm):
        submit = SubmitField('')


@app.route('/', methods=['GET', 'POST'])
def first_slide():
        return render_template('home.html')


@app.route('/Question1.html', methods=['GET', 'POST'])
def Question_1():
        form = InfoForm()
        if request.method == 'POST':
                if request.form['options', False] == 'option1':
                        Crusader + 1
                        Beserker + 1
                elif request.form['options', False] == 'option2':
                        Mage + 1
                        return redirect(url_for('Question2'))
                elif request.form['options', False] == 'option3':
                        Thief + 1
                elif request.form['options', False] == 'option4':
                        Crusader + 1

        return render_template('Question1.html', form=form, Crusader1=Crusader)


@app.route('/Question2.html')
def Question_2():
        return render_template('Question2.html')


if __name__ == "__main__":
        app.run(debug=True)
