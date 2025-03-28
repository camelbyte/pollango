from django.db import models
import datetime
from django.utils import timezone



class Question(models.Model):
    """
    Description: A question in the poll.
    Fields:
        question_text: The text of the question.
        pub_date: The date the question was published.
    Methods:
        __str__: Returns a string representation of the question.
    """
    def __str__(self):
        return self.question_text


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    def was_published_recently(self):
        """
        Returns True if the question was published within the last day.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    """
    Description: A choice for a question in the poll.
    Fields:
        question: A foreign key to the related question.
        choice_text: The text of the choice.
        votes: The number of votes for this choice.
    Methods:
        __str__: Returns a string representation of the choice.
    """
    def __str__(self):
        return self.choice_text


    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)