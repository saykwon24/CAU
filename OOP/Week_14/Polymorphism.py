# Week 14 (1)

"""
Polymorphism: 'having multiple shapes'
              dynamic method lookup: method calls are always determined at run time based on the type of the actual object
                                     automatically select the method of the correct class
              this allows us to treat objects of different classes in a uniform way
              allows us to manipulate objects that share a set of tasks, even though the tasks are executed in diffrent ways
              e.g. a code block for object of superclass can also be applied to an object of subclass, but not vice versa


Subclass and Instances: isinstance function can also be used to determine if an object is an instance of a subclass
                        to verify that the arguments passed to a function or method are of the correct type
                        but, don't use this function for type test
                        because you need to revise all parts of your program when a new subclass is added
                        instead, use the Polymorphism: declare a method for this, then override it in the subclasses
    isinstance(object, type) | return True if the 'object' is an instance of the 'type' or any subclass of the 'type'
"""

## Superclass
class Question:
    def __init__(self):
        self._text = ""
        self._answer = ""
    
    def setText(self, questionText):
        self._text = questionText
    
    def setAnswer(self, correctResponse):
        self._answer = correctResponse
    
    def checkAnswer(self, response):
        return response == self._answer
    
    def display(self):
        print(self._text)
    
    # Dynamic method lookup
    def presentQuestion(self):
        self.display()
        response = input("Your answer: ")
        print(self.checkAnswer(response))

## Subclass
class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []
    
    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)
    
    def display(self):
        super().display()
        
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))


## Unit test
def main():
    first = Question()
    first.setText("Who was the inventor of Python?")
    first.setAnswer("Guido van Rossum")
    
    second = ChoiceQuestion()
    second.setText("In which country was the inventor of Python born?")
    second.addChoice("Australia", False)
    second.addChoice("Canada", False)
    second.addChoice("Netherlands", True)
    second.addChoice("United States", False)
    
    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(5)    # TypeError: integer is not a subclass of Question
    
    
    text = "In which year was Python first released?"
    answers = ['1991', '1995', '1998', '2000']
    correct = 0
    
    third = ChoiceQuestion()
    first.setText(text)
    addAllChoices(first, answers, correct)    # AttributeError: first is an object of Question, not ChoiceQuestion
    addAllChoices(third, answers, correct)    # Correct
    
    
    cq = ChoiceQuestion()
    cq.setText("In which country was the inventor of Python born?")
    cq.presentQuestion()    # ChoiceQuestion versions of the display and checkAnswer methods are called automatically
                            # because Question class(superclass) supplies a presentQuestion method that specifies the common nature to ChoiceQuestion(subclass)



## Some functions for main function
def presentQuestion(q):
    # Assume that programmer intended q is an object of Question class(superclass)
    # Verify the correct type of the object
    if not isinstance(q, Question):
        raise TypeError("The argument is not a Question or one of its subclasses")
    
    # Uses dynamic method lookup
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))


def addAllChoices(q, choices, correct):
    for i in range(len(choices[i])):
        if i == correct:
            q.addChoice(choices[i], True)
        else:
            q.addChoice(choices[i], False)


main()



"""
Abstract Class | contains at least one abstract method
Concrete Class | contains no abstract method

Abstract Method: a do-nothing method of superclass
                 this forces the implementors of subclasses to specify 'concrete' implementations of this method
                 i.e. forces the programmers to create subclass that specifies this method
                 in Python, no explicit way to specify that a method is an abstract method
                 instead, raise a 'NotImplementedError' exception to inform the method is the abstract method
"""