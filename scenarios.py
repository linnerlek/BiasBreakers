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
                    "1": {
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
                "sub_choices": {
                    "1": {
                        "text": "Invite her to a follow-up discussion after the meeting.",
                        "outcome": "This is the outcome",
                        "pfeedback": "feedback",
                        "challenges": "challenges",
                        "encouragement": "ecouragement",
                        "dialogue": {
                            "user": "I invited her to continue the conversation privately after the meeting.",
                            "her": "I’m open to discussing this further, but I still have my doubts.",
                            "thoughts": "You feel hopeful that a one-on-one conversation might lead to a more nuanced understanding."
                        },
                    },
                    "2": {
                        "text": "Ask the team to share similar experiences.",
                        "dialogue": {
                            "user": "I asked if others had faced similar experiences with bias.",
                            "her": "I hadn’t realized it was such a common issue here.",
                            "thoughts": "You feel validated as more team members begin sharing their experiences."
                        },
                    },
                    "3": {
                        "text": "Propose creating a team initiative to address bias.",
                        "dialogue": {
                            "user": "I proposed creating a team initiative to address bias more systematically.",
                            "her": "That could be interesting, but I’m not sure how it would work.",
                            "thoughts": "You feel encouraged that she’s at least considering the idea."
                        },
                    },
                    "4": {
                        "text": "Acknowledge her perspective while emphasizing the importance of allyship.",
                        "dialogue": {
                            "user": "I acknowledged her experience while stressing the need for us to support each other as allies.",
                            "her":" I see your point, but I still believe my own experiences are valid.",
                            "thoughts": "You feel that recognizing her perspective may make her more open to hearing yours."
                        },
                    }
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

