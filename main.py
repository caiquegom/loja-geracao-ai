import os
from utils.textGeneration import generateText
from utils.imageGeneration import generateImage

generationChoice = 0

while True:
    generationChoice = int(input("Escolha uma opção:\n\n[1] - Texto\n[2] - Imagem\n\nOpção: "))
    os.system("clear")

    match generationChoice:
        case 1:
            userQuestion = input("Pergunta: ")
            answer = generateText(userQuestion)
            print("Resposta:", answer)
            break
        case 2:
            userPrompt = input("Descreva a imagem: ")
            imageUrl = generateImage(userPrompt)
            print("Link da imagem", imageUrl)
            break
        case _:
            print("Digite uma opção válida.")
