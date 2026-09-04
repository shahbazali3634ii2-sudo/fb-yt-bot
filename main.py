from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class BotControlPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(BotControlPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        # Title
        self.add_widget(Label(text='[b]FB & YT Automation Bot[/b]', markup=True, font_size='22sp', size_hint_y=None, height=50))

        # YouTube Link Input
        self.add_widget(Label(text='Enter YouTube Video Link:', font_size='14sp', size_hint_y=None, height=30))
        self.yt_link_input = TextInput(text='', hint_text='https://youtube.com/...', multiline=False, size_hint_y=None, height=45)
        self.add_widget(self.yt_link_input)

        # Platform Connect Buttons
        self.add_widget(Label(text='Account Connections:', font_size='14sp', size_hint_y=None, height=30))
        
        self.fb_btn = Button(text='Continue with Facebook', background_color=(0.1, 0.4, 0.8, 1), size_hint_y=None, height=45)
        self.fb_btn.bind(on_press=self.connect_facebook)
        self.add_widget(self.fb_btn)

        self.tt_btn = Button(text='Continue with TikTok', background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=45)
        self.tt_btn.bind(on_press=self.connect_tiktok)
        self.add_widget(self.tt_btn)

        # Video Format Selection (Long / Reel Parts)
        self.add_widget(Label(text='Select Video Format / Split Parts:', font_size='14sp', size_hint_y=None, height=30))
        self.format_spinner = Spinner(
            text='Long Video (Full)',
            values=('Long Video (Full)', 'Reel / Short (Auto Parts 1, 2, 3...)'),
            size_hint_y=None, height=45
        )
        self.add_widget(self.format_spinner)

        # Upload Target Selection
        self.add_widget(Label(text='Upload Destination:', font_size='14sp', size_hint_y=None, height=30))
        self.target_spinner = Spinner(
            text='Facebook Only',
            values=('Facebook Only', 'TikTok Only', 'All Platforms (FB + TikTok)'),
            size_hint_y=None, height=45
        )
        self.add_widget(self.target_spinner)

        # Time Schedule Input
        self.add_widget(Label(text='Schedule Time (HH:MM):', font_size='14sp', size_hint_y=None, height=30))
        self.time_input = TextInput(text='12:00', hint_text='e.g., 14:30', multiline=False, size_hint_y=None, height=45)
        self.add_widget(self.time_input)

        # Start Automation Button
        self.start_btn = Button(text='Start Automated Upload', background_color=(0.1, 0.7, 0.3, 1), size_hint_y=None, height=50)
        self.start_btn.bind(on_press=self.start_automation)
        self.add_widget(self.start_btn)

        # Status Label
        self.status_label = Label(text='Status: Ready', font_size='14sp', size_hint_y=None, height=40)
        self.add_widget(self.status_label)

    def connect_facebook(self, instance):
        self.status_label.text = 'Status: Facebook Account Linked Successfully!'

    def connect_tiktok(self, instance):
        self.status_label.text = 'Status: TikTok Account Linked Successfully!'

    def start_automation(self, instance):
        link = self.yt_link_input.text
        target = self.target_spinner.text
        fmt = self.format_spinner.text
        sched_time = self.time_input.text
        
        if not link:
            self.status_label.text = 'Error: Please enter a YouTube link!'
        else:
            self.status_label.text = f'Scheduled for {sched_time} on {target}!'

class FBYouTubeBotApp(App):
    def build(self):
        return BotControlPanel()

if __name__ == '__main__':
    FBYouTubeBotApp().run()
