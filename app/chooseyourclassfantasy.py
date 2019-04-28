#choose your class through real life actions. Fantasy edition
from flask import Flask, render_template, redirect, url_for,request, session
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, validators, RadioField
from wtforms.validators import DataRequired




app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
combat = 0
magic = 0
stealth = 0


class Question1Form(Form):
        combat = 0
        question1 = RadioField('You walk into a bar and noticed the barkeep is being harrassed by some thugs from out of town. Things are getting a bit intense and the patrons of the bar are getting anxious. What do you do?', 
                                 choices=[('Q1C1', 'Start a fight with the thugs'),
                                 ('Q1C2', 'Wait for the thugs to leave'), ('Q1C3', 'Calmly get the thugs to leave with no violence'), ('Q1C4', 'Start stealing valuable items while the barkeep is distracted')])
        question2 = RadioField(
            'You are working in an old mine chipping away at the rock when you notice a lockbox hidden beneath the rubble. What do you do?',
            choices=[('Q2C1', 'Use your trusty pick lock to get it open'), ('Q2C2', 'Throw the box on the ground and keep stomping on it till it opens'), (
                'Q2C3', 'Pray that you are blessed with the ability to open this box.'), ('Q2C4', 'Look for a key nearby or examine the box thoroughly to find other ways to open it.')])
        question3 = RadioField(
            'If you were transformed by a wizard into the animal of your choice below what might that be?',
            choices=[('Q3C1', 'Snake'), ('Q2C2', 'Grizzly Bear'), (
                'Q3C3', 'Horse'), ('Q2C4', 'Octopus')])
        question4 = RadioField(
            'A man claiming to be a God has appeared in court, he murdered his brother stating Its what I willed.. You are the judge of the court what do you decide to do with the man?',
            choices=[('Q4C1', 'sentence him to death. You think no God would allow himself to be killed'), ('Q4C2', 'Bring in a jury and allow the man to explain why he claims to be god and why his actions were just'), (
                'Q4C3', 'Speak to him privately and persuade him into giving all his money up for his freedom'), ('Q4C4', 'Release the man and ask to join him and be apart of his vision of the world')])
        question5 = RadioField(
            'Upon arriving in a far away town for the first time. As you walk through the town the citizens yell at you to leave and go back to where you are from and other hostile comments. What do you do?',
            choices=[('Q5C1', 'Slaughter the whole village'), ('Q5C2', 'Keep your head down and do the business you needed to do in town'), (
                'Q5C3', 'Leave the town immediately'), ('Q5C54', 'Find the leader of the town and kill him later in the night to send a message')])
        submit = SubmitField('Submit Answers')




@app.route('/', methods=['GET', 'POST'])
def first_slide():
        return render_template('home.html')

@app.route('/Question1.html', methods=['GET','POST'])
def Question_1():
        combat = 0
        magic = 0
        stealth = 0
        form = Question1Form()
        if form.is_submitted():
                session['question1'] = form.question1.data
                session['question2'] = form.question2.data
                session['question3'] = form.question3.data
                session['question4'] = form.question4.data
                session['question5'] = form.question5.data
                if form.question1.data == "Q1C1":
                        combat += 1
                return redirect(url_for('results'))
        return render_template('Question1.html', form=form, combat=combat, magic=magic, stealth=stealth)
                        
                

@app.route('/results.html')  
def results():
        return render_template('results.html',combat=combat, magic=magic, stealth=stealth)              

        
        
if __name__ == "__main__":
        app.run(debug=True)
