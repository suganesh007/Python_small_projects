class QuizBrain:  # quiz

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)  # it tells true or false

    def next_question(self):
        current_q = self.question_list[self.question_number]
        print(current_q)
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} ('True / False'):")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you got it right")
            self.score += 1
        else:
            print("that's wrong")

        print(f"the answer is, {correct_ans}")
        print(f"your current score is {self.score} / {self.question_number}")
        print("\n")
