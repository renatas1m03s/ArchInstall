#!/usr/bin/env python3

import blessed

PRINTABLE_AREA = 100

def text_set_printable_area(term, printable_area):
	global PRINTABLE_AREA
	
	if printable_area <= term.width:
		PRINTABLE_AREA = printable_area
		return 0
	else:
		return 1
	
def text_justify_left(term, position, text):
	text = term.move_yx(position[0], (term.width-PRINTABLE_AREA)//2)+text
	return text
	
def text_justify_left_middle(term, position, text):
	text = term.move_yx(position[0], ((term.width-PRINTABLE_AREA)//2) + (((PRINTABLE_AREA)//2))) +text
	return text
	
def text_justify_center(term, position, text):
	text = term.move_yx(position[0], (term.width-PRINTABLE_AREA)//2)+(term.center(text, PRINTABLE_AREA))
	return text

def text_print_list(term, position, text_list):
	key = 0
	x = position[1]
	y = position[0]

	for i, line in enumerate(text_list):
		print(term.move_yx(y+i,x)+term.clear_eos()+line)
	pass

def resolve_uw_display(term, inc_y=None, inc_x=None): # Increments of y and x are optional
	offset = list((int(0),int(0)))
	
	position = term.get_location()
	if inc_y or inc_x:
		if inc_y:
			offset[0] = position[0] + inc_y
		if inc_x:
			offset[1] = position[1] + inc_x
	else:
		offset[0] = position[0]
		offset[1] = position[1]
		
	if term.width > PRINTABLE_AREA:
		offset[1]=(offset[1]+((term.width-PRINTABLE_AREA)//2))
	
	return offset
