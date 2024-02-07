from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(q_list=question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

