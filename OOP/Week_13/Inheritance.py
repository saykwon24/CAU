# Week 13 (3)

"""
Inheritance Hierarchies: means relationship between subclass and superclass
                         subclass inherits data and behavior(i.e. all instance variables and methods) from superclass
                         so only declare methods that are not part of the superclass objects, and can override some methods inherited from superclass
                         but, instance variables of superclass are 'private' to superclass
                         so only superclass methods should access its instance variables
                         therefore, subclass methods must use the 'public interface' of superclass
                         
                         constructor of subclass must explicitly call the superclass constructor using super() function
                         it should be called before the subclass defines its own instance variables
                         because instance variables of superclass would be used in that of subclass
                         if there are arguments in superclass constructor, they should be passed as well
                         
                         substitution principle: can always use a subclass object when a superclass object is expected
                         usually, is used to model objects with different behavior
                         that is, "single class for variation in values, inheritance for variation in behavior"


Overriding Method: can extend or replace the funtionality of the superclass method by specifying a new implementation in the subclass
                   whenever you call a superclass method from a subclass method with the same name, be sure to use super function in place of the self reference


class 'Object': superclass of every class in Python
                defines several very general methods
                __repr__ method can be overriden in user-defined class, and usually for use in 'debugging'
"""

## 1-1) Define a super class
# 
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
    
    # can override __repr__ method
    """def __repr__(self):
        return "Question[%s, %s]" % (self._text, self._answer)"""


## 1-2) Unit test for the superclass
def test1():
    "from questions import Question"    # assume Question class is in 'questions' program

    # Create the question and answer
    q = Question()
    print("Created object:", q)    # for use in debugging
    q.setText("Who is the investor of Python?")
    print("Added the text:", q)
    q.setAnswer("Guido van Rossum")
    print("Added the answer", q)

    # Display the question and obtain user's response
    q.display()
    response = input("Enter your answer: ")
    print(q.checkAnswer(response))

    # The superclass Object: diplay default __repr__ method
    first = Question()
    second = Question()
    print(repr(first))
    print(repr(second))

test1()


## 2-1) Form a subclass inherited from superclass
#
class ChoiceQuestion(Question):    # inherited from Question
    def __init__(self):            # subclass has its own constructor
        super().__init__()         # call the superclass constructor before initializing instance variables of subclass
        self._choices = []
    
    # Specific method of subclass; different behavior from superclass
    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            # Convert the length of the list to a string
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)
    
    # Overriden method that is already defined in superclass
    def display(self):
        # Display the question text
        super().display()    # the self parameter references an object of type ChoiceQuestion(subclass), not superclass
                             # written that way, the method would call itself over and over
                             # so instead of the self, use super function
        
        # Display the answer choices
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))


## 2-2) Unit test for the subclass
def test2():
    "from choicequestions import ChoiceQuestion"    # assume ChoiceQuestion class is in 'choicequestions' program
    
    first = ChoiceQuestion()
    first.setText("In what year was the Python language first released?")
    first.addChoice("1991", True)
    first.addChoice("1995", False)
    first.addChoice("1998", False)
    first.addChoice("2000", False)
    
    second = ChoiceQuestion()
    second.setText("In which country was the inventor of Python born?")
    second.addChoice("Australia", False)
    second.addChoice("Canada", False)
    second.addChoice("Netherlands", True)
    second.addChoice("Unitied States", False)
    
    presentQuestion(first)
    presentQuestion(second)

def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))

test2()