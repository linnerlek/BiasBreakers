scenarios = {
    1: {
        "description": "At a team meeting, a female colleague dismisses concerns about gender bias after another woman shares her experience of being interrupted by male colleagues. Your colleague makes comments like, 'I’ve never faced discrimination, so I don’t think it’s that big of a deal.' She frequently aligns herself with male colleagues, often downplaying workplace inequalities. You believe her behavior reflects internalized sexism and is counterproductive to gender equality.",
        "choices": {
            "A": "Speak to her privately and try to educate her about the importance of being an ally",
            "B": "Publicly challenge her comments during the meeting",
            "C": "Stay quiet and hope things improve on their own",
            "D": "Seek advice from a female mentor or trusted colleague on how to handle the situation"
        },
        "outcomes": {
            "A": {
                "dialogue": {
                    "user": "Hey, I wanted to talk to you about something from the meeting. It’s important to me that we create a space where everyone feels heard, and I think what you said earlier might have unintentionally downplayed some real challenges people face.",
                    "her": "I didn’t mean anything by it. I just feel like everyone should focus on working hard instead of pointing out differences.",
                    "thoughts": "You sense some defensiveness but recognize an opportunity to engage with her perspective thoughtfully."
                },
                "sub_choices": {
                    "1": {
                        "text": "Ask others for their opinions.",
                        "outcome": "After your private conversation, you share your concerns with a few trusted colleagues, asking if they’ve experienced similar situations. During the next meeting, several team members bravely share their stories, creating a moment of solidarity. Your colleague listens attentively, visibly surprised by the number of shared experiences.",
                        "pfeedback": "Bringing in other perspectives was a great move. It helped her see that others in the team have similar concerns, making your argument stronger without singling her out.",
                        "challenges": "It may take time to build trust with colleagues and encourage them to share openly, especially if they fear judgment or repercussions.",
                        "encouragement": "Great job starting an open dialogue! Even if the conversation doesn’t change her mind entirely, you’re fostering a culture where people feel safe to share.",
                        "dialogue": {
                            "user": "I’ve talked to a few team members, and it turns out they’ve faced similar challenges. I think hearing their stories might add another perspective to what we talked about.",
                            "her": "I had no idea this was such a common issue. I thought it was just isolated incidents.",
                            "thoughts": "She seemed surprised but thoughtful, like she’s starting to understand that this isn’t just about one person’s experience."
                        }
                    },
                    "2": {
                        "text": "Provide data on gender bias.",
                        "outcome": "You follow up by sharing well-researched data and studies highlighting the prevalence and impact of gender bias in the workplace. Seeing the statistics, your colleague grows quieter and starts to reflect. Although she initially questions whether these findings apply to your team specifically, the evidence leaves her with something to consider.",
                        "pfeedback": "Using data shows that you came prepared and approached the topic objectively, making it less about personal opinions and more about systemic issues.",
                        "challenges": "She might still push back by questioning whether the data applies to your workplace or relying on personal anecdotes to dismiss broader trends.",
                        "encouragement": "You did an amazing job supporting your argument with evidence. Even if she’s skeptical, you’re planting a seed for future reflection.",
                        "dialogue": {
                            "user": "There’s a lot of research on this topic. For example, studies show that women are more likely to be interrupted during meetings or have their ideas dismissed. It’s not just about one person’s experience—it’s a pattern.",
                            "her": "These numbers are shocking. I didn’t realize it was such a widespread issue.",
                            "thoughts": "She seemed caught off guard by the stats, but I could tell it made her think about the bigger picture."
                        }
                    },
                    "3": {
                        "text": "Suggest a team workshop on gender issues.",
                        "outcome": "You propose organizing a workshop to address gender dynamics in the workplace. Surprisingly, the idea is well-received by the team, including your colleague. The workshop sparks productive conversations, with participants sharing insights and strategies for fostering a more inclusive environment.",
                        "pfeedback": "Proposing a workshop was a forward-thinking solution. It opens the door for the entire team to learn and grow, showing leadership and initiative.",
                        "challenges": "Not everyone might take the workshop seriously, and some colleagues could see it as unnecessary or even a waste of time.",
                        "encouragement": "Suggesting the workshop was a bold step! You’re taking action to address the issue on a larger scale, and that’s worth applauding.",
                        "dialogue": {
                            "user": "I was thinking it could help if we did a workshop on gender dynamics in the workplace. It would give us all tools to better support each other.",
                            "her": "A workshop sounds interesting. I just hope everyone will take it seriously.",
                            "thoughts": "You’re hopeful that this initiative will build long-term awareness and collaboration."
                        }
                    },
                    "4": {
                        "text": "Follow up with her afterward.",
                        "outcome": "She thanked you for the conversation and expressed a willingness to reflect more deeply on the issue.",
                        "pfeedback": "Following up shows dedication and consistency. It reinforces that you care about the issue and want to keep the conversation going in a respectful way.",
                        "challenges": "It might be difficult to stay patient if she continues to push back or if her progress feels slow.",
                        "encouragement": "Amazing work checking in after the initial conversation! You’re showing empathy and persistence, which is key to creating lasting change.",
                        "dialogue": {
                            "user": "I wanted to check in after our chat earlier. How are you feeling about what we talked about?",
                            "her": "Thanks for talking to me about it. I’ve been thinking about what you said and trying to see things differently.",
                            "thoughts": "You feel hopeful, knowing that even small steps toward understanding can lead to greater progress."
                        }
                    }
                }
            },
            "B": {
                "dialogue": {
                    "user": "I just want to pause for a second. I think it’s important to acknowledge that what you said might come across as dismissive of some real challenges women face in the workplace.",
                    "her": "I’m not dismissing anyone. I just think we all have to deal with challenges, so why make it about gender?",
                    "thoughts": "You notice a few colleagues shifting uncomfortably in their seats. Some seem supportive, while others appear unsure about the confrontation."
                },
                "sub_choices": {
                    "1": {
                        "text": "Share a personal example.",
                        "outcome": "You share a relevant experience from your own career, highlighting how similar comments in the past have impacted your confidence or opportunities. Your team listens attentively, and the discussion shifts toward understanding how small comments can have a big effect.",
                        "pfeedback": "Sharing your story adds authenticity and helps others connect emotionally with the issue, encouraging empathy and reflection.",
                        "challenges": "Opening up can feel vulnerable, and there’s a risk your example might be dismissed if others don’t empathize.",
                        "encouragement": "You showed courage by sharing your experience. Even if not everyone understands immediately, you’ve made an impression that could inspire future change.",
                        "dialogue": {
                            "user": "I wanted to share a quick story about something similar I experienced. Comments like that can unintentionally discourage people, even if they’re meant as a joke.",
                            "her": "I didn’t think of it that way. I’m sorry if I made you or anyone else feel uncomfortable.",
                            "thoughts": "Her apology seemed sincere. Maybe sharing my perspective helped her see things differently."
                        }
                    },
                    "2": {
                        "text": "Focus on team dynamics.",
                        "outcome": "You steer the conversation toward the importance of fostering an inclusive and supportive environment for everyone on the team. The discussion remains constructive, and several teammates chime in to share their thoughts.",
                        "pfeedback": "Focusing on team values helps frame the issue as a shared responsibility, encouraging others to get involved.",
                        "challenges": "Generalizing the issue might dilute the impact, and not everyone may feel motivated to act.",
                        "encouragement": "Great job emphasizing the team’s shared goals. You’re encouraging collaboration and creating a safe space for open dialogue.",
                        "dialogue": {
                            "user": "I think it’s important that we make sure everyone on the team feels valued and supported. Comments like that might make it harder for some people to speak up.",
                            "her": "That’s a fair point. I hadn’t thought about how it might come across to others.",
                            "thoughts": "She seemed thoughtful, like she’s starting to realize the broader impact of her words."
                        }
                    },
                    "3": {
                        "text": "Ask for clarification.",
                        "outcome": "You ask her to explain what she meant by her comment, prompting her to think critically about her words. She hesitates and then acknowledges that she might not have been as considerate as she should have.",
                        "pfeedback": "Asking for clarification helps people reflect on their own biases and encourages self-awareness.",
                        "challenges": "She might feel defensive or uncomfortable, which could make the conversation more difficult to navigate.",
                        "encouragement": "You handled the situation tactfully. By asking questions, you encouraged reflection without directly confronting her.",
                        "dialogue": {
                            "user": "I just wanted to clarify—what did you mean by that comment?",
                            "her": "I guess I didn’t really think it through. It was just an offhand remark, but I see how it might not have come across well.",
                            "thoughts": "Her response felt genuine. Hopefully, this conversation will make her more mindful in the future."
                        }
                    },
                    "4": {
                        "text": "Propose an immediate solution.",
                        "outcome": "You suggest that the team establish ground rules for meetings, such as focusing on constructive feedback and avoiding dismissive remarks. The idea is well-received, and the team agrees to revisit its meeting protocols.",
                        "pfeedback": "Proposing a solution demonstrates leadership and provides a clear path forward, preventing similar issues in the future.",
                        "challenges": "Not everyone might agree with the proposed changes, and some might see it as unnecessary or restrictive.",
                        "encouragement": "You took initiative and offered a proactive solution. Great work leading by example!",
                        "dialogue": {
                            "user": "How about we agree on some ground rules for meetings to make sure everyone feels heard and respected?",
                            "her": "That sounds like a good idea. I’d be open to discussing it further.",
                            "thoughts": "Her response was encouraging. She seems willing to work toward a more inclusive environment."
                        }
                    }
                }
            },
            "C": {
                "dialogue": {
                    "user": "I decided to stay quiet, hoping the issue would resolve on its own.",
                    "her": "Nothing changed in her behavior.",
                    "thoughts": "I couldn’t shake the feeling that I missed a chance to challenge her perspective. By not addressing it, I let her behavior continue unchecked."
                },
                "sub_choices": {
                    "1": {
                        "text": "Reflect on why you chose silence.",
                        "outcome": "You recognize that fear of conflict or uncertainty about how to handle the situation led you to avoid the conversation. You understand that staying silent allowed the behavior to continue, but it gave you the chance to reflect on your approach.",
                        "pfeedback": "The self-reflection helped you understand the underlying reasons for your silence, giving you clarity for future situations.",
                        "challenges": "You might feel frustrated by not addressing the issue, and your colleague’s behavior continues unchanged.",
                        "encouragement": "Taking time to reflect shows you're growing in self-awareness, which is an important step toward handling tough situations better in the future.",
                        "dialogue": {
                            "user": "I decided not to confront her to avoid conflict.",
                            "her": "She continued behaving the same way.",
                            "thoughts": "You chose to maintain silence, but now recognize its limitations."
                        }
                    },
                    "2": {
                        "text": "Consider talking to a colleague about it.",
                        "outcome": "You talk to a trusted colleague, gaining support, but the issue with your colleague remains unresolved.",
                        "pfeedback": "It felt good to have someone understand, but the problem with your colleague isn’t fixed yet.",
                        "challenges": "While you found emotional support, the behavior still isn’t addressed, and it might feel like you’re avoiding confrontation.",
                        "encouragement": "It’s great that you sought support—this will help you feel stronger when you eventually address the issue directly",
                        "dialogue": {
                            "user": "I talked to a colleague about the situation.",
                            "her": "The colleague agreed with your concerns.",
                            "thoughts": "You feel more confident because you’re not the only one who thinks this way."
                        }
                    },
                    "3": {
                        "text": "Think about how to address it later.",
                        "outcome": "You decide to speak to her when the timing feels right.",
                        "pfeedback": "You’re glad to have a plan in place. It feels like you’ve made a thoughtful choice.",
                        "challenges": "Delaying the conversation may weaken its impact. You might lose the opportunity for a more immediate resolution.",
                        "encouragement": "Great job taking a moment to think things through! You’re setting yourself up to handle it with confidence when the time is right.",
                        "dialogue": {
                            "user": "I think I’ll wait for a better moment to talk to her.",
                            "her": "She looks a bit surprised, but she’s open to talking when you’re ready",
                            "thoughts": "You feel that giving it time might make the conversation more effective. It’s a relief knowing you have a plan in place"
                        }
                    },
                    "4": {
                        "text": "Accept that sometimes silence is okay.",
                        "outcome": "You realize that staying silent can be a strategic choice in certain situations.",
                        "pfeedback": "Your decision to stay quiet helped maintain peace temporarily, but you still want to address the issue later.",
                        "challenges": "The behavior you hoped to change remained unaddressed, and you might feel unsettled by not taking action right away.",
                        "encouragement": "Well done for recognizing when silence can be powerful. You’re making a wise choice by waiting for the right moment to speak up.",
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
                    "her": "Your mentor offered support and practical advice on how to approach the situation.",
                    "thoughts": "You feel a bit more at ease knowing you have someone who understands and is offering advice, but you're still anxious about how to handle the conversation with her."
                },
                "sub_choices": {
                    "1": {
                        "text": "Ask your mentor how to approach the conversation effectively.",
                        "outcome": "Your mentor gave you a step-by-step strategy, which increased your confidence in managing the upcoming conversation.",
                        "pfeedback": "You feel much more prepared with a clear approach that you can follow.",
                        "challenges": "Even with the strategy, the conversation may still be tense and emotional, and you're not entirely sure how she will react.",
                        "encouragement": "You've got a solid plan now—having a strategy is half the battle! You've taken an important step toward handling this with confidence.",
                        "dialogue": {
                            "user": "I asked my mentor for concrete advice on how to approach the conversation without it getting too heated.",
                            "her": "Your mentor gave you detailed steps: start by acknowledging her perspective, then share your experiences calmly, focusing on how you feel, not on what she did wrong.",
                            "thoughts": "With a clear plan in mind, you feel more confident about keeping the conversation respectful and productive. You can approach this with a level head, which will be important for both of you."
                        }
                    },
                    "2": {
                        "text": "Get advice on how to maintain a positive relationship with her.",
                        "outcome": "The mentor helped you see how important it is to balance addressing the issue with keeping the relationship intact, helping you navigate the conversation with care.",
                        "pfeedback": "You feel relieved that your mentor emphasized the importance of the relationship and gave you the tools to approach the issue while being mindful of her feelings.",
                        "challenges": "It's tough to strike the right balance between confronting her on the issue and not coming across as overly critical, especially since you value the relationship.",
                        "encouragement": "You’ve got a clear mindset: confrontation doesn't always mean confrontation in a negative way! With the right approach, you can resolve the issue and keep things positive.",
                        "dialogue": {
                            "user": "I asked my mentor for advice on how to talk to her without ruining our professional relationship.",
                            "her": "Your mentor suggested approaching her with empathy, acknowledging her strengths, and gently explaining how her actions have affected you. Make it clear you want to find a solution, not just vent.",
                            "thoughts": "You feel more confident now—understanding that you can address your concerns while showing respect for her work. You’re feeling better about the outcome."
                        }
                    },
                    "3": {
                        "text": "Discuss the possibility of involving a mediator in the conversation.",
                        "outcome": "Your mentor agreed that bringing a neutral third party into the discussion could help keep it productive, objective, and prevent either of you from feeling personally attacked.",
                        "pfeedback": "The idea of mediation gives you comfort—having a mediator might help both sides feel heard in a more structured environment.",
                        "challenges": "It may be hard to convince her to agree to having a mediator, especially if she feels defensive or doesn’t see the need for it.",
                        "encouragement": "You’re being proactive and looking for ways to keep things neutral. The fact that you're considering a third party shows you're dedicated to making this work in a healthy, constructive way!",
                        "dialogue": {
                            "user": "I spoke to my mentor about possibly involving a mediator in case the conversation becomes too heated.",
                            "her": "Your mentor thinks it's a good idea—especially if it helps both sides feel like their perspectives are being respected. They suggested it might ease the tension and keep things focused on solutions.",
                            "thoughts": "You now feel more open to the idea of bringing in someone impartial—this could help smooth over any tension, allowing for a much more productive discussion."
                        }
                    },
                    "4": {
                        "text": "Ask for resources to better understand internalized sexism.",
                        "outcome": "Your mentor provided a few insightful resources—articles, books, and research—that helped you better understand internalized sexism, enabling you to articulate your concerns more clearly and thoughtfully.",
                        "pfeedback": "These resources gave you the depth of understanding you needed to address the issue more convincingly, empowering you to speak with authority and empathy.",
                        "challenges": "The more you learn, the more you realize how deep-rooted the problem is , and this could take time to fully understand and address.",
                        "encouragement": "You’ve taken the time to educate yourself—and that makes you more prepared than ever. Knowledge is power, and now you’ve got the tools to have a more informed and effective conversation.",
                        "dialogue": {
                            "user": "I asked my mentor for resources to better understand internalized sexism, so I can talk about it more effectively.",
                            "her": "Your mentor recommended several books and articles that highlight how internalized sexism impacts women in the workplace and how to address it with compassion and confidence.",
                            "thoughts": "You feel empowered with this knowledge—understanding the topic more deeply means you’ll be better equipped to address it thoughtfully, without missing any key points."
                        }
                    }
                }
            }
        }

    }
}
