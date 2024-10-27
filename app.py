# All code written by Linn Klofta
# 2024

from flask import Flask, render_template, request, session, redirect
from scenarios import scenarios

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/scenario')
def scenario():
    return render_template('scenario.html')


@app.route('/new_game')
def new_game():
    # Clear the dialogue history from the session
    session.pop('dialogue_history', None)
    session.pop('main_choice', None)
    # Redirect to the scenario selection or the initial game page
    return redirect('/scenario')

@app.route('/game/<int:scenario_id>', methods=['GET', 'POST'])
def game(scenario_id):
    if scenario_id not in scenarios:
        return "Scenario not found", 404

    scenario = scenarios[scenario_id]
    sub_choices = None
    game_ended = False

    if 'dialogue_history' not in session:
        session['dialogue_history'] = []

    if request.method == 'POST':
        if 'choice' in request.form:
            user_choice = request.form['choice']
            main_dialogue = scenario["outcomes"][user_choice]["dialogue"]

            # Add main choice dialogue to session history only if it's not empty
            if main_dialogue['user'] or main_dialogue['her'] or main_dialogue['thoughts']:
                session['dialogue_history'].append({
                    "user_message": f"You: {main_dialogue['user']}" if main_dialogue['user'] else "",
                    "her_response": f"They say: {main_dialogue['her']}" if main_dialogue['her'] else "",
                    "thoughts": f"You think: {main_dialogue['thoughts']}" if main_dialogue['thoughts'] else ""
                })

            # Store selected main choice in the session
            session['main_choice'] = user_choice
            sub_choices = scenario["outcomes"][user_choice]["sub_choices"]

        elif 'sub_choice' in request.form:
            main_choice = session.get('main_choice')
            sub_choice = request.form['sub_choice']

            # Retrieve dialogue for sub-choice
            sub_data = scenario["outcomes"][main_choice]["sub_choices"][sub_choice]
            sub_dialogue = scenario["outcomes"][main_choice]["sub_choices"][sub_choice]["dialogue"]

            # Append sub-choice dialogue to history only if not empty
            if sub_dialogue['user'] or sub_dialogue['her'] or sub_dialogue['thoughts']:
                session['dialogue_history'].append({
                    "user_message": f"You: {sub_dialogue['user']}" if sub_dialogue['user'] else "",
                    "her_response": f"They say: {sub_dialogue['her']}" if sub_dialogue['her'] else "",
                    "thoughts": f"You think: {sub_dialogue['thoughts']}" if sub_dialogue['thoughts'] else ""
                })

            # Append additional information
            if sub_data.get('outcome'):
                session['dialogue_history'].append(
                    {"additional": f"Outcome: {sub_data['outcome']}"})
            if sub_data.get('pfeedback'):
                session['dialogue_history'].append(
                    {"additional": f"Feedback: {sub_data['pfeedback']}"})
            if sub_data.get('challenges'):
                session['dialogue_history'].append(
                    {"additional": f"Challenges: {sub_data['challenges']}"})
            if sub_data.get('encouragement'):
                session['dialogue_history'].append(
                    {"additional": f"Encouragement: {sub_data['encouragement']}"})

            # Mark game as ended
            game_ended = True


    return render_template(
        'game.html',
        scenario=scenario,
        dialogue_history=session['dialogue_history'],
        sub_choices=sub_choices if 'sub_choices' in locals() else None,
        game_ended=game_ended
    )


if __name__ == '__main__':
    app.run(debug=True)
