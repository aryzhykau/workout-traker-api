from mongoengine import *
from entities.trainer.models import Trainer, Questionnaire, Question



def get_questionnaire(tg_id):
    trainer = Trainer.objects(tg_id=tg_id).first()
    if trainer.questionnaire:
        return trainer.questionnaire
    else:
        return []


def create_questionnaire(tg_id, questionnaire):
    trainer = Trainer.objects(tg_id=tg_id).first()
    trainer.questionnaire == questionnaire
    return True