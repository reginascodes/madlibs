import pyglet
from pyglet.window import key
import gui
import random

window = pyglet.window.Window(width=960, height=720)
current_screen = None
title_screen = gui.TitleWindow()
options_screen = gui.OptionsWindow()
howto_screen = gui.InstructionsWindow()
input_screen = gui.InputWindow()
story_screen = gui.StoryWindow()
holder = ''
inputs = []
position = input_screen.position

templates = open('templates.txt', 'r').readlines() #list ng lahat ng templates
temp_to_use = templates[position] #outputs a string ng mismong template na gagamitin
template = temp_to_use.split('_') #outputs a list ng mga parts ng template (sentences _ sentences)

def change_screen(screen):
	global current_screen
	current_screen = screen
	#screen.show()

def makestory(template,inputs):
	story = ''
	maximum = len(template)

	for i in range(maximum):
		story += template[i]
		try:
			story += inputs[i]
		except IndexError:
			pass
	return story

def update(dt):
	pass

def main():
	change_screen(title_screen)
	pyglet.clock.schedule_interval(update, 1 / 60.0)
	pyglet.app.run()

@window.event
def on_key_press(symbol, modifiers):
	global holder
	global inputs
	global story
	if symbol == pyglet.window.key.UP:
		if current_screen == title_screen:
			change_screen(options_screen)
		elif current_screen == howto_screen:
			holder = ''
			change_screen(input_screen)

	elif symbol == pyglet.window.key.DOWN:
		if current_screen == options_screen:
			change_screen(input_screen)

	elif symbol == key.LEFT:
		if current_screen == options_screen:
			change_screen(howto_screen)

	elif symbol == key.RIGHT:
		if current_screen == options_screen:
			exit()

	elif symbol == pyglet.window.key.BACKSPACE:
		holder = holder[:-1]
		input_screen.holder.text = holder

	elif symbol == pyglet.window.key.ENTER:
		if current_screen == input_screen:
			inputs.append(holder)
			holder = ''
			input_screen.counter += 1
			if input_screen.counter == input_screen.maximum:
				holder = ''
				change_screen(story_screen)

		elif current_screen == story_screen:
			story = makestory(template,inputs)
			story_file = open('yourstory.txt','w')
			story_file.write(story)
			story_file.close()
			end_screen = gui.EndWindow()
			change_screen(end_screen)

@window.event
def on_text(text):
	global holder
	if current_screen == input_screen:
		if (text.isalnum()) or text == ' ':
			holder += text
		input_screen.holder.text = holder
		window.clear()

@window.event
def on_draw():
	global current_screen
	window.clear()
	current_screen.draw()

if __name__ == '__main__':
	main()