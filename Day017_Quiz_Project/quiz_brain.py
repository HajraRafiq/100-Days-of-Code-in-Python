class QuizBrain():
    def __init__(self,ques_list):
        self.ques_list = ques_list
        self.ques_num=0
        self.score=0

    def still_has_questions(self):
        if self.ques_num < len(self.ques_list):
            return True
        else:
            return False

    def next_ques(self):
        current_ques= self.ques_list[self.ques_num]
        self.ques_num+=1
        user_answer= input(f"Q.{self.ques_num}: {current_ques.text} (True/False)")
        self.check_answer(user_answer , current_ques.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print("You got it right")
        else:
            print("Thats wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.ques_num}")
        print("\n")

