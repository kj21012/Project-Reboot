from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    
    def on_enter(self):
        Clock.schedule_once(self.switch, 3)

    def switch(self, *args):
        self.manager.current = "second"


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

Builder.load_string("""
#:kivy 1.11.0
           
WindowManager:
    MainWindow:
        id: 'main'
    SecondWindow:
        id: 'second'
        
<MainWindow>:
    name: "main"
    # Anchor Layout 1 
    AnchorLayout: 
          
        # position of Anchor Layout  
        anchor_x: 'center'
        anchor_y: 'center'
  
        # creating Canvas  
        canvas: 
            Color: 
                rgb: [1, 1, 1] 
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'Splash.png'
  
  
<SecondWindow>:
    name: "second"
    Button:
        text: "Go Back"
        on_release:
            root.manager.current = "main"
            root.manager.transition.direction = "right"
""")


sm = WindowManager()
screens = [Screen(name='Title {}'.format(i)) for i in range(3)]
sm.add_widget(MainWindow(name='main'))
sm.add_widget(SecondWindow(name='second'))
# later


class mainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    mainApp().run()