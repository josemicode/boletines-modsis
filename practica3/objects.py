
from datetime import datetime


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.questions = []
        self.answers = []
        self.topics_of_interest = []
        self.following = []
        self.votes = []

    def add_topic(self, a_topic): #? code smelling sospechoso "a_vote"
        self.topics_of_interest.append(a_topic)

    def get_votes(self):
        return self.votes

    def questions_of_interest(self):
        return self.question_retriever.retrieve_questions(self)

    def get_question_retriever(self):
        return self.question_retriever

    def add_question(self, a_question):
        self.questions.append(a_question)

    def get_username(self):
        return self.username

    def get_questions(self):
        return self.questions

    def follow(self, a_user):
        self.following.append(a_user)

    def stop_follow(self, a_user):
        self.following.remove(a_user)

    def get_answers(self):
        return self.answers

    def get_following(self):
        return self.following

    def add_vote(self, a_vote):
        self.votes.append(a_vote)

    def get_password(self):
        return self.password

    def add_answer(self, an_answer):
        self.answers.append(an_answer)

    def get_topics_of_interest(self):
        return self.topics_of_interest

    def set_password(self, an_object):
        self.password = an_object

    def set_username(self, an_object):
        self.username = an_object

    def calculate_score(self):
        score = 0
        for question in self.questions:
            pv = len(question.positive_votes())
            nv = len(question.negative_votes())
            if pv > nv:
                score += 10

        # Sumar puntos por respuestas con más votos positivos que negativos
        for answer in self.answers: #* pv -> positive//// nv -> negative
            pv = len(answer.positive_votes())
            nv = len(answer.negative_votes())
            if pv > nv:
                score += 20

        return score


class Vote(object): # Clase limpia
    
    def __init__(self, user, is_like=True):
        self.is_positive_vote = is_like
        self.timestamp = datetime.now()
        self.user = user

    def is_like(self):
        return self.is_positive_vote

    def get_user(self):
        return self.user

    def like(self):
        self.is_positive_vote = True

    def dislike(self):
        self.is_positive_vote = False
