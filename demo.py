import en_core_web_sm
nlp = en_core_web_sm.load()

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
