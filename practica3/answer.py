class Answer(object): 
    def __init__(self, question, user, description):
        self.votes = []
        self.timestamp = datetime.now()
        self.user = user
        self.description = description
        self.question = question
        self.question.add_answer(self)

    def positive_votes(self):
        r = []
        for vote in self.votes:
            if vote.is_like():
                r.append(vote)
        return r
	
    def negative_votes(self):
        r = [] #! code smelling: r = feo, hay que cambiarlo
        for vote in self.votes:
            if not vote.is_like():
                r.append(vote) #! code smelling: r = feo, hay que cambiarlo
        return r #! code smelling: r = feo, hay que cambiarlo
	
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
