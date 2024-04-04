class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_options(self):
        for i in range(len(self.options)):
            print(f"{chr(65 + i)}. {self.options[i]}")
            
    def check_answer(self, user_choice):
        return user_choice.upper() == self.correct_answer


class MultipleChoiceQuestion(Question):
    def __init__(self, prompt, options, correct_answer):
        super().__init__(prompt, options, correct_answer)

    def display_options(self):
        super().display_options()


class TrueFalseQuestion(Question):
    def __init__(self, prompt, correct_answer):
        options = ["True", "False"]
        super().__init__(prompt, options, correct_answer)

    def display_options(self):
        print("A. True")
        print("B. False")


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            print(question.prompt)
            question.display_options()
            user_choice = input("Enter your choice (A, B, C, etc.): ")
            if question.check_answer(user_choice):
                print("Correct!")
                self.score += 1
                print(f"Your current score is {self.score}/{len(self.questions)}.")

            else:
                print("Incorrect!")
                print(f"Your current score is {self.score}/{len(self.questions)}.")

        print(f"Quiz Ended !!! Your final score is {self.score}/{len(self.questions)} .")

questions = [
    MultipleChoiceQuestion("What is the capital of France? ", ["London", "Paris", "Berlin", "Madrid"], "B"),
    MultipleChoiceQuestion("What is 2 + 2? ", ["3", "4", "5", "6"], "B"),
    MultipleChoiceQuestion("Which planet is known as the Red Planet? ", ["Mars", "Venus", "Mercury", "Saturn"], "A"),
    MultipleChoiceQuestion("Who wrote 'Romeo and Juliet'? ", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "B"),
    MultipleChoiceQuestion("What is the largest mammal in the world? ", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "B"),
    TrueFalseQuestion("The sun rises in the west. ", "B"),
    TrueFalseQuestion("Water boils at 100 degrees Celsius at sea level. ", "A")
]

quiz = Quiz(questions)
quiz.run_quiz()

percentage_correct = (quiz.score / len(questions)) * 100
print(f"Percentage of correct answers: {percentage_correct:.2f}%")