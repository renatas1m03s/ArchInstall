#!/usr/bin/env python3

import blessed

OPTIONS_LIMIT = 15

def choices_set_options_limit(term, options_limit):
	global OPTIONS_LIMIT
	
	if options_limit <= term.width - 7 and options_limit != 0:
		OPTIONS_LIMIT = options_limit
		return 0
	else:
		OPTIONS_LIMIT = 15
		return 1

def key_down(idx_row, idx_offset, options_limit, len_menu):
	if idx_row < len_menu-1:
		idx_row += 1
		if idx_row >= options_limit and (idx_offset+options_limit) < len_menu -1:
			idx_offset +=1
	else:
		idx_row=0
		idx_offset=0
	return idx_row, idx_offset

def key_up(idx_row, idx_offset, options_limit, len_menu):
	if idx_row == 0:
		idx_row = len_menu-1
		idx_offset= (idx_row-options_limit)+1
	else:
		idx_row-=1
		if idx_row <= options_limit:
			idx_offset=0
		else:
			idx_offset-=1
	return idx_row, idx_offset		

def key_pgdwn(idx_row, idx_offset, options_limit, len_menu)	:
	if len_menu <= options_limit:
		idx_row = len_menu -1
	else:
		if idx_row < (len_menu-1)-options_limit:
			idx_row += options_limit
			if idx_row >= options_limit and (idx_offset+options_limit) < len_menu-1:
				idx_offset += options_limit
		else:
			idx_row=0
			idx_offset=0	
	return idx_row, idx_offset
	
def key_pgup(idx_row, idx_offset, options_limit, len_menu):
	if len_menu <= options_limit:
		idx_row = 0
	else:
		if idx_row > options_limit:
			idx_row -= options_limit
			if idx_row >= options_limit and (idx_offset+options_limit) > 0:
				idx_offset -= options_limit
		else:
			idx_row = len_menu-1
			idx_offset= (idx_row-options_limit)	
	return idx_row, idx_offset
	
# Return one sigle item off inline menu list
def choices_horizontal_menu(term, position, menu, title=None):
	key = 0
	idx_column = 0
	y = position[0]
	x = position[1]
	preserv_y = y
	preserv_x = x
	encerra = True

	while encerra: # Inicia o loop que é interrompido somente com o enter
		x = preserv_x
		y = preserv_y
		selected_items = '0'
		if title:
			print(term.move_yx(y,x)+title)
			y+=1
		for idx, item_menu in enumerate(menu): #  Printa as opções do menu
			if idx == idx_column:
				print(term.move_yx(y,x)+term.bold(term.black_on_gray("[•] "+item_menu)))
			else:
				print(term.move_yx(y,x)+"[ ] "+item_menu)
			x = x + len(menu[idx])+6
#		print(term.move_yx(y+1,x)+"Press ENTER to select item and move on")
		with term.cbreak(), term.hidden_cursor():
			key = term.inkey()
		if key.name == 'KEY_RIGHT' and idx_column < len(menu)-1:
			idx_column += 1
		if key.name == 'KEY_LEFT' and idx_column > 0:
			idx_column -=1
		if key.name == 'KEY_ENTER':
			selected_items = menu[idx_column]
			encerra = False
			return selected_items
		if key.name == 'KEY_ESCAPE':
			encerra = False
			return '0'

# Return one sigle item off menu list
def choices_single_option(term, position, menu, title=None): 
	key = idx_row = idx_offset = 0
	finish = True
	selected_item = '0'

	navigate_instructions = 'Navigate with '+ term.bold('ARROWS/PgUP/PgDN') + ', press ' + term.bold('ENTER') + ' to select and proceed to next step.'	
	
	preserv_y = position[0]
	y = position[0]
	x = position[1]
	
	if len(menu) <= OPTIONS_LIMIT:
		options_limit = len(menu)
	else:
		options_limit = OPTIONS_LIMIT
		
	while finish: # Stops with ENTER or ESC
		i=0
		y = preserv_y
		if title:
			print(term.move_yx(y,x)+title)
			y+=2
		for i in range(options_limit): 
			if i+idx_offset == idx_row:
				print(term.move_yx(y+i,x) + term.bold(term.black_on_gray("[•] "+menu[i+idx_offset]) + term.clear_eol))
			else:
				if idx_row <= len(menu)-1 and (i+idx_offset) <= len(menu)-1:
					print(term.move_yx(y+i,x) + "[ ] " + menu[i+idx_offset] + term.clear_eol)
		
		print(term.move_yx(y+2+i,x) + navigate_instructions + term.clear_eol, idx_row, idx_offset)
		
		with term.cbreak(), term.hidden_cursor():
			key = term.inkey()
		if key.name == 'KEY_DOWN':
			idx_row, idx_offset = key_down(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_UP':
			idx_row, idx_offset = key_up(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_PGDOWN':
			idx_row, idx_offset = key_pgdwn(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_PGUP':
			idx_row, idx_offset = key_pgup(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_ENTER':
			selected_item = menu[idx_row]
			return selected_item
			finish = False
		if key.name == 'KEY_ESCAPE':
			finish = False
			return '0'

# Return one or several items off menu list, selected_items are possible default values
def choices_multiple_options(term, position, menu, title = None, selected_items = None): # title and selected itens are optional
	key = 0
	idx_row = 0
	idx_offset = 0
	x = position[1]
	y = position[0]
	preserv_y = y
	preserv_x = x
	encerra = True
	YES_OR_NO = ['Yes','No']
	yes_or_no = 0

	if len(menu) <= OPTIONS_LIMIT:
		options_limit = len(menu)
	else:
		options_limit = OPTIONS_LIMIT

	if selected_items:
		preserv_selected_items = selected_items
	else:
		selected_items = list(('0'))
		preserv_selected_items = list(('0'))

	while encerra: # Stops with ENTER or ESC
		y = preserv_y
		x = preserv_x
		if title:
			print(term.move_yx(y,x)+term.clear_eos()+title) # Print title without clear entire screen
			y+=2 # Adds a line between title and options
		i = 0
		for i in range(options_limit): 
			if menu[i+idx_offset] in selected_items:
				if i+idx_offset == idx_row:
					print(term.move_yx(y,x)+term.bold(term.black_on_gray("[x] "+menu[i+idx_offset])) + term.clear_eol)
				else:
					if i+idx_offset <= len(menu)-1:
						print(term.move_yx(y,x) + "[x] "+menu[i+idx_offset] + term.clear_eol)
			else:
				if i+idx_offset == idx_row:
					print(term.move_yx(y,x) + term.bold(term.black_on_gray("[-] "+menu[i+idx_offset])) + term.clear_eol)
				else:
					print(term.move_yx(y,x) + "[ ] "+menu[i+idx_offset] + term.clear_eol)
			y+=1 
		print(term.move_yx(y+1,x)+'Press ' + term.bold('SPACE') + ' to select item, ' + term.bold('ENTER') + ' to finish and proceed to next step')
		with term.cbreak(), term.hidden_cursor():
			key = term.inkey()
		if key.name == 'KEY_DOWN':
			idx_row, idx_offset = key_down(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_UP':
			idx_row, idx_offset = key_up(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_PGDOWN':
			idx_row, idx_offset = key_pgdwn(idx_row, idx_offset, options_limit, len(menu))
		if key.name == 'KEY_PGUP':
			idx_row, idx_offset = key_pgup(idx_row, idx_offset, options_limit, len(menu))
		if key == ' ':
			if selected_items[0] == '0':
				selected_items[0] = menu[idx_row]
			else:
				if menu[idx_row] in selected_items or menu[idx_row] in preserv_selected_items:
					if len(selected_items)==1:
						selected_items[0]='0'
					else:
						selected_items.remove(menu[idx_row])
				else:
					selected_items.append(menu[idx_row])
		if key.name == 'KEY_ENTER':
			if selected_items[0] == '0':
				print(term.move_yx(y+3,x)+'Nothing is selected, this is correct?')	
				x = x+term.length(term.move_yx(y+3,x)+'No option selected, this is correct?')+2
				position[0]=y+3
				position[1]=x
				yes_or_no=choices_horizontal_menu(term, position,YES_OR_NO)
				if yes_or_no==YES_OR_NO[0]:
					encerra = False
					return selected_items
			else:
				encerra = False
				return selected_items
		if key.name == 'KEY_ESCAPE':
			encerra = False
			return '0'
