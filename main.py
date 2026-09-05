from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle

class AIAutomatorDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super(AIAutomatorDashboard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 12

        # Background color setting for AI dark theme look
        with self.canvas.before:
            Color(0.08, 0.09, 0.12, 1) # Dark AI background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # App Title / AI Header
        title = Label(
            text='[b]🤖 AI SOCIAL AUTOMATOR[/b]', 
            markup=True, 
            font_size='20sp', 
            size_hint_y=None, 
            height=40,
            color=(0, 0.8, 1, 1)
        )
        self.add_widget(title)

        # 1. Select Source Platform Spinner
        self.add_widget(Label(text='Select Source Platform:', font_size='13sp', size_hint_y=None, height=25, color=(0.8, 0.8, 0.8, 1)))
        self.source_spinner = Spinner(
            text='Select Source',
            values=('YouTube', 'TikTok', 'Facebook', 'Instagram'),
            size_hint_y=None, height=45
        )
        self.source_spinner.bind(text=self.on_source_select)
        self.add_widget(self.source_spinner)

        # 2. Link Input Box (Changes hint dynamically)
        self.link_input = TextInput(
            text='', 
            hint_text='Paste link here...', 
            multiline=False, 
            size_hint_y=None, 
            height=45
        )
        self.add_widget(self.link_input)

        # 3. Continue Account Buttons
        self.add_widget(Label(text='Account Connections:', font_size='13sp', size_hint_y=None, height=25, color=(0.8, 0.8, 0.8, 1)))
        
        self.tt_btn = Button(text='Continue with TikTok', background_color=(0.1, 0.1, 0.1, 1), size_hint_y=None, height=40)
        self.tt_btn.bind(on_press=lambda x: self.update_status("TikTok Connected!"))
        self.add_widget(self.tt_btn)

        self.fb_btn = Button(text='Continue with Facebook', background_color=(0.1, 0.3, 0.7, 1), size_hint_y=None, height=40)
        self.fb_btn.bind(on_press=lambda x: self.update_status("Facebook Connected!"))
        self.add_widget(self.fb_btn)

        self.yt_btn = Button(text='Continue with YouTube', background_color=(0.8, 0.1, 0.1, 1), size_hint_y=None, height=40)
        self.yt_btn.bind(on_press=lambda x: self.update_status("YouTube Connected!"))
        self.add_widget(self.yt_btn)

        self.ig_btn = Button(text='Continue with Instagram', background_color=(0.7, 0.1, 0.4, 1), size_hint_y=None, height=40)
        self.ig_btn.bind(on_press=lambda x: self.update_status("Instagram Connected!"))
        self.add_widget(self.ig_btn)

        # 4. Select Time Input
        self.add_widget(Label(text='Select Upload Time (HH:MM):', font_size='13sp', size_hint_y=None, height=25, color=(0.8, 0.8, 0.8, 1)))
        self.time_input = TextInput(text='12:00', hint_text='HH:MM', multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.time_input)

        # 5. Choose Video Format (Long Video with 1-min parts / Short)
        self.add_widget(Label(text='Choose Video Type / Parts:', font_size='13sp', size_hint_y=None, height=25, color=(0.8, 0.8, 0.8, 1)))
        self.format_spinner = Spinner(
            text='Long Video (Auto 1-min Parts)',
            values=('Long Video (Auto 1-min Parts)', 'Short / Reel (Single)'),
            size_hint_y=None, height=45
        )
        self.add_widget(self.format_spinner)

        # Action Button
        self.action_btn = Button(text='⚡ Start AI Automation', background_color=(0.1, 0.7, 0.3, 1), size_hint_y=None, height=45)
        self.action_btn.bind(on_press=self.start_bot)
        self.add_widget(self.action_btn)

        # Status Display
        self.status_label = Label(text='Status: System Ready', font_size='13sp', size_hint_y=None, height=35, color=(0, 1, 0.5, 1))
        self.add_widget(self.status_label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_source_select(self, spinner, text):
        self.link_input.hint_text = f'Paste {text} link here...'
        self.status_label.text = f'Source selected: {text}'

    def update_status(self, msg):
        self.status_label.text = msg

    def start_bot(self, instance):
        link = self.link_input.text
        if not link:
            self.status_label.text = 'Error: Please enter a link first!'
        else:
            self.status_label.text = 'Task Queued! Processing 1-min parts...'

class AIApp(App):
    def build(self):
        return AIAutomatorDashboard()

if __name__ == '__main__':
    AIApp().run()
    
