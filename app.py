# All code written by Linn Klofta
# 2024

from flask import Flask, render_template, request, session, redirect
from scenarios import scenarios

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/scenario')
def scenario():
    return render_template('scenario.html')


@app.route('/new_game')
def new_game():
    # Clear session data for a new game
    session.pop('dialogue_history', None)
    session.pop('main_choice', None)
    session.pop('statistics', None)  # Clear statistics
    session.pop('user_choices', None)  # Clear user choices
    return redirect('/game/1')


@app.route('/game/<int:scenario_id>', methods=['GET', 'POST'])
def game(scenario_id):
    if scenario_id not in scenarios:
        return "Scenario not found", 404

    scenario = scenarios[scenario_id]
    sub_choices = None
    game_ended = False

    if 'dialogue_history' not in session:
        session['dialogue_history'] = []

    if 'statistics' not in session:
        session['statistics'] = {
            "outcome": None, "feedback": None, "challenges": None, "encouragement": None}

    if 'user_choices' not in session:
        session['user_choices'] = []

    if request.method == 'POST':
        if 'choice' in request.form:
            user_choice_key = request.form['choice']
            # Fetch the choice text
            user_choice_text = scenario["choices"][user_choice_key]
            main_dialogue = scenario["outcomes"][user_choice_key]["dialogue"]

            if main_dialogue['user'] or main_dialogue['her'] or main_dialogue['thoughts']:
                session['dialogue_history'].append({
                    "user_message": f" {main_dialogue['user']}" if main_dialogue['user'] else "",
                    "her_response": f" {main_dialogue['her']}" if main_dialogue['her'] else "",
                    "thoughts": f"<i>{main_dialogue['thoughts']}</i>" if main_dialogue['thoughts'] else ""
                })

            session['main_choice'] = user_choice_key
            session['user_choices'].append(
                f"{user_choice_text}")  # Log main choice text
            sub_choices = scenario["outcomes"][user_choice_key]["sub_choices"]

        elif 'sub_choice' in request.form:
            main_choice = session.get('main_choice')
            sub_choice_key = request.form['sub_choice']
            # Fetch the sub-choice text
            sub_choice_text = scenario["outcomes"][main_choice]["sub_choices"][sub_choice_key]["text"]

            sub_data = scenario["outcomes"][main_choice]["sub_choices"][sub_choice_key]
            sub_dialogue = sub_data["dialogue"]

            if sub_dialogue['user'] or sub_dialogue['her'] or sub_dialogue['thoughts']:
                session['dialogue_history'].append({
                    "user_message": f" {sub_dialogue['user']}" if sub_dialogue['user'] else "",
                    "her_response": f" {sub_dialogue['her']}" if sub_dialogue['her'] else "",
                    "thoughts": f"<i>{sub_dialogue['thoughts']}</i>" if sub_dialogue['thoughts'] else ""
                })

            session['user_choices'].append(
                f"{sub_choice_text}")  # Log sub-choice text

            # Update statistics with additional information
            if sub_data.get('outcome'):
                session['statistics']['outcome'] = sub_data['outcome']
            if sub_data.get('pfeedback'):
                session['statistics']['feedback'] = sub_data['pfeedback']
            if sub_data.get('challenges'):
                session['statistics']['challenges'] = sub_data['challenges']
            if sub_data.get('encouragement'):
                session['statistics']['encouragement'] = sub_data['encouragement']

            game_ended = True

    return render_template(
        'game.html',
        scenario=scenario,
        dialogue_history=session['dialogue_history'],
        statistics=session['statistics'],  # Pass statistics to the template
        # Pass user choices to the template
        user_choices=session['user_choices'],
        sub_choices=sub_choices if 'sub_choices' in locals() else None,
        game_ended=game_ended
    )



if __name__ == '__main__':
    app.run(debug=True)
