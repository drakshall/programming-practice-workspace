import os
import random
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.button import Button

os.chdir(os.path.dirname(os.path.abspath(__file__)))
Config.set('graphics', 'fullscreen', 'auto')

class SequenceApp(App):
    pass

class SequenceRoot(BoxLayout):
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

    def showFailPage(self):
        self.clear_widgets()
        self.add_widget(FailPage())

    def showSuccessPage(self):
        self.clear_widgets()
        self.add_widget(SuccessPage())

class MainMenuSelect(BoxLayout):
    pass

class InputNameForm(BoxLayout):
    nameInput = ObjectProperty()
    def recordName(self):
        print(self.nameInput.text) # input handling (might not be worthwhile)

class RulesPage(BoxLayout):
    pass

class LeaderboardPage(FloatLayout):
    listScores = ObjectProperty()
    def displayScores(self):
        leaderboardTemp = []
        filename = "sequenceleaderboard.txt"
        if not os.path.exists(filename):
            open(filename, 'w').close()
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    name, score = parts
                    leaderboardTemp.append({
                        'name': name,
                        'score': score
                    })
        leaderboardTemp.sort(key=lambda x: int(x['score']), reverse=True)
        list = self.listScores
        list.data = leaderboardTemp
        list.data = [{'text': f"{item['name']}: {item['score']}"} for item in leaderboardTemp]

class SequenceGame(FloatLayout):
    timerLabel = ObjectProperty()
    buttonContainer = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timeInt = 50
        self.filename = "sequence1.txt"
        self.buttonCount = 0
        self.levelCount = 1
        Clock.schedule_interval(self.timer, 1)
        self.randomiseButtons()
        
    def randomiseButtons(self):
        lineIndex = 0
        sequenceDict = {}
        with open(self.filename) as f:
            for line in f:
                line = line.strip()
                lineIndex += 1
                sequenceDict[lineIndex] = line

        widthHint = 0.1
        heightHint = 0.1
        maxX = 1 - widthHint
        maxY = 1 - heightHint
        tempIndex = 1
        for child in self.buttonContainer.children:
            child.pos_hint = {
                'x': random.uniform(0, maxX),
                'y': random.uniform(0, maxY)
            }
            child.text = sequenceDict[tempIndex]
            tempIndex += 1

    def timer(self, dt):
        self.timeInt -= 1
        print (self.timeInt)
        self.timerLabel.text = (f"{self.timeInt}")
        if self.timeInt == 0 and self.levelCount != 5:
            self.parent.showFailPage()
            return False
        elif self.levelCount == 5:
            return False

    def sequenceButton(self,btnID):
        self.buttonCount += 1
        print(self.buttonCount)
        print(btnID)
        if btnID == self.buttonCount:
            if self.buttonCount == 5:
                self.levelCount += 1
                if self.levelCount == 5:
                    self.parent.showSuccessPage()
                    self.timer
                else:
                    self.filename = f"sequence{self.levelCount}.txt"
                    self.buttonCount = 0
                    self.randomiseButtons()
            else:
                pass #make icon green
        else:
            self.buttonCount -= 1
            # make icon flash red




class FailPage(FloatLayout):
    pass

class SuccessPage(FloatLayout):
    pass # something to record time value & name value to file

if __name__ == '__main__':
    SequenceApp().run()
