## initialize chatter bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    name='GUI Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ],
    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'],
    database_uri='sqlite:///database.db',
    read_only=True
)

"""corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')"""


## training corpus list
## Disable these two lines below AFTER first run when a *.db file is generated in project directory
print(bot.get_response("Who are you"))