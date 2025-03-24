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
