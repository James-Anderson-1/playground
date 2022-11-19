answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

response = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

if response[-1] == answers[len(response)-1]:
    correct = True
else:
    correct = False

if not correct:
    del response[-1]
    print("sorry, please try the last question again!")
elif len(response) < len(answers):
    print("Quiz not complete.")
    correct = str(len(response))
    print("You've got " + correct + " answers correct so far, please add an answers for the next question.")
else:
    print("Well done, you have completed the quiz!")