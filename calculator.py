from tkinter import *
from tkinter import ttk

def main():
    calc = calculator()
    vars = calc.variables
    ops = calc.operations
    paren = calc.parenthesis

    '''
  
    '''
    '''
    print(f"paren = {paren}")
    for i in paren:
        print(i, paren[i])

    print(f"\nvars = {vars}")
    for i in vars:
        print(i, vars[i])

    print(f"\nops = {ops}")    
    for i in ops:
        print(i, ops[i])
    '''
    

class calculator:
    def __init__(self, expr=''):
        if expr == '': expr = input ("Enter the operation: ")
        if expr == '': self.__init__()

        # Storing all variables, operations and parenthesis in order of appeareance
        operators = {
                    '*' : 1,
                    '/' : 1,
                    '+' : 2, 
                    '-' : 2
                    }
        v = 0
        o = 0
        self._variables = {}
        self._operations = {}
        self._parenthesis = {}
        count_paren = {}

        for c in expr:
            if c.isdigit() or (c == '.'): 
                print(f"c is {c} ")
                self._variables[v] = self._variables.get(v, '') + c
                if self._operations.get(o):
                    o +=1
                print(f"self._variables is {self._variables}\n")

            elif c in operators:
                print(f"c is {c} ")
                self._operations[o] = c
                if self._variables.get(v):
                    v +=1
                print(f"self._operations is {self._operations}\n")
                
# PAY ATTENTION HEREEEE
            elif c in ['(', ')']:
                print(f"c is {c} ")
                self._parenthesis[c] = {o: self._parenthesis.get(c, {}).get(o, 0)+1}
                count_paren[c] = count_paren.get(c, 0) + 1
                print(f"self._parenthesis is {self._parenthesis} ")
                print(f"count_paren is {count_paren}\n")

    	# Error checking
        if count_paren.get('(', 0) > count_paren.get(')', 0):
            print('Missing closing parenthesis')
            self.__init__()
        if count_paren.get('(', 0) < count_paren.get(')', 0):
            print('Missing opening parenthesis')
            self.__init__()
        if not len(self._variables) == len(self._operations)+1:
            print('Operator without operand')
            self.__init__()

        # Convert stored variables to float
        for i in self._variables:
            try: self._variables[i] = float(self._variables[i])
            except: continue

        # Perform calculations
        i = 0
        while i < len(self._variables)-1:
            result = self.calculate(self._variables[i], self._variables[i+1], self._operations[i])
            print(result)
            i +=1

        #self.__init__()

    # Variables
    @property
    def variables(self):
        return self._variables
    @variables.setter
    def variables(self, v):
        self._variables = v

    # Operations
    @property
    def operations(self):
        return self._operations
    @operations.setter
    def operations(self, o):
        self._operations = o

    # Parenthesis
    @property
    def parenthesis(self):
        return self._parenthesis
    @parenthesis.setter
    def parenthesis(self, p):
        self._parenthesis = p

    def calculate(self, l, r, op):
        if op == '*':
            return(l*r)
        if op == '/':
            return(l/r)
        if op == '+':
            return(l+r)
        if op == '-':
            return(l-r)

if __name__ == '__main__':
    main()

























































'''
window = Tk()
window.title("Hijueputa calculator")

mainframe = ttk.Frame(window, padding="5 3 12 12")
mainframe.grid(column=4, row=4, sticky=(N, W, E, S))
window.columnconfigure(4, weight=1)
window.rowconfigure(4, weight=1)

mult_button = ttk.Button(window,text='*')


calculation = StringVar()
calculation_entry = ttk.Entry(mainframe, width=30, textvariable=calculation)
calculation_entry.grid(column=3, row=3, sticky=(N, S))

window.mainloop()
'''