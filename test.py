import chatterbot
import chatterbot.trainers as trainers
bot = chatterbot("test")
trainers = trainers.ChatterBotCorpusTrainer(bot)
