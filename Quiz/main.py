from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Si può prendere da Open Trivia DataBase (opentdb.com) il database di domande.
# Scegli in alto a destra il bottone API, con poi il numero di domande, categoria,
# tipo, categoria, difficoltà..... e lascia default encoding. Poi genera l'URL,
# copialo e incollalo nel browser e copia tutto. È distribuito in formato JSON,
# ma possiamo facilmente adattarlo per usarlo in Python.
# OCCHIO! A volte non vanno alcune difficoltà, poi il server s'imballa spesso,
# quindi se non va, riprovare!

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}.")
