import os
import random
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.button import Button

os.chdir(os.path.dirname(os.path.abspath(__file__)))                                            # Sets the default file path to the directory where the files are present.
#Config.set('graphics', 'fullscreen', 'auto')                                                    # Ensures the program launched in fullscreen

class SequenceApp(App):                                                                         # App root, when called by the python file loads the associated kivy file.
    pass

class SequenceRoot(BoxLayout):                                                                  # Screen orchestrator class, handles the clearing & loading of widgets.
    def showNameForm(self):
        self.clear_widgets()  
        self.add_widget(InputNameForm())

    def showLeaderboard(self):
        self.clear_widgets()
        self.add_widget(LeaderboardPage())

    def showHome(self):
        self.clear_widgets()
        self.add_widget(MainMenuSelect())

    def showRules(self):
        self.clear_widgets()
        self.add_widget(RulesPage())
    
    def showSequenceGame(self):
        self.clear_widgets()
        self.add_widget(SequenceGame())

    def showFail(self):
        self.clear_widgets()
        self.add_widget(FailPage())

    def showSuccess(self):
        self.clear_widgets()
        self.add_widget(SuccessPage())

class MainMenuSelect(BoxLayout):                                                                # No logic because changing screens is handled by previous class.
    pass                                                                                        # Layout defined in kivy file.

class InputNameForm(BoxLayout):                                                                 # Takes user inputed name, ensures it adheres to length rules, then stores
    nameInput = ObjectProperty()                                                                # the string in the 'nameBearer' variable with the SequenceRoot class. 
    def recordName(self):                                                                       # As the orchestration layer the instance of SequenceRoot is never cleared 
        if 1 <= len(self.nameInput.text) <= 3:                                                  # in the way its children widgets are which allows it to store variables 
            self.parent.nameBearer = self.nameInput.text                                        # for the duration of the program runtime.
            self.parent.showRules()
        
class RulesPage(BoxLayout):
    pass

class LeaderboardPage(FloatLayout):                                                             # Displays a sorted list of user scores.   
    listScores = ObjectProperty()                                                               # Variables are passed between kivy and python using the ObjectProperty
    def displayScores(self):                                                                    # class rather than direct referencing to better seperate out logic
        leaderboardArray = []                                                                   # and structure concerns.
        with open("sequenceLeaderboard.txt") as f:                                              # Reads leaderboard information from file, splits each line and
            for line in f:                                                                      # arranges the elements into a single entry dictionary formatted for
                line = line.strip()                                                             # the kivy RecycleView widget. Those dicts are loaded into an array
                name, score = line.split(',')                                                   # and sorted by their score value before being passed to the widget.
                leaderboardArray.append({'text': f"{name}: {score}"})
        leaderboardArray.sort(key=lambda x: int(x['text'].split(':')[1].strip()), reverse=True) # Used python's inbuilt sorting method because its the fastest available.
        self.listScores.data = leaderboardArray

class SequenceGame(FloatLayout):                                                                # Main class handling game mechanics.
    timerLabel = ObjectProperty()
    buttonContainer = ObjectProperty()
    buttonCountLabel = ObjectProperty()

    def __init__(self, **kwargs):                                                               # Initialises relevant variables on page load.
        super().__init__(**kwargs)
        self.timeInt = 50                                                                       # Determines length of game timer.
        self.filename = "sequence1.txt"
        self.buttonCount = 0
        self.levelCount = 1
        Clock.schedule_interval(self.timer, 1)                                                  # Begins the timer, executes code from timer method for each time interval (1 second).
        self.randomiseButtons()                                                                 # Calls method that randomises the position of the sequence buttons.
        
    def randomiseButtons(self):
        sequenceDict = {}
        with open(self.filename) as f:
            for i, line in enumerate(f):
                sequenceDict[i] = line.strip()                                                  # Loads the sequence data stored in text files and indexes them by their line index.
        widthH = 0.2                                        
        heightH = 0.1
        maxX = 1 - widthH
        maxY = 1 - heightH                                                                      # Ensures generated box placements dont clip off-screen.
        buttons = list(self.buttonContainer.children)                                           # Compiles the children button widgets of the buttonContainer into an array.
        ButtonPositions = []  
        for j, child in enumerate(buttons):                     
            for r in range(1000):                                                               # Iterates through each button in buttonContainer up to 1000 times randomly selecting
                x = random.uniform(0, maxX)                                                     # positions until one that isnt occupied by another button is found.
                y = random.uniform(0, maxY) 
                overlap = False
                for (px, py) in ButtonPositions:
                    if self.overlapCheck(x, y, widthH, heightH, px, py, widthH, heightH):       # Calls overlap checker method to compare the corner positions of the current iteration's
                        overlap = True                                                          # buttons to the corner positions of each previously placed button.
                        break                                                                   
                if not overlap:
                    ButtonPositions.append((x, y))                                              # Stores button position co-ords in a list for future comparison.
                    child.pos_hint = {'x': x, 'y': y}                                           # Places button at the randomised, non-colliding co-ords.
                    break
            child.text = sequenceDict.get(j, "?")                                               # Assigns appropriately ordered sequence data to the buttons by using the buttonContainer
                                                                                                # index as the sequenceDict key, thus matching the button IDs with the sequence order.
    def overlapCheck(self, x1, y1, w1, h1, x2, y2, w2, h2):                                         
        if x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:                     # Compares corner co-ordinates of two buttons, if all conditions are true the icons overlap
            return True
        else:
            return False                       

    def timer(self, dt):                                                                        # Method called every second by the clock object.
        self.timeInt -= 1                                                                       # Subtracts time integer by 1 every 1 second cycle.
        self.timerLabel.text = (f"{self.timeInt}")                                              # Updates the timer display with the new time after each cycle.
        if self.timeInt == 0 and self.levelCount != 5:                                          # Checks if the timer reaches 0 before the final level is over and ends the game if so.
            self.parent.showFail()                                                              
            return False                                                                        # Returning false stops the clock.
        elif self.levelCount == 5:                                                              # Checks if the final level has been reached, if so ends the timer.
            return False

    def sequenceButton(self,btnID):                                                             # Method triggered on every button press, button ID number passed from kivy file.
        self.buttonCount += 1                                                                   # Temporarily increments button count (number of correct guesses + 1).
        if btnID == self.buttonCount:                                                           # Compares the button count to the button ID, if they match the incremented value is displayed
            self.buttonCountLabel.text = (f"{self.buttonCount}")                                # as the number of correct guesses on the screen, otherwise button count is decremented.
            if self.buttonCount == 5:                                                           
                self.levelCount += 1                                                            # If the last button in the sequence is pressed the level count is incremented, and if that
                if self.levelCount == 5:                                                        # was the last level the user's name and score are recorded to the leaderboard and the user
                    nameBearer = self.parent.nameBearer                                         # is shown the victory screen.
                    with open("sequenceLeaderboard.txt", "a") as file:
                        file.write(f"{nameBearer},{self.timeInt}\n") 
                    self.parent.showSuccess()
                else:                                                                           # However if it was not the final level then the next sequence data file is loaded and
                    self.filename = f"sequence{self.levelCount}.txt"                            # relevant conditions are reset.
                    self.buttonCount = 0
                    self.buttonCountLabel.text = (f"{self.buttonCount}")
                    self.randomiseButtons()
            else:
                pass
        else:
            self.buttonCount -= 1

class FailPage(FloatLayout):
    pass

class SuccessPage(FloatLayout):                                                                 
    winnerMessage = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.displayWinnerMessage()                                                             # Calls method on page load.

    def displayWinnerMessage(self):                                                             # Extracts the user's score and name as the final entries from the leaderboard file
        with open("sequenceLeaderboard.txt", "r") as f:                                         # and applies them to the victory message widget text.
            lines = f.readlines()
            lastLine = lines[-1].strip()
            name, score = lastLine.split(',')
        self.winnerMessage.text = f"{name} your score was {score}" 
        pass 

    
if __name__ == '__main__':
    SequenceApp().run()
