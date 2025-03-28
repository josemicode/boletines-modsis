
from question_retriever import QuestionRetriever
from datetime import datetime

class CuOOra:
    def __init__(self):
        self.questions = []

    def add_question(self, a_question):
        self.questions.append(a_question)
        #! se crea una variable temporal que solo se usa una vez, sobra la linea del medio en todas
    def get_social_questions_for_user(self, user):
        social_retriever = QuestionRetriever.create_social()
        return social_retriever.retrieve_questions(self.questions, user)

    def get_topic_questions_for_user(self, user):
        topic_retriever = QuestionRetriever.create_topics()
        return topic_retriever.retrieve_questions(self.questions, user)

    def get_news_questions_for_user(self, user):
        news_retriever = QuestionRetriever.create_news()
        return news_retriever.retrieve_questions(self.questions, user)

    def get_popular_questions_for_user(self, user):
        popular_retriever = QuestionRetriever.create_popular_today()
        return popular_retriever.retrieve_questions(self.questions, user)


'''
class CuOOra:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions_by_type(self, type_):
        retriever_methods = {
            "social": QuestionRetriever.create_social,
            "topic": QuestionRetriever.create_topics,
            "news": QuestionRetriever.create_news,
            "popular": QuestionRetriever.create_popular_today,
        }
        if type_ not in retriever_methods:
            raise ValueError("Tipo de pregunta no válido")
        return retriever_methods[type_]().retrieve_questions(self.questions)

    def get_social_questions_for_user(self, user):
        return self.get_questions_by_type("social").retrieve_questions(self.questions, user)

    def get_topic_questions_for_user(self, user):
        return self.get_questions_by_type("topic").retrieve_questions(self.questions, user)

    def get_news_questions_for_user(self, user):
        return self.get_questions_by_type("news").retrieve_questions(self.questions, user)

    def get_popular_questions_for_user(self, user):
        return self.get_questions_by_type("popular").retrieve_questions(self.questions, user)
'''