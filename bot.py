from nltk.chat.util import Chat, reflections

# Formato:
# [     
#         r"mi nombre es (.*)",
#         ["Hola %1, ¿cómo puedo ayudarte?",]
# ],

pairs = [
    [r"Mi nombre es (.*)",
    ["Hola %1, que tal como estas dime ¿en que puedo ayudarte?"],],
    [r"Quisiera saber cual es tu nombre",
    ["Bueno es facil soy ChatBot diseñado por Agustin como practica"],],
    [r"(.*) ayuda (.*)",
    ["Especificamente, ¿en que necesitas ayuda?"],],
    [r"(.*) definime (.*)",
    ["No cuento con la definicion de lo que me proporcionas"],],
]

def chatbot():
    print("El bot ha sido inicializado correctamente...")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()