import random

class Messages:
    """Class to store Bot messages. """

    #Create a Dictionary with all Messages
    books = {
        "The Art of Laziness, by Library Mindset" : [
            "Nunca vai haver um timing perfeito, portanto o melhor é começar já.",
            "Pomodoro Technique - Trabalhar durante 25 minutos e descansar 5.",
            "Se algo demorar menos de 5 minutos, é para ser feito imediatamente.",
            "Multitasking não resulta, é preferível fazer 1 coisa de cada vez.",
            "Aprender a dizer que não.",
            "Fazer as tarefas que odiamos primeiro.",
            "Fazer coisas que gostamos.",
            "Ler sobre tudo.",
            "“Daqui a 20 anos, as únicas pessoas que se vã lembrar que trabalhaste até tarde vão ser os teus filhos”, Sahil Bloom",
            "Nunca falhar em nada durante dois dias seguidos.",
            "Comer até ficar 80% cheio.",
            "“Se uma decisão for reversível, toma-se a decisão o mais rápido possível, se for irreversível, toma-se o mais tardar possível”, Shane Parris.",
        ],
        "Como falar com todos, by Leil Lowndes" : [
            "O Sorriso Inundante: Não sorria imediatamente ao cumprimentar alguém, como se fosse qualquer pessoa que entrasse no seu campo de visão fosse a benficiária. Em vez diso, olhe para o rosto da outra pessoa por um segundo. Faça uma pausa. Absorva a personalidade dela. Depois, deixe que um sorriso rasgado, caloroso e recetivo inunde o seu rosto e lhe transborde nos olhos. Desta maneira irá envolver o destinatário como uma onda quente. O atraso de uma fração de segundo convence as pessoas que o seu sorriso é genuino e apenas para elas.",
        ]
    }

    def chooseMessage(self):
        """ Chooses a random message from a random Book """
        
        #Randomly chooses a random book
        book = random.choice(list(self.books.keys()))

        #Randomly chooses a message from a random book
        message = random.choice(list(self.books[book]))

        return f"{message}\n{book}"



