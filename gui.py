import pyglet
import random

global violet
violet = (29, 15, 27, 200)

class BaseWindow:
	def draw(self): raise NotImplementedError
	
class TitleWindow(BaseWindow):
	def __init__(self): #parang initialize??
		self.introscreen = pyglet.image.load_animation("graphics/intro-screen.gif")
		self.introsprite = pyglet.sprite.Sprite(self.introscreen)
		self.introsprite.scale = 0.75

	def draw(self):
		self.introsprite.draw()

class OptionsWindow(BaseWindow):
	def __init__(self):
		self.options = pyglet.image.load("graphics/options.png")
		self.optionssprite = pyglet.sprite.Sprite(self.options)
		self.optionssprite.scale = 0.75

	def draw(self):
		self.optionssprite.draw()

class InstructionsWindow(BaseWindow):
	def __init__(self):
		self.instructions = pyglet.image.load_animation("graphics/how-to-play.gif")
		self.howtosprite = pyglet.sprite.Sprite(self.instructions)
		self.howtosprite.scale = 0.75

	def draw(self):
		self.howtosprite.draw()	

class InputWindow(BaseWindow):
	def __init__(self):
		self.fills = open('fill.txt', 'r').readlines() #list ng lahat ng fills
		self.randomfill = random.choice(self.fills) #outputs string ng isang fill
		self.position = self.fills.index(self.randomfill) #index ng fill (para makuha yung sa same index galing sa template)
		self.rfill = self.randomfill.split(',') #outputs list ng mga noun,adjective, etc. to be displayed na
		self.maximum = len(self.rfill)

		self.counter = 0
		self.bg = pyglet.image.load("graphics/bg.png")
		self.bgsprite = pyglet.sprite.Sprite(self.bg)
		self.bgsprite.scale = 0.75
		self.label = pyglet.text.Label('Input {0}'.format(self.rfill[self.counter]),
						font_name='Helsinki',
						x=480, y=480,
						font_size=26,
						anchor_x='center',anchor_y='center',
						color = violet)

		self.holder = pyglet.text.Label('',
						font_name='Helsinki',
						x=480, y=360,
						font_size=48,
						anchor_x='center',anchor_y='center',
						color = violet)

	def draw(self):
		self.bgsprite.draw()
		self.label.draw() 
		self.holder.draw()
		self.label.text = 'Input {0}'.format(self.rfill[self.counter])

class StoryWindow(BaseWindow):
	def __init__(self):
		self.bg = pyglet.image.load_animation("graphics/enter.gif")
		self.bgsprite = pyglet.sprite.Sprite(self.bg)
		self.bgsprite.scale = 0.75

	def draw(self):
		self.bgsprite.draw()

class EndWindow(BaseWindow):
	def __init__(self):
		self.bg = pyglet.image.load("graphics/bg.png")
		self.bgsprite = pyglet.sprite.Sprite(self.bg)
		self.bgsprite.scale = 0.75

		self.sublabel = pyglet.text.Label('Your story is ready!',
						font_name='Helsinki',
						font_size=48,
						x =480, y=600,
						anchor_x='center', anchor_y='center',
						width = 720, multiline = True,
						color = violet)

		#try:
		self.output = open('yourstory.txt', 'r').readlines()
		for x in self.output:
			storyy = x.strip()
		self.printing = storyy
		self.story = pyglet.text.Label("{}".format(self.printing),
						font_name = 'Gotham Book',
						font_size = 20,
						x = 480, y = 300,
						anchor_x = 'center', anchor_y = 'center',
						width = 720,
						multiline = True,
						align = 'center',
						color = violet)
		#except FileNotFoundError:
		#	pass

	def draw(self):
		self.bgsprite.draw()
		self.sublabel.draw()
		#try:
		self.story.draw()
		#except AttributeError:
		#	pass