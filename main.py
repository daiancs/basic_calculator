import re
from calc_op import Calculator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class RootApplication(BoxLayout):
    new_input_value = True

    def digit_click(self, value):
        """A digit was clicked on the numeric keyboard"""
        if self.new_input_value:
            self.ids["edt_value"].text = ""
            self.new_input_value = False

        self.ids.edt_value.insert_text(value)

    def plus_minus(self):
        """Multiply value on input by -1"""
        if self.ids.edt_value.text:
            temp_value = float(self.ids.edt_value.text) * -1
            if temp_value == int(temp_value):
                self.ids["edt_value"].text = str(int(temp_value))
            else:
                self.ids["edt_value"].text = str(temp_value)

    def do_calc(self, operation):
        """Make the operation selected"""
        if self.ids.edt_value.text:
            result = calcs.operation(self.ids.edt_value.text, operation)
            self.new_input_value = True
            if result:
                if calcs.memvalue == int(calcs.memvalue):
                    self.ids["edt_value"].text = str(int(calcs.memvalue))
                else:
                    self.ids["edt_value"].text = str(calcs.memvalue)

    def clear_entry(self):
        """Clear the input text field"""
        self.ids["edt_value"].text = ""
        self.new_input_value = True

    def clear(self):
        """Clear the input text and the calc memory.
        As if it has reset the calculator to the initial state."""
        self.clear_entry()
        calcs.clear()


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
