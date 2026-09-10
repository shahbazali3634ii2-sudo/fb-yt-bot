import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import schedule

class BotApp(BoxLayout):
    def __init__(self, **kwargs):
        super(BotApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(text='[b]Multi-Platform Auto Bot[/b]', markup=True, font_size=24))

        self.add_widget(Label(text='Upload Time (e.g., 21:40 for 9:40 PM):'))
        self.time_input = TextInput(text='21:40', multiline=False, font_size=18)
        self.add_widget(self.time_input)

        self.status_label = Label(text='Status: Waiting for action...', font_size=16)
        self.add_widget(self.status_label)

        self.sched_btn = Button(text='Start Scheduled Upload', background_color=(0.1, 0.6, 0.1, 1))
        self.sched_btn.bind(on_press=self.start_scheduler)
        self.add_widget(self.sched_btn)

        self.test_btn = Button(text='Test Upload Now', background_color=(0.1, 0.4, 0.8, 1))
        self.test_btn.bind(on_press=self.test_upload)
        self.add_widget(self.test_btn)

    def run_bot_task(self):
        self.status_label.text = 'Status: Processing Video...'
        try:
            time.sleep(3) 
            self.status_label.text = 'Status: Video Successfully Uploaded!'
        except Exception as e:
            self.status_label.text = f'Status Error: {str(e)}'

    def job(self):
        self.run_bot_task()

    def scheduler_loop(self, target_time):
        schedule.clear()
        schedule.every().day.at(target_time).do(self.job)
        self.status_label.text = f'Status: Scheduled for {target_time} daily.'
        
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_scheduler(self, instance):
        t_str = self.time_input.text.strip()
        threading.Thread(target=self.scheduler_loop, args=(t_str,), daemon=True).start()

    def test_upload(self, instance):
        threading.Thread(target=self.run_bot_task, daemon=True).start()

class MainApp(App):
    def build(self):
        return BotApp()

if __name__ == '__main__':
    MainApp().run()
