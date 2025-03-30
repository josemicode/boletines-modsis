from datetime import datetime
from abc import ABC, abstractmethod

class CuOOra:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions_by_type(self, type_, user):
        retriever_methods = {
            "social": QuestionRetriever.create_social,
            "topic": QuestionRetriever.create_topics,
            "news": QuestionRetriever.create_news,
            "popular": QuestionRetriever.create_popular_today,
        }
        if type_ not in retriever_methods:
            raise ValueError("Tipo de pregunta no válido")
        retriever = retriever_methods[type_]()
        return retriever.retrieve_questions(self.questions, user)

    def get_social_questions_for_user(self, user):
        return self.get_questions_by_type("social", user)

    def get_topic_questions_for_user(self, user):
        return self.get_questions_by_type("topic", user)

    def get_news_questions_for_user(self, user):
        return self.get_questions_by_type("news", user)

    def get_popular_questions_for_user(self, user):
        return self.get_questions_by_type("popular", user)


    #================================#
    
class QuestionRetrievalStrategy(ABC):
    @abstractmethod
    def retrieve_questions(self, questions, a_user):
        pass

class SocialRetriever(QuestionRetrievalStrategy):
    def retrieve_questions(self, questions, a_user):
        following_questions = []
        for follow in a_user.following:
            following_questions.extend(follow.questions)
        sorted_q = sorted(following_questions, key=lambda q: len(q.positive_votes()))
        q_ret = sorted_q[-min(100, len(sorted_q)):]
        return [q for q in q_ret if q.user != a_user]

class TopicRetriever(QuestionRetrievalStrategy):
    def retrieve_questions(self, questions, a_user):
        topics_questions = []
        for topic in a_user.get_topics_of_interest():
            topics_questions.extend(topic.questions)
        sorted_q = sorted(topics_questions, key=lambda q: len(q.positive_votes()))
        q_ret = sorted_q[-min(100, len(sorted_q)):]
        return [q for q in q_ret if q.user != a_user]

class NewsRetriever(QuestionRetrievalStrategy):
    def retrieve_questions(self, questions, a_user):
        news_questions = [q for q in questions if q.timestamp.date() == datetime.today().date()]
        sorted_q = sorted(news_questions, key=lambda q: len(q.positive_votes()))
        q_ret = sorted_q[-min(100, len(sorted_q)):]
        return [q for q in q_ret if q.user != a_user]

class PopularTodayRetriever(QuestionRetrievalStrategy):
    def retrieve_questions(self, questions, a_user):
        today_questions = [q for q in questions if q.timestamp.date() == datetime.today().date()]
        if today_questions:
            average_votes = sum(len(q.positive_votes()) for q in today_questions) / len(today_questions)
            popular_questions = [q for q in today_questions if len(q.positive_votes()) > average_votes]
            sorted_q = sorted(popular_questions, key=lambda q: len(q.positive_votes()))
            q_ret = sorted_q[-min(100, len(sorted_q)):]
        else:
            q_ret = []
        return [q for q in q_ret if q.user != a_user]

class QuestionRetriever: #!

    @classmethod
    def create_social(cls):
        return SocialRetriever()

    @classmethod
    def create_topics(cls):
        return TopicRetriever()

    @classmethod
    def create_news(cls):
        return NewsRetriever()

    @classmethod
    def create_popular_today(cls):
        return PopularTodayRetriever()
    
    #================================#

class Answer(object): 
    def __init__(self, question, user, description):
        self.votes = []
        self.timestamp = datetime.now()
        self.user = user
        self.description = description
        self.question = question
        self.question.add_answer(self)
    
    def _filter_votes(self, positive: bool):
        """Filtra los votos en función de si son positivos o negativos."""
        return [vote for vote in self.votes if vote.is_like() == positive]

    def positive_votes(self):
        return self._filter_votes(True)
    
    def negative_votes(self):
        return self._filter_votes(False)

    def get_question(self):
        return self.question
		
    def get_user(self):
        return self.user

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
	
    def get_timestamp(self):
        return self.timestamp

    def add_vote(self, a_vote):                                     #? code smelling sospechoso "a_vote"
        if any(vote.user == a_vote.user for vote in self.votes):
            raise ValueError("Este usuario ya ha votado")
        self.votes.append(a_vote)

    def get_votes(self):
        return self.votes

    #================================#
    
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
        question_score = sum(10 for q in self.questions if len(q.positive_votes()) > len(q.negative_votes()))
        answer_score = sum(20 for a in self.answers if len(a.positive_votes()) > len(a.negative_votes()))
        return question_score + answer_score

    #================================#

#* De chill, nada que cambiar
class Vote(object): #* Clase limpia
    
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

    #================================#
    
class Question:
    def __init__(self, user, title, description, topics=[]):
        self.timestamp = datetime.now()
        self.title = title
        self.description = description
        self.answers = []
        self.votes = []
        self.user = user
        self.user.add_question(self)
        self.topics = []
        for topic in topics:
            self.add_topic(topic)

    def set_description(self, an_object):
        self.description = an_object

    def get_description(self):
        return self.description

    def _filter_votes(self, positive: bool):
        """Filtra los votos en función de si son positivos o negativos."""
        return [vote for vote in self.votes if vote.is_like() == positive]

    def positive_votes(self):
        return self._filter_votes(True)
    
    def negative_votes(self):
        return self._filter_votes(False)

    def get_topics(self):
        return self.topics

    def get_title(self):
        return self.title
    
    def set_title(self, a_title):
        self.title = a_title

    def get_user(self):
        return self.user

    def get_timestamp(self):
        return self.timestamp

    def get_votes(self):
        return self.votes

    def add_vote(self, a_vote): #? code smelling sospechoso "a_vote"
        if any(vote.user == a_vote.user for vote in self.votes): 
            raise ValueError("Este usuario ya ha votado")
        self.votes.append(a_vote)

    def add_topic(self, a_topic):
        if a_topic in self.topics:  #? code smelling sospechoso "a_topic"
            raise ValueError("El tópico ya está agregado.")
        self.topics.append(a_topic)
        a_topic.add_question(self)

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_best_answer(self):
        if not self.answers:
            return None
        
        return sorted(self.answers, key=lambda a: len(a.positive_votes()) - len(a.negative_votes()), reverse=True)[0]

    #================================#
    
class Topic:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.questions = []

    def add_question(self, a_question):
        self.questions.append(a_question)

    def get_description(self):
        return self.description

    def set_description(self, an_object):
        self.description = an_object

    def get_name(self):
        return self.name

    def set_name(self, an_object):
        self.name = an_object

    def get_questions(self):
        return self.questions