#Character Class

class Character(object):
    """ character class """
    def __init__(self):
        self.n = 0
        self.q = [
            {'Question' : 'What town is Stranger Things set in?' , 'Answers' : 'Hawkins, Hooveville' , 'Correct' : 'Hawkins' },
            {'Question' : 'What decade is it placed in?', 'Answers' : "1980's, 1970's", 'Correct' : "1980's" }
            ]

    def advance(self):
        print("You succeeded, move forward.")
        self.n += 1
    def died(self):
        print("You chose wrong and died.")
    def won(self):
        print("Finally, you remember where the gate to the Upside Down is. You have won the game.")
    def get_question(self):
        print(self.q[0]['Question'])
        for answer in print(self.q[self.n]['Answers']):
            print(answer)
        if input(">>>>") == self.q[self.n]['Correct']:
            self.advance
        else:
            self.died
c= Character()
while c.n < len(c.q):
    c.get_question

if c.n == len(c.q):
    c.won




#create a dictionary
#question:
    #answer:
        #correct answer:
