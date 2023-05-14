#from gui import GUI
from tkinter import *
from graph import Graph


window = Tk()
graph = Graph()
count = 0
window.title("Strong consistency")
label_main = Label(window, text="Check if the graph is strongly consistent", font=("Montserrat", 16),
                           bg='#FFF2F2', foreground='#241414')
label_main.grid(column=0, row=0, columnspan=3, padx=80, pady=60)
window['bg'] = '#FFF4F4'
window.geometry('608x320')
window.resizable(width=False, height=False)
photo = PhotoImage(file='icon.png')
window.iconphoto(False, photo)
vertexes = Entry(window)
btn_create = Button(window, text='Create a graph', bg='#D0ADA7', foreground='#241414',
                    activebackground='#FFC8AF', command=lambda: create())
btn_random = Button(window, text='Random graph', bg='#D0ADA7', foreground='#241414',
                    activebackground='#FFC8AF', command=lambda: random())
btn_create.grid(column=0, row=1, columnspan=1, padx=96, pady=0)
btn_random.grid(column=1, row=1, columnspan=1, padx=0, pady=0)
label_invalid = Label(window, text="Invalid input", font=("Montserrat", 14),
                      bg='#FFF2F2', foreground='#241414')
edge_start = Entry(window)
edge_end = Entry(window)
btn_close = Button(window, text='Close', bg='#D0ADA7', foreground='#241414',
                   activebackground='#FFC8AF', command=lambda: check_window())
btn_check = Button(window, text='Check', bg='#D0ADA7', foreground='#241414',
                   activebackground='#FFC8AF', command=lambda: check(graph))
label_vert = Label(window, text="Input a vertex", font=("Montserrat", 14),
                   bg='#FFF2F2', foreground='#241414')
label_ed_start = Label(window, text="Input start vertex of an edge", font=("Montserrat", 14),
                       bg='#FFF2F2', foreground='#241414')
btn_addv = Button(window, text='Add', bg='#D0ADA7', foreground='#241414',
                  activebackground='#FFC8AF', command=lambda: add_v_check())
btn_adde = Button(window, text='Add', bg='#D0ADA7', foreground='#241414',
                  activebackground='#FFC8AF', command=lambda: add_e_check())
label_ed_end = Label(window, text="Input end vertex of an edge", font=("Montserrat", 14),
                     bg='#FFF2F2', foreground='#241414')
label_true = Label(window, text="The graph is strongly consistent.", font=("Montserrat", 14),
                   bg='#FFF2F2', foreground='#241414')
label_false = Label(window, text="The graph isn't strongly consistent.", font=("Montserrat", 14),
                    bg='#FFF2F2', foreground='#241414')


def create():
    label_main.grid_forget()
    btn_create.grid_forget()
    btn_random.grid_forget()


    label_vert.grid(column=0, row=0, columnspan=1, padx=20, pady=20)

    vertexes.grid(column=2, row=0, columnspan=2, padx=5, pady=5)

    label_ed_start.grid(column=0, row=1, columnspan=1, padx=20, pady=10)

    label_ed_end.grid(column=0, row=3, columnspan=1, padx=20, pady=10)


    edge_start.grid(column=2, row=1, columnspan=1)
    edge_end.grid(column=2, row=3, columnspan=1)

    btn_addv.grid(column=4, row=0, columnspan=3, padx=5, pady=5)

    btn_adde.grid(column=4, row=2, columnspan=3, padx=5, pady=5)
    btn_close.grid(column=0, row=5, pady=30)


def add_v_check():
    global vertexes
    global label_invalid
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O', 'P', 'R', 'S','T', 'U', 'V', 'W', 'X',
            'Y', 'Z']
    if vertexes.get().isdigit() or vertexes.get() in values:
        label_invalid.grid_forget()
        v = vertexes.get()
        add_v(vertexes.get())
    else:
        vertexes.delete(0, 'end')
        label_invalid.grid(column=0, row=6, columnspan=3, padx=64, pady=60)

def add_e_check():
    global edge_start
    global edge_end
    if edge_start.get() in graph.graph and edge_end.get() in graph.graph:
        label_invalid.grid_forget()
        s = edge_start.get()
        e = edge_end.get()
        add_e(s, e)
    else:
        edge_start.delete(0, 'end')
        edge_end.delete(0, 'end')
        label_invalid.grid(column=0, row=6, columnspan=3, padx=64, pady=60)


def add_e(s, e):
    edge_start.delete(0, 'end')
    edge_end.delete(0, 'end')
    graph.add_edge(s, e)
def add_v(v):
    vertexes.delete(0, 'end')
    graph.add_vertex(v)
def random_graph(self):
    return


def check_window():
    label_main.grid(column=0, row=0, columnspan=3, padx=80, pady=60)
    label_invalid.grid_forget()
    label_vert.grid_forget()
    label_ed_start.grid_forget()
    label_ed_end.grid_forget()
    btn_adde.grid_forget()
    btn_addv.grid_forget()
    btn_close.grid_forget()
    vertexes.grid_forget()
    edge_start.grid_forget()
    edge_end.grid_forget()
    btn_check.grid(column=0, row=1, columnspan=3, padx=80, pady=30)


def check(g):
    btn_check.grid_forget()
    label_main.grid_forget()
    result = strong_consistency(g)
    if result:
        label_true.grid()
    else:
        label_false.grid()



def dfs_help(graph):
    postvisited = {}
    visited = set()

    def dfs_visit(graph, vertex, visited, postvisited):
        global count
        visited.add(vertex)
        count += 1

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                dfs_visit(graph, neighbor, visited, postvisited)

        count += 1
        postvisited[vertex] = count
        print(vertex, postvisited[vertex])

    def dfs(graph, visited, postvisited):
        for vertex in graph.graph:
            if vertex not in visited:
                dfs_visit(graph, vertex, visited, postvisited)

    dfs(graph, visited, postvisited)

    rev = dict(reversed(list(postvisited.items())))
    postvisited_sorted = list(rev.keys())

    return postvisited_sorted


def dfs_main(graph, order):
    visited = set()

    def dfs_visit(graph, vertex, visited):
        visited.add(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                dfs_visit(graph, neighbor, visited)

    def dfs(graph, visited, order):
        count_main = 0
        for vertex in order:
            if vertex not in visited:
                count_main += 1
                dfs_visit(graph, vertex, visited)
        return count_main
    res = dfs(graph, visited, order)
    return res


def strong_consistency(graph):
    print("Input graph: ")
    graph.print_graph()
    reversed_graph = graph.reverse_graph()
    print()
    print("Reversed graph: ")
    reversed_graph.print_graph()
    print()
    res = dfs_main(graph, dfs_help(reversed_graph))

    if res == 1:
        return True
    else:
        return False


def random():
    label_invalid.grid_forget()
    label_vert.grid_forget()
    label_ed_start.grid_forget()
    label_ed_end.grid_forget()
    btn_adde.grid_forget()
    btn_addv.grid_forget()
    btn_close.grid_forget()
    vertexes.grid_forget()
    edge_start.grid_forget()
    edge_end.grid_forget()
    btn_random.grid_forget()
    btn_create.grid_forget()
    check(graph2)


#TESTCASE 1

graph1 = Graph()
graph1.add_vertex(7)
graph1.add_vertex(1)
graph1.add_vertex(6)
graph1.add_vertex(2)
graph1.add_vertex(3)
graph1.add_vertex(8)
graph1.add_vertex(4)
graph1.add_vertex(5)
graph1.add_edge(1, 6)
graph1.add_edge(1, 2)
graph1.add_edge(2, 3)
graph1.add_edge(2, 5)
graph1.add_edge(3, 4)
graph1.add_edge(4, 2)
graph1.add_edge(4, 8)
graph1.add_edge(5, 7)
graph1.add_edge(5, 4)
graph1.add_edge(6, 7)
graph1.add_edge(7, 6)
graph1.add_edge(8, 7)

#TESTCASE 2

graph2 = Graph()
graph2.add_vertex('C')
graph2.add_vertex('A')
graph2.add_vertex('B')
graph2.add_vertex('G')
graph2.add_vertex('D')
graph2.add_vertex('E')
graph2.add_vertex('H')
graph2.add_vertex('I')
graph2.add_vertex('J')
graph2.add_vertex('F')
graph2.add_edge('B', 'A')
graph2.add_edge('E', 'A')
graph2.add_edge('B', 'G')
graph2.add_edge('A', 'C')
graph2.add_edge('E', 'I')
graph2.add_edge('G', 'I')
graph2.add_edge('I', 'H')
graph2.add_edge('A', 'H')
graph2.add_edge('H', 'G')
graph2.add_edge('H', 'F')
graph2.add_edge('J', 'C')
graph2.add_edge('D', 'F')
graph2.add_edge('C', 'D')
graph2.add_edge('F', 'J')


#TESTCASE 3

graph3 = Graph()
graph3.add_vertex(0)
graph3.add_vertex(1)
graph3.add_vertex(2)
graph3.add_vertex(3)
graph3.add_vertex(4)
graph3.add_vertex(5)
graph3.add_vertex(6)
graph3.add_vertex(7)
graph3.add_vertex(8)
graph3.add_edge(0, 1)
graph3.add_edge(1, 2)
graph3.add_edge(3, 0)
graph3.add_edge(0, 4)
graph3.add_edge(4, 1)
graph3.add_edge(2, 5)
graph3.add_edge(4, 3)
graph3.add_edge(4, 5)
graph3.add_edge(6, 3)
graph3.add_edge(4, 7)
graph3.add_edge(8, 4)
graph3.add_edge(5, 8)
graph3.add_edge(7, 6)
graph3.add_edge(8, 7)


window.mainloop()







