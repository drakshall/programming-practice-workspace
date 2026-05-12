from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

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

class MainMenuSelect(BoxLayout):
    pass

class InputNameForm(BoxLayout):
    nameInput = ObjectProperty()
    def recordName(self):
        print(self.nameInput.text)

class RulesPage(BoxLayout):
    pass

class LeaderboardPage(BoxLayout):
    listScores = ObjectProperty()
    def displayScores(self):
        leaderboardTemp = []
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

class SequenceGame1(BoxLayout):
    pass

if __name__ == '__main__':
    SequenceApp().run()