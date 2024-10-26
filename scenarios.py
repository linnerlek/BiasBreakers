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
                        "outcome": "Others agreed with your concerns and shared similar experiences, making the colleague more thoughtful.",
                        "pfeedback": "Positive feedback from others reinforced your perspective.",
                        "challenges": "Some colleagues were hesitant to speak up, delaying the conversation.",
                        "encouragement": "Your calm approach encouraged others to open up and support the conversation.",
                        "dialogue": {
                            "user": "I decided to ask others for their perspectives during a team meeting.",
                            "her": "I wasn’t expecting everyone to have similar experiences.",
                            "thoughts": "You feel more confident now that others are involved."
                        }
                    },
                    "2": {
                        "text": "Provide data on gender bias.",
                        "outcome": "Your colleague seemed taken aback by the data and started reconsidering her views.",
                        "pfeedback": "The data was well-received and helped shift the focus to facts.",
                        "challenges": "She still questioned whether the statistics applied to your specific workplace.",
                        "encouragement": "Presenting objective information empowered you to address the issue logically.",
                        "dialogue": {
                            "user": "I shared some research with her, highlighting workplace disparities.",
                            "her": "I didn’t realize the numbers were that significant.",
                            "thoughts": "You think you may have reached her logically."
                        }
                    },
                    "3": {
                        "text": "Suggest a team workshop on gender issues.",
                        "outcome": "The team agreed to hold a workshop, which led to more productive discussions about workplace equality.",
                        "pfeedback": "Your suggestion was met with support from others.",
                        "challenges": "Some colleagues were reluctant to attend, but they participated anyway.",
                        "encouragement": "Seeing your colleagues' openness to learning made you feel optimistic.",
                        "dialogue": {
                            "user": "I proposed a workshop to help us better understand these issues.",
                            "her": "A workshop could be helpful, but will everyone be open to it?",
                            "thoughts": "You’re hopeful that this could lead to meaningful change."
                        }
                    },
                    "4": {
                        "text": "Follow up with her afterward.",
                        "outcome": "She thanked you for the conversation and expressed a willingness to reflect more deeply on the issue.",
                        "pfeedback": "She appreciated your respectful approach.",
                        "challenges": "She was still defensive at times, but the conversation stayed civil.",
                        "encouragement": "You feel hopeful that this follow-up will lead to a lasting change.",
                        "dialogue": {
                            "user": "I followed up with her after the meeting to continue the discussion.",
                            "her": "I appreciate you taking the time to talk.",
                            "thoughts": "You feel hopeful that this follow-up will lead to lasting change."
                        }
                    }
                }
            },
            "B": {
                "dialogue": {
                    "user": "I can't let this slide. It’s important we address bias openly.",
                    "her": "But isn't it just a discussion? People are allowed to have different opinions.",
                    "thoughts": "You realize that challenging her may create tension, but it's necessary to foster a more equitable environment."
                },
                "sub_choices": {
                    "1": {
                        "text": "Invite her to a follow-up discussion after the meeting.",
                        "outcome": "The follow-up discussion helped clarify viewpoints, fostering a better understanding.",
                        "pfeedback": "Her willingness to continue the conversation was encouraging.",
                        "challenges": "She remained defensive but open to listening.",
                        "encouragement": "The dialogue was respectful, keeping future interactions positive.",
                        "dialogue": {
                            "user": "I suggested we have a private discussion to clear things up.",
                            "her": "I’m open to discussing this further, but I still have my doubts.",
                            "thoughts": "You feel hopeful that a one-on-one conversation might lead to a more nuanced understanding."
                        }
                    },
                    "2": {
                        "text": "Ask the team to share similar experiences.",
                        "outcome": "The team shared similar experiences, making her more aware of the issue.",
                        "pfeedback": "Collective voices made the discussion more impactful.",
                        "challenges": "Not all team members were comfortable sharing initially.",
                        "encouragement": "The conversation gained momentum as more voices joined in.",
                        "dialogue": {
                            "user": "I asked the team if others had similar experiences.",
                            "her": "I hadn’t realized it was such a common issue here.",
                            "thoughts": "You feel validated as more team members begin sharing their experiences."
                        }
                    },
                    "3": {
                        "text": "Propose creating a team initiative to address bias.",
                        "outcome": "The proposal led to a structured plan for addressing bias within the team.",
                        "pfeedback": "Colleagues appreciated the proactive approach.",
                        "challenges": "Initial resistance came from those uncertain about implementation.",
                        "encouragement": "The initiative was a step toward meaningful change.",
                        "dialogue": {
                            "user": "I proposed a structured initiative to address bias within the team.",
                            "her": "That could be interesting, but I’m not sure how it would work.",
                            "thoughts": "You feel encouraged that she’s at least considering the idea."
                        }
                    },
                    "4": {
                        "text": "Acknowledge her perspective while emphasizing the importance of allyship.",
                        "outcome": "Acknowledging her viewpoint opened a pathway for mutual understanding.",
                        "pfeedback": "She felt heard, which made her more receptive.",
                        "challenges": "She remained hesitant about fully accepting your stance.",
                        "encouragement": "The respectful exchange made future dialogues seem possible.",
                        "dialogue": {
                            "user": "I acknowledged her experience while emphasizing the need for allyship.",
                            "her": "I see your point, but I still believe my own experiences are valid.",
                            "thoughts": "You feel that recognizing her perspective may make her more open to hearing yours."
                        }
                    }
                }
            },
            "C": {
                "description": "You avoided the conversation altogether.",
                "dialogue": {
                    "user": "I decided to stay quiet, hoping the issue would resolve on its own.",
                    "her": "Nothing changed in her behavior.",
                    "thoughts": "However, you can’t shake the feeling that you missed an opportunity to challenge a harmful mindset."
                },
                "sub_choices": {
                    "1": {
                        "text": "Reflect on why you chose silence.",
                        "outcome": "You realize that fear of conflict held you back.",
                        "pfeedback": "The self-reflection provided clarity.",
                        "challenges": "The issue persisted without confrontation.",
                        "encouragement": "You are more aware of the impact of inaction.",
                        "dialogue": {
                            "user": "I decided not to confront her to avoid conflict.",
                            "her": "She continued behaving the same way.",
                            "thoughts": "You chose to maintain silence, but now recognize its limitations."
                        }
                    },
                    "2": {
                        "text": "Consider talking to a colleague about it.",
                        "outcome": "A colleague validated your concerns, offering support.",
                        "pfeedback": "It felt good to have someone else understand your perspective.",
                        "challenges": "It did not directly address the issue with her.",
                        "encouragement": "You feel more confident knowing you're not alone.",
                        "dialogue": {
                            "user": "I talked to a colleague about the situation.",
                            "her": "The colleague agreed with your concerns.",
                            "thoughts": "You feel more confident because you’re not the only one who thinks this way."
                        }
                    },
                    "3": {
                        "text": "Think about how to address it later.",
                        "outcome": "You decide to speak to her when the timing feels right.",
                                                "pfeedback": "You’re glad to have a plan in place.",
                        "challenges": "Delaying the conversation may weaken its impact.",
                        "encouragement": "You feel better prepared to address it later.",
                        "dialogue": {
                            "user": "I plan to talk to her when the timing feels right.",
                            "her": "She seems surprised but open to discussing it.",
                            "thoughts": "You feel you made the right decision to speak up, even if you waited initially."
                        }
                    },
                    "4": {
                        "text": "Accept that sometimes silence is okay.",
                        "outcome": "You realize that staying silent can be a strategic choice in certain situations.",
                        "pfeedback": "Your decision to stay quiet helped maintain peace temporarily.",
                        "challenges": "The behavior you hoped to change remained unaddressed.",
                        "encouragement": "You understand that timing matters, and you can choose to speak up when more appropriate.",
                        "dialogue": {
                            "user": "I chose not to confront her, thinking it wasn’t the right time.",
                            "her": "Her behavior remained unchanged.",
                            "thoughts": "You accept that not all issues require immediate confrontation, but change is still necessary."
                        }
                    }
                }
            },
            "D": {
                "dialogue": {
                    "user": "I spoke with my mentor for guidance on how to handle this.",
                    "her": "Your mentor offered support and advice.",
                    "thoughts": "You feel more prepared but still anxious about the upcoming conversation."
                },
                "sub_choices": {
                    "1": {
                        "text": "Ask your mentor how to approach the conversation effectively.",
                        "outcome": "Your mentor provided a structured approach that improved your confidence.",
                        "pfeedback": "The mentor’s tips made you feel more prepared.",
                        "challenges": "The conversation might still be challenging.",
                        "encouragement": "You feel encouraged by having a strategy in mind.",
                        "dialogue": {
                            "user": "I asked my mentor for specific tips on having a constructive discussion.",
                            "her": "Your mentor advised starting by acknowledging her perspective, then sharing your own experiences.",
                            "thoughts": "You feel more prepared to have a calm, respectful conversation that focuses on understanding."
                        }
                    },
                    "2": {
                        "text": "Get advice on how to maintain a positive relationship with her.",
                        "outcome": "The mentor's guidance helped you find a balance between addressing issues and preserving rapport.",
                        "pfeedback": "You appreciated the focus on maintaining a good relationship.",
                        "challenges": "Balancing confrontation with positivity is still delicate.",
                        "encouragement": "You’re hopeful that you can address concerns without damaging the relationship.",
                        "dialogue": {
                            "user": "I asked my mentor how to address the issue while preserving our professional relationship.",
                            "her": "Your mentor suggested approaching her with empathy and making it clear you value her contributions.",
                            "thoughts": "You feel reassured, knowing that you can address the problem without straining the relationship."
                        }
                    },
                    "3": {
                        "text": "Discuss the possibility of involving a mediator in the conversation.",
                        "outcome": "Your mentor supported the idea of mediation, adding structure to the discussion.",
                        "pfeedback": "You appreciated having a potential third party to keep the conversation neutral.",
                        "challenges": "Convincing her to agree to mediation could be difficult.",
                        "encouragement": "You’re more confident knowing there’s an objective party involved.",
                        "dialogue": {
                            "user": "I brought up the idea of having a neutral party mediate the discussion.",
                            "her": "Your mentor agreed, noting that mediation can help keep the conversation objective.",
                            "thoughts": "You consider that involving a mediator could make the conversation feel more balanced."
                        }
                    },
                    "4": {
                        "text": "Ask for resources to better understand internalized sexism.",
                        "outcome": "Your mentor provided helpful resources that deepened your understanding of the issue.",
                        "pfeedback": "The resources helped you better articulate your concerns.",
                        "challenges": "More information means a longer preparation time.",
                        "encouragement": "You feel empowered by having more knowledge, making you better equipped for the conversation.",
                        "dialogue": {
                            "user": "I asked my mentor if there are any resources to better understand internalized sexism.",
                            "her": "Your mentor recommended reading research articles and literature on internalized sexism.",
                            "thoughts": "You feel more empowered by gaining knowledge, strengthening your approach in future discussions."
                        }
                    }
                }
            }
        }

    }
}
