import re
from calc_op import Calculator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class RootApplication(BoxLayout):
    def digit_click(self, value):
        """A digit was clicked on the numeric keyboard"""
        self.ids.edt_value.insert_text(value)


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super().insert_text(s, from_undo=from_undo)


class CalcApp(App):
    def build(self):
        return RootApplication()


if __name__ == "__main__":
    calcs = Calculator()
    CalcApp().run()
