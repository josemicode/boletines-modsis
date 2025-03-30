
from datetime import datetime

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

#Extraction method como en la clase answer
    '''
    def _filter_votes(self, positive: bool):
        """Filtra los votos en función de si son positivos o negativos."""
        return [vote for vote in self.votes if vote.is_like() == positive]

    def positive_votes(self):
        return self._filter_votes(True)
    
    def negative_votes(self):
        return self._filter_votes(False)
    '''
    
    def positive_votes(self): 
        r = [] #! code smelling: r = feo, hay que cambiarlo
        for vote in self.votes:
            if vote.is_like():
                r.append(vote) #! code smelling: r = feo, hay que cambiarlo
        return r #! code smelling: r = feo, hay que cambiarlo

    def negative_votes(self):
        r = [] #! code smelling: r = feo, hay que cambiarlo
        for vote in self.votes:
            if not vote.is_like():
                r.append(vote) #! code smelling: r = feo, hay que cambiarlo
        return r #! code smelling: r = feo, hay que cambiarlo

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

