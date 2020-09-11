from tkinter import *
def remove_match_char(list1, list2): 

	for i in range(len(list1)) : 
		for j in range(len(list2)) : 
			if list1[i] == list2[j] : 
				c = list1[i] 

				list1.remove(c) 
				list2.remove(c) 
				list3 = list1 + ["*"] + list2 

				return [list3, True] 

	list3 = list1 + ["*"] + list2 
	return [list3, False] 


def tell_status() : 
	
	p1 = Player1_field.get() 

	p1 = p1.lower() 

	p1.replace(" ", "") 

	p1_list = list(p1) 

	p2 = Player2_field.get() 
	p2 = p2.lower() 
	p2.replace(" ", "") 
	p2_list = list(p2) 
 
	proceed = True
	while proceed : 

		ret_list = remove_match_char(p1_list, p2_list) 
		con_list = ret_list[0] 
		proceed = ret_list[1] 

		star_index = con_list.index("*") 

		p1_list = con_list[ : star_index] 

		p2_list = con_list[star_index + 1 : ] 


	# count total remaining characters 
	count = len(p1_list) + len(p2_list) 

	# list of FLAMES acronym 
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 

	# keep looping untill only one item 
	# is not remaining in the result list 
	while len(result) > 1 : 

		# store that index value from 
		# where we have to perform slicing. 
		split_index = (count % len(result) - 1) 

		# this steps is done for performing 
		# anticlock-wise circular fashion counting. 
		if split_index >= 0 : 

			# list slicing 
			right = result[split_index + 1 : ] 
			left = result[ : split_index] 

			# list concatenation 
			result = right + left 

		else : 
			result = result[ : len(result) - 1] 

	# insert method inserting the 
		# value in the text entry box. 
	Status_field.insert(10, result[0]) 


# Function for clearing the 
# contents of all text entry boxes 
def clear_all() : 
	Player1_field.delete(0, END) 
	Player2_field.delete(0, END) 
	Status_field.delete(0, END) 
	
	# set focus on the Player1_field entry box 
	Player1_field.focus_set() 


# Driver code 
if __name__ == "__main__" : 
	
	# Create a GUI window 
	root = Tk() 
	
	# Set the background colour of GUI window 
	root.configure(background = 'red') 
	
	# Set the configuration of GUI window 
	root.geometry("350x125") 
	
	# set the name of tkinter GUI window 
	root.title("Flames Game") 
		
	# Create a Player 1 Name: label 
	label1 = Label(root, text = "Player 1 Name: ", 
				fg = 'black', bg = 'dark green') 
	
	# Create a Player 2 Name: label 
	label2 = Label(root, text = "Player 2 Name: ", 
				fg = 'black', bg = 'dark green') 
		
	# Create a Relation Status: label 
	label3 = Label(root, text = "Relationship Status: ", 
				fg = 'black', bg = 'pink') 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	label1.grid(row = 1, column = 0, sticky ="E") 
	label2.grid(row = 2, column = 0, sticky ="E") 
	label3.grid(row = 4, column = 0, sticky ="E") 

	# Create a text entry box 
	# for filling or typing the information. 
	Player1_field = Entry(root) 
	Player2_field = Entry(root) 
	Status_field = Entry(root) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	# ipadx keyword argument set width of entry space . 
	Player1_field.grid(row = 1, column = 1, ipadx ="50") 
	Player2_field.grid(row = 2, column = 1, ipadx ="50") 
	Status_field.grid(row = 4, column = 1, ipadx ="50") 

	# Create a Submit Button and attached 
	# to tell_status function 
	button1 = Button(root, text = "Submit", bg = "yellow", 
					fg = "black", command = tell_status) 
	
	# Create a Clear Button and attached 
	# to clear_all function 
	button2 = Button(root, text = "Clear", bg = "blue", 
					fg = "black", command = clear_all) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	button1.grid(row = 3, column = 1) 
	button2.grid(row = 5, column = 1) 

	# Start the GUI 
	root.mainloop() 
