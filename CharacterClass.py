

#Character Class

# Description for player and rules
print("You have woken up in the Upside Down. Clouds of dusts and darkness surround you. You hear the sound of a screeching monster and begin to run. The only way to survive is to answer the next series of questions correctly; if not you die. Good luck! ")
class Character(object):
    """ character class """
    #initialize the character class an sets self to 0 so the player starts from the beginning

    def __init__(self):
        self.n = 0
        #list of dictionaries
        #dictionary includes the question that the player is asked, with a list of answers to chooes from and with the correct answer

        self.q = [
            {'Question' : 'What town is Stranger Things set in?' , 'Answers' : ['Hawkins', 'Hooveville'] , 'Correct' : 'hawkins' },
            {'Question' : 'What decade is it placed in?', 'Answers' : ["1980's", "1970's"] , 'Correct' : "1980's" },
            {'Question' : "Where does season one's opening take place?", "Answers" : ["The Byer's House" , "The Laboratory"], 'Correct' : "the laboratory"},
            {'Question' : "How many episodes does season 1 consist of?", "Answers" : ["12","8"] , 'Correct' : "8"},
            {'Question' : "What game do the kids play often in the show?" , 'Answers' : ["Dungeons and Dragons","Pac-Man"] , 'Correct' : "dungeons and dragons" },
            {'Question' : "What is the name of the girl with the telekensis powers?" , 'Answers' : ["Eleven","Eight"] , 'Correct' : "eleven" },
            {'Question' : "What are El's favorite food?" , 'Answers' : ["Twinkies","Eggos"] , 'Correct' : "eggos" },
            {'Question' : "Which character goes missing in the beginning?" , 'Answers' : ["Will","Barb"] , 'Correct' : "will" },
            {'Question' : "Who is Nancy's best friend?" , 'Answers' : ["Steve","Barb"] , 'Correct' : "barb" },
            {'Question' : "Which actress plays Will's mom?" , 'Answers' : ["Katie McGrath","Winona Ryder"] , 'Correct' : "winona ryder" },
            {'Question' : "What is the name of the terrible, faceless creature?" , 'Answers' : ["Dementors","Demogorgan"] , 'Correct' : "demogorgan" },
            {'Question' : "What is the rural area eleven and the boys use called?" , 'Answers' : ["Mirkwood","Backroad"] , 'Correct' : "backroad" },
            {'Question' : "What is Will's mom name?" , 'Answers' : ["Joyce","Nancy"] , 'Correct' : "joyce" },
            {'Question' : "How does Joyce comminucate with Will when he is in the upside down?" , 'Answers' : ["Walkie talkie","Christmas Lights"] , 'Correct' : "christmas lights" } ,
            {'Question' : "Who is Nancy's boyfriend?", "Answers" : ["Steve","Jonathan"], "Correct" : "steve" },
            {'Question' : "What does Jonathan give Will while he is recovering?", "Answers" : ["A movie ticket to see 'Poltergeist'","A mixtape"], "Correct" : "a mixtape" },
            {'Question' : "Who is the character with the red hair?", "Answers" : ["Mad Max","Kali"], "Correct" : "mad max" },
            {'Question' : "What is another name for the Shadow Monster?", "Answers" : ["The Mind Flayer","Demagorgan"], "Correct" : "the mind flayer" },
            {'Question' : "What is the game the boys play in the arcade?", "Answers" : ["Pac-man","Dig Dug"], "Correct" : "dig dug" },
            {'Question' : "Who is Billy?", "Answers" : ["Mad Max's stepbrother","Mad Max's brother"], "Correct" : "mad max's stepbrother" },
            {'Question' : "Finish the quote. 'She can't resist these ____ '", "Answers" : ["pearls","skills"], "Correct" : "pearls" },
            {'Question' : "What does Mad Max ride?", "Answers" : ["skateboard","bike"], "Correct" : "skateboard" },
            {'Question' : "What do the boys dress up as for Halloween?", "Answers" : ["Dungeons and Dragons' characters","Ghostbusters"], "Correct" : "ghostbusters" },
            {'Question' : "Who does Lucas go with to the dance?", "Answers" : ["El","Max"], "Correct" : "max" },
            {'Question' : "Who dances with Dustin at the dance?", "Answers" : ["Max","Nancy"], "Correct" : "nancy" },
            {'Question' : "What is the sheriff's name?", "Answers" : ["Hopper","Lively"], "Correct" : "hopper" },
            {'Question' : "Who is Kali?", "Answers" : ["El's sister ","El's friend"], "Correct" : "el's friend" },
            {'Question' : "What is Bob's Haloween costume?", "Answers" : ["Superman","Count Dracula"], "Correct" : "count dracula"},
            {'Question' : "Where is the Gate to the Upside Down?", "Answers" : ["In the underground tunnels beneath the Pumpkin Patch","At Hawkin's Lab"], "Correct" : "at hawkin's lab"},
            ]

    #allows the player to go onto the next question in the game and gives the user the message below if they get the question right
    def advance(self):
        print("You succeeded, move forward.")
        self.n += 1

    #the function that is called if the user chose and invalid or wrong answer
    def died(self):
        print("Game Over. You chose wrong and died.")
        #the code below applies if the above is true and the player gets the question wrong
        #it ends the game by going to the end of the list/length of questions and adding another index which ends the game
        self.n = len(self.q) + 1

    #this function is called if the player answers everything correctly
    def won(self):
    #give the user this message indicating they have won the game
        print("Finally, you remember where the gate to the Upside Down is. You have won the game.")

    #this function will give the user a question from the list
    def get_question(self):
    #print the question from the list
        print(self.q[self.n]['Question'])
        #print the answer choices in the list
        for answer in self.q[self.n]['Answers']:
            print(answer)
       # print(self.q[self.n]['Correct'])
            #allows the user to input an answer based on the answer choices
            # .lower() allows them to input answers and have it accounted as correct despite capitalization
        if input(">>>>").lower() == self.q[self.n]['Correct']:
        #an if statement where if what the user entered matches the correct answer in the dictionary then it calls the advance function and allows the user to proceed
            self.advance()
        else:
        #if the user inputs an invalid or wrong answer, it will then call the died function
            self.died()

#variable for the character class so it is easily accessible
c= Character()

#while loop for when the index is less than the length of the question
while c.n < len(c.q):
    #calls the get question function to produce the next question in the list for the user to input
    c.get_question()

#if statement for when the user reaches the end of the list/last question successfully
if c.n == len(c.q):
    #calls the won function
    c.won()