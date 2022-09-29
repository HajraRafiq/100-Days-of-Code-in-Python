from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    ques_text = ques["text"]
    ques_answer = ques["answer"]
    new_ques = Question(ques_text,ques_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():

    quiz.next_ques()
print("You've completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.ques_num}")