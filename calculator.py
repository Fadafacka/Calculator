class Calculator:
    operators_priority = {
            '*' : 1,
            '/' : 1,
            '+' : 2, 
            '-' : 2
            }
    
    def __init__(self):
        self.expression = ""
        self.variables = []
        self.operations = []
        self.parenthesis = [0, 0]

        while self._expression == "" :
            try :
                self.expression = input(".\n..\n...\nEnter the operation: ")
            except KeyboardInterrupt :
                print("Keyboard interrupt")
                exit()
            except : print("Looks like the setter failed, thus the parse")

        print("DEBUG - 26 - init - Expression has been evaluated correct. We move forward met the calculations.")
        print(self)

        self.__init__()

    def __str__(self):
        return str(self.calculate())

    '''                                                                               ATTRIBUTES                                                                                    '''
    @property   # Expression
    def expression(self): return self._expression
    @expression.setter
    def expression(self, expr):
        try:
            self.parse(expr)
            print("DEBUG - 41 - expression setter - 'try : parse()' successful")
            self._expression = expr
        except Exception as e :
            print(f"DEBUG - 44 - expression setter - Exception: {e}")
            self._expression = ""
    '''                                                                               ATTRIBUTES                                                                                    '''


    '''                                                                                 METHODS                                                                                     '''
    def parse(self, expr: str = None) :                 # Storing all variables, operations and parenthesis in order of appeareance
        print(f"DEBUG - 51 - parse() - Parsing '{expr}' ...")
        if expr == "" : return

        vars = []
        ops = []
        pars = [0, 0]
        v = 0   # Variable ID 
        o = 0   # Operator ID

        for c in expr:
            print(f"DEBUG - 61 - parse() - Parsing character '{c}' ...")
            if c.isdigit() or c in '().' : 
                print(f"DEBUG - 63 - parse() - '{c}' is digit")
                try :           vars[v] = vars[v] + c
                except:         vars.append(c)
                if c == '(' :   pars[0] += 1
                if c == ')' :
                    pars[1] += 1
                    if pars[1] > pars[0] :
                        raise Exception("Closing parenthesis without opening.")
            elif c in Calculator.operators_priority :
                if pars[0] > pars[1] :
                    vars[v] = vars[v] + c
                else:
                    ops.append(c)
                    o +=1
                    v +=1

        # Error checking
        if pars[0] > pars[1] :
            print('Missing closing parenthesis ")"')
            raise

        if pars[0] < pars[1] :
            print('Missing opening parenthesis')
            raise

        if not (0 < len(vars) == len(ops)+1):
            print('Missing operator or operand')
            raise

        # Save parsed expresion as intance variables
        if self.expression == "" :
            print(f"DEBUG - 111 - parse() - self.expression == '' --> '{expr}'")
            self.variables = vars
            self.operations = ops
            self.parenthesis = pars

        return vars, ops, pars

    def calculate(self, varsopspars = None):
        if varsopspars == None : varsopspars = self.variables, self.operations, self.parenthesis
        vars, ops, pars = varsopspars

        # Convert stored variables to float
        for i in range(len(vars)) :
            try: vars[i] = float(vars[i])
            except:
                print(f"DEBUG - 96 - calculate() - Cannot convert variable '{vars[i]}' to float.\nExiting in absence of further implementation")
                print(f"\nNow we recurse: {self.vars[i]} -->  {self.vars[i][1:len(self.vars[i])-1]}")
                exit()
                # If the variable is a parenthesis expression
                if self.vars[i][0] == '(' and self.vars[i][len(self.vars[i])-1] == ')': 
                    print(f"\nNow we recurse: {self.vars[i]} -->  {self.vars[i][1:len(self.vars[i])-1]}")
                    print(self.vars[i][1:len(self.vars[i])-1])
                    # Substitute the variable for the result of its calculation
                    #self._vars[i] = calculate(parse(self._vars[i][1:len(self._vars[i])-1]))
                else:
                    print(f"variable {i} is not a number or a parenthesis")
                    quit()

        while len(vars) > 1 :
            ops.pop(0)
            vars[0] = vars[0]+vars.pop(1)

        print("DEBUG - 126 - calculate() - Finishing")

        try :
            return self.variables[0]
        except :
            print("Nothing to return")
            return 0

        '''
        print(f'\nCalculating {l}{op}{r}...\n        self.variables: {self.variables}\n        self.operations: {self.operations}')
        
        if op == '*':
            return l*r
        elif op == '/':
            return l/r
        elif op == '+':
            return l+r
        elif op == '-':
            return l-r
        elif op == '':
            for o in self.operations:
                order = {}
                order[o] = self.operators[self.operations[o]]

        while len(order) > 0 :
            for e in order.copy() :
                if order[e] == 1:
                    _ = order.pop(e)
                    self.variables[e] = self.calculate(self.variables[e], self.variables.pop(e+1), self.operations.pop(e))

            for e in order.copy() :
                if order[e] == 2 :
                    _ = order.pop(e)
                    self.variables[e] = self.calculate(self.variables[e], self.variables.pop(e+1), self.operations.pop(e))
        return result
        '''
    '''                                                                                 METHODS                                                                                     '''

if __name__ == '__main__':
    main()
