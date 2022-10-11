import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
	#txt = random.Random(10)
	def build(self):
		main_layout = BoxLayout(orientation='vertical', padding = 1,spacing = 1)
		layout = BoxLayout(orientation='horizontal', padding = 10,spacing = 10,
						   size_hint=(1, .1),
						   #size=(100,70)
						   )

		#BoxLayout(cols = 2, rows = 1, row_force_default = True, row_default_height = 40,
		#					spacing = 10, padding = 10)
		self.fr = TextInput(text = "0", size_hint=(1, 1),  pos_hint={"left": 0.9, "center_y": 0.5})
		self.to = TextInput(text="10", size_hint=(1, 1), pos_hint={"right": 0.9, "center_y": 0.5})
		#submit = Button(text ='Submit', on_press = self.submit)
		layout.add_widget(self.fr)
		layout.add_widget(self.to)
		#layout.add_widget(submit)
		main_layout.add_widget(layout)
		#boxlay = BoxLayout(orientation='vertical')
		btn = Button(text="Запуск генерации чисел", font_size=46,
					 on_press=self.btn_press,
					 on_release=self.btn_release,
					 #background_color=[.22, .12, .30, 1],
					 background_color=[0, 0, 0, 1],
					 background_normal='',
					 pos_hint={"center_x": 0.5, "center_y": 0.1}
					# ,					 size_hint_x=None, width=300
					 )
		main_layout.add_widget(btn)
		return main_layout

	def submit(self,obj):
		print("from = " + self.fr.text)
		print("from = " + self.to.text)

	def btn_press(self, instance):
		# print('The button <%s> is being pressed' )
		instance.text = "Жмяк!"

	def btn_release(self, instance):
		#str_numbers = str(random.randrange(int(self.fr.text), int(self.to.text), 1))
		#str_numbers = str_numbers[:2]+' '+str_numbers[2:4]+' '+str_numbers[4:6]
		str_numbers = str(random.randrange(int(self.fr.text), int(self.to.text), 1)).rjust(2,"0")
		str_numbers = str_numbers + ' ' +str(random.randrange(int(self.fr.text), int(self.to.text), 1)).rjust(2,"0")
		str_numbers = str_numbers + ' ' + str(random.randrange(int(self.fr.text), int(self.to.text), 1)).rjust(2,"0")
		instance.text = str_numbers

if __name__== "__main__":
	MyApp().run()