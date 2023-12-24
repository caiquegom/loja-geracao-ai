from utils.textGeneration import generateText

userQuestion = input("Pergunta: ")

answer = generateText(userQuestion)
print("Resposta:", answer)
