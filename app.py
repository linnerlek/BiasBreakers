from flask import Flask, render_template, request, session

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


# Sample scenario data
scenarios = {
    1: {
        "description": "At a team meeting, a female colleague dismisses concerns about gender bias after another woman shares her experience of being interrupted by male colleagues. Your colleague makes comments like, 'I’ve never faced discrimination, so I don’t think it’s that big of a deal.' She frequently aligns herself with male colleagues, often downplaying workplace inequalities. You believe her behavior reflects internalized sexism and is counterproductive to gender equality.",
        "choices": {
            "A": "Speak to her privately and try to educate her about the importance of being an ally",
            "B": "Publicly challenge her comments during the meeting",
            "C": "Avoid the conversation altogether and hope her behavior improves",
            "D": "Seek advice from a female mentor or trusted colleague on how to handle the situation"
        },
        "outcomes": {
            "A": {
                "description": "You spoke to her privately.",
                "dialogue": {
                    "user": "I understand you may not have faced discrimination, but it’s important to realize that others experience things differently. When we dismiss these concerns, it weakens our ability to support each other as women.",
                    "her": "I’m just saying I’ve never needed special treatment, so why should anyone else? We all deal with challenges.",
                    "thoughts": "You feel frustrated but also hopeful that you’ve planted a seed for her to reflect on. You handled the situation respectfully, but you wonder if it will truly make her reconsider."
                },
                "sub_choices": {
                    "1":{
                        "text": "Ask others for their opinions.",
                        "outcome": "This is the outcome",
                        "pfeedback": "feedback",
                        "challenges": "challenges",
                        "encouragement": "ecouragement",
                        "dialogue": {
                            "user": "I decided to ask others...",
                            "her": "Her response was surprising...",
                            "thoughts": "You feel more confident now that others are involved."
                        },
                    },
                    "2": {
                        "text": "Provide data on gender bias.",
                        "dialogue": {
                            "user": "I shared some research with her.",
                            "her": "She seemed taken aback by the numbers.",
                            "thoughts": "You think you may have reached her logically."
                        },
                    },
                    "3": {
                        "text": "Suggest a team workshop on gender issues.",
                        "dialogue": {
                            "user": "Team workshop",
                            "her": "Team workshop",
                            "thoughts": "team workshop."
                        },
                    },
                    "4": {
                        "text": "Follow up with her afterward.",
                        "dialogue": {
                            "user": "follow up",
                            "her": "follow up",
                            "thoughts": "follow up"
                        },
                    }
                }
            },
            "B": {
                "dialogue": {
                    "user": "I can't let this slide. It’s important we address bias openly.",
                    "her": "But isn't it just a discussion? People are allowed to have different opinions.",
                    "thoughts": "You realize that challenging her may create tension, but it's necessary to foster a more equitable environment."
                }
            },
            "C": {
                "dialogue": {
                    "user": "I decided to stay quiet, hoping the issue will resolve on its own.",
                    "her": "Testing",
                    "thoughts": "However, you can’t shake the feeling that you missed an opportunity to challenge a harmful mindset."
                }
            },
            "D": {
                "dialogue": {
                    "user": "I spoke with my mentor for guidance on how to handle this.",
                    "thoughts": "She reassured you, but you still feel anxious about the upcoming conversation."
                }
            }
        },
        "sub_choices": {
            "A": {
                "description": "You spoke to her privately.",
                "sub_choices": {
                    "1": "Ask her to share her experiences.",
                    "2": "Suggest resources for understanding bias.",
                    "3": "Invite her to a women's group meeting.",
                    "4": "Encourage her to reflect on her stance."
                }
            },
            "B": {
                "description": "You publicly challenged her comments.",
                "sub_choices": {
                    "1": "Ask others for their opinions.",
                    "2": "Provide data on gender bias.",
                    "3": "Suggest a team workshop on gender issues.",
                    "4": "Follow up with her afterward."
                }
            },
            "C": {
                "description": "You avoided the conversation altogether.",
                "sub_choices": {
                    "1": "Reflect on why you chose silence.",
                    "2": "Consider talking to a colleague about it.",
                    "3": "Think about how to address it later.",
                    "4": "Accept that sometimes silence is okay."
                }
            },
            "D": {
                "description": "You sought advice from a mentor.",
                "sub_choices": {
                    "1": "Discuss your feelings about the situation.",
                    "2": "Ask for tips on approaching her.",
                    "3": "Get insights on allyship.",
                    "4": "Explore other mentor resources."
                }
            }
        }
    },
    # You can define more scenarios here
}


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

            # Add main choice dialogue to session history
            session['dialogue_history'].append({
                "user_message": main_dialogue["user"],
                "her_response": main_dialogue["her"],
                "thoughts": main_dialogue["thoughts"]
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

            # Append sub-choice dialogue to history
            session['dialogue_history'].append({
                "user_message": sub_dialogue["user"],
                "her_response": sub_dialogue["her"],
                "thoughts": sub_dialogue["thoughts"]
            })

            session['dialogue_history'].append({
                "user_message": f"<strong>Outcome:</strong> {sub_data['outcome']}",
                "her_response": f"<strong>Feedback:</strong> {sub_data['pfeedback']}",
                "thoughts": f"<strong>Challenges:</strong> {sub_data['challenges']}",
                "additional": f"<strong>Encouragement:</strong> {sub_data['encouragement']}"
            })

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
