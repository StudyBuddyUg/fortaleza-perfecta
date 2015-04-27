from django.db import models

# Create your models here.
class LowerGrade(models.Model):
    lower_grade_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.lower_grade_name


class UpperGrade(models.Model):
    upper_grade_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.upper_grade_name


class ThemePack(models.Model):
    grade = models.ForeignKey(LowerGrade)
    theme_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.theme_name


class TopicPack(models.Model):
    grade = models.ForeignKey(UpperGrade)
    subject_name = models.CharField(max_length=30)
    topic_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.topic_name


class Card(models.Model):
    question = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=200)
    answer = models.TextField()


    class Meta:
        abstract = True

    def __unicode__(self):
        return self.question


class ThemeCard(Card):
    # grade = models.ForeignKey(LowerGrade)
    theme = models.ForeignKey(ThemePack)


class TopicCard(Card):
    # grade = models.ForeignKey(UpperGrade)
    topic = models.ForeignKey(TopicPack)
