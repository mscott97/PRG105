class Question:

    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, correct_answer):
        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__correct_answer = correct_answer

    def get_question(self):
        return self.__question

    def get_answer_1(self):
        return self.__answer_1

    def get_answer_2(self):
        return self.__answer_2

    def get_answer_3(self):
        return self.__answer_3

    def get_answer_4(self):
        return self.__answer_4

    def get_answer_5(self):
        return self.__answer_5

    def get_answer_6(self):
        return self.__answer_6

    def get_answer_7(self):
        return self.__answer_7

    def get_answer_8(self):
        return self.__answer_8

    def get_answer_9(self):
        return self.__answer_9

    def get_answer_10(self):
        return self.__answer_10


    def get_correct_answer(self):
        return self.__correct_answer

    def set_question(self, question):
        self.__question = question

    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    def __str__(self):
        return self.__correct_answer


def main():
    total = 0

    questions = {}

    question_1 = Question("How old is Sam Harris?", "30", "40", "50", "60", "50")
    question_2 = Question("What is the capital of California?", "Los Angeles", "Sacramento", "Pasadena", "Hollywood",
                          "Sacramento")

    questions[0] = question_1
    questions[1] = question_2
    questions[2] = questions_3
    questions[3] = questions_4
    questions[4] = questions_5
    questions[5] = questions_6
    questions[6] = questions_7
    questions[7] = questions_8
    questions[8] = questions_9
    questions[9] = questions_10

    for x in questions:
        print(questions[x].get_question())
        print("Here are the possible answers: ")
        print("1.", questions[x].get_answer_1())
        print("2.", questions[x].get_answer_2())
        print("3.", questions[x].get_answer_3())
        print("4.", questions[x].get_answer_4())
        print("5.", questions[x].get_answer_5())
        print("6.", questions[x].get_answer_6())
        print("7.", questions[x].get_answer_7())
        print("8.", questions[x].get_answer_8())
        print("9.", questions[x].get_answer_9())
        print("10.", questions[x].get_answer_10())
        answer = input("Please enter the number of your answer: ")

        while answer.isdigit() != True:
            answer = input("Please enter only the number: ")

        if answer == "1" and questions[x].get_answer_1() == questions[x].get_correct_answer():
            total += 1

        elif answer == "2" and questions[x].get_answer_2() == questions[x].get_correct_answer():
            total += 1

        elif answer == "3" and questions[x].get_answer_3() == questions[x].get_correct_answer():
            total += 1

        elif answer == "4" and questions[x].get_answer_4() == questions[x].get_correct_answer():
            total += 1

        elif answer == "5" and questions[x].get_answer_5() == questions[x].get_correct_answer():
            total += 1

        elif answer == "6" and questions[x].get_answer_6() == questions[x].get_correct_answer():
            total += 1

        elif answer == "7" and questions[x].get_answer_7() == questions[x].get_correct_answer():
            total += 1

        elif answer == "8" and questions[x].get_answer_8() == questions[x].get_correct_answer():
            total += 1

        elif answer == "9" and questions[x].get_answer_9() == questions[x].get_correct_answer():
            total += 1

        elif answer == "10" and questions[x].get_answer_10() == questions[x].get_correct_answer():
            total += 1


    print("The total number of correct answers is: ", total)


main()
