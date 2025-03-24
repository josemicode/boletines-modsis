
from datetime import datetime

class QuestionRetriever:

    @classmethod
    def create_social(cls):
        return cls._create_with_option("social")

    @classmethod
    def create_topics(cls):
        return cls._create_with_option("topics")

    @classmethod
    def create_news(cls):
        return cls._create_with_option("news")

    @classmethod
    def create_popular_today(cls):
        return cls._create_with_option("popularToday")

    @classmethod
    def _create_with_option(cls, option):
        instance = cls()
        instance._set_option(option)
        return instance
    
    def _set_option(self, an_option):
        self.option = an_option

    def retrieve_questions(self, questions, a_user):
        q_ret = []

        if self.option == "social":
            following_col = []
            for follow in a_user.following:
                following_col.extend(follow.questions)
            temp = sorted(following_col, key=lambda q: len(q.positive_votes()))
            q_ret = temp[-min(100, len(temp)):]

        elif self.option == "topics":
            topics_col = []
            for topic in a_user.get_topics_of_interest():
                topics_col.extend(topic.questions)
            temp = sorted(topics_col, key=lambda q: len(q.positive_votes()))
            q_ret = temp[-min(100, len(temp)):]

        elif self.option == "news":
            news_col = []
            for question in questions:
                if question.timestamp.date() == datetime.today().date():
                    news_col.append(question)
            temp = sorted(news_col, key=lambda q: len(q.positive_votes()))
            q_ret = temp[-min(100, len(temp)):]

        elif self.option == "popularToday":
            today_questions = [q for q in questions if q.timestamp.date() == datetime.today().date()]
            if today_questions:
                average_votes = sum(len(q.positive_votes()) for q in today_questions) / len(today_questions)
                popular_questions = []
                for q in today_questions:
                    if len(q.positive_votes()) > average_votes:
                        popular_questions.append(q)
                temp = sorted(popular_questions, key=lambda q: len(q.positive_votes()))
                q_ret = temp[-min(100, len(temp)):]

        return [q for q in q_ret if q.user != a_user]
