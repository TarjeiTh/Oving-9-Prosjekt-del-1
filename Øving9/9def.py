# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:54:35 2021

@author: tarje
"""

class MultipleChoiceQuestion:
    def __init__(self, question, options, correct):
        self.__question = question
        self.__options = options
        self.__correct = correct

    def __str__(self):
        question = self.__question + '\n'
        for i in range(len(self.__options)) :
            question += '{}. {}\n'.format(i, self.__options[i])

        return question

    def check_answer(self, user_choice):
        return user_choice == self.__correct

    def correct_answer_text(self):
        return self.__options[self.__correct]


def readFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    questions = []

    for line in lines:
        question, correct, options = line.split(':')

        question = question.strip()

        correct = int(correct.strip())

        options = options.strip().strip('[]')

        options = [i.strip() for i in options.split(',')]

        questions.append(MultipleChoiceQuestion(question, options, correct))

    return questions

if __name__ == '__main__':
    questions = readFile('sporsmaalsfil.txt')

    player1_correct = 0
    player2_correct = 0

    for question in questions:
        print(question)

        player1_input = int(input("Velg et svaralternativ for spiller 1: "))
        player2_input = int(input("Velg et svaralternativ for spiller 2: "))

        print("\nKorrekt svar:", question.correct_answer_text(),'\n')
        
        if question.check_answer(player1_input):
            print("Spiller 1: Korrekt")
            player1_correct += 1
        else:
            print("Spiller 1: Feil")

        if question.check_answer(player2_input):
            print("Spiller 2: Korrekt")
            player2_correct += 1
        else:
            print("Spiller 2: Feil")
        print()

    print("-"*30)
    print("Total number of questions:", len(questions))
    print("Correctly answered by Player 1:", player1_correct)
    print("Correctly answered by Player 2:", player2_correct)
    print("-"*30)