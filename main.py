import os
import sys
from tkinter import *

#   BINARY TREE

# node class
class Node():
    def __init__(self, data = None):
        self.data = data
        self.Left_Child = None
        self.Right_Child = None


class BST():  # binary tree class
    def __init__(self):
        self.root = Node()

    def add(self, value):

        if self.root.data is None:
            self.root.data = value
        else:
            def add_to_node(value, node):  #adds nodes to existing nodes
                if value < node.data:
                    if node.Left_Child is None:
                        node.Left_Child = Node(value)
                    else:
                        add_to_node(value, node.Left_Child)
                if value > node.data:
                    if node.Right_Child is None:
                        node.Right_Child = Node(value)
                    else:
                        add_to_node(value, node.Right_Child)
            add_to_node(value, self.root)
    def Construct(self):
        for i in range(len(bst_Input)):
            self.add(int(bst_Input[i]))

    def Delete(self):
        # preorder
        def Preorder_Traversal(node):
            global result
            if node:
                if node.data:
                    result = Preorder_Traversal(node.Left_Child)
                    if node.data in to_Be_Deleted: result += ('')
                    else: result += (str(node.data) + '    ')
                    result = Preorder_Traversal(node.Right_Child)
            return result
        Preorder_Traversal(self.root)
# declaration of global variables

# is the form of input right
valid_flag = True
result = ''
# separated values of the binary tree from the input
bst_Input = []
# separated to-be-deleted values
to_Be_Deleted = []
newBST = BST()

# GRAPHICAL USER INTERFACE (for Windows)

root = Tk()
root.title('Binary Search Tree')
root.configure(bg='#E8DCCA')
root.geometry('480x250')
info0 = Label(root, text='---THIS IS THE APP THAT BUILDS THE BINARY TREE AND DELETES ITS ELEMENTS---') #This is an app that helps building and editing binary search trees.')
info1 = Label(root, text='Input a series of integers, separated by spacebar, to create a BST [end with -999].')
info2 = Label(root, text='Then input a series of integers to be deleted from BST [end with -990]')
info0.place(x=17, y=20)
info1.place(x=25, y=50)
info2.place(x=50, y=70)


def input_split(text):

    global valid_flag
    text = text.split()
    if text.count('-999') != 1:
        valid_flag = False
    if '-0' in text:
        valid_flag = False

    if not (text[-1] == '-990' or text[-1] == '-999'):
        valid_flag = False
    a = bst_Input
    for i in range(len(text)):
        try:
            text[i] = int(text[i])
        except:
            valid_flag = False
            break

        if text[i] == -999:

            a = to_Be_Deleted
        elif text[i] == -990:
            break
        else:
            a.append(text[i])
    print(bst_Input)


def input_command():

    global valid_flag

    inp = input.get()
    input_split(inp)
    newBST.Construct()
    newBST.Delete()
    if valid_flag:
        info5 = Label(root, text='Your tree is ready:) Have a look!')
        info5.place(x=120, y=180)
        res = Label(root, text=result)
        res.place(x=120,y=210)

    else:
        info6 = Label(root, text='Error: input is invalid!')
        info6.place(x=170, y=190)

def again_command():
    os.execl(sys.executable, sys.executable, *sys.argv)



input = Entry(root, width=50)
input.place(x=85, y=110)
input_button = Button(root, text='Create a BST', bg='#C1D4E3', command=input_command)
input_button.place(x=150, y=140)
try_again_button = Button(root, text='Try again', bg='#CCE8DB', command=again_command)
try_again_button.place(x=250, y=140)


root.mainloop()
