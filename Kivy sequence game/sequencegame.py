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
    
    def showSequenceGame1(self):
        self.clear_widgets()
        self.add_widget(SequenceGame1())

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
        print(self.nameInput.text)

class RulesPage(BoxLayout):
    pass

class LeaderboardPage(FloatLayout):
    listScores = ObjectProperty()
    def displayScores(self):
        leaderboardTemp = []
        filename = "sequenceleaderboard.txt"
        if not os.path.exists(filename):
            open(filename, 'w').close()
        with open("sequenceleaderboard.txt") as f:
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

class SequenceGame1(FloatLayout):
    timerLabel = ObjectProperty()
    buttonContainer = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timeInt = 50
        Clock.schedule_interval(self.timer, 1)
        self.randomiseButtons()
        
    def randomiseButtons(self):
        widthHint = 0.1
        heightHint = 0.1
        maxX = 1 - widthHint
        maxY = 1 - heightHint
        for child in self.buttonContainer.children:
            child.pos_hint = {
                'x': random.uniform(0, maxX),
                'y': random.uniform(0, maxY)
            }

    def timer(self, dt):
        self.timeInt -= 1
        print (self.timeInt)
        self.timerLabel.text = (f"{self.timeInt}")
        if self.timeInt == 0:
            self.parent.showFailPage()
            return False

    def sequenceButton(self):
        pass



class FailPage(BoxLayout):
    pass

class SuccessPage(BoxLayout):
    pass

if __name__ == '__main__':
    SequenceApp().run()
