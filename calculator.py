def main():
    calc = Calculator()

class Calculator :
    operators_penalty = {
            '*' : 1,
            '/' : 1,
            '+' : 2, 
            '-' : 2
            }
    
    def __init__(self) :
        self.variables      =   []
        self.operations     =   []
        self.parenthesis    =   [0, 0]
        self.expression     =   ""

        while self.expression == "" :
            try : self.expression = input("\n\n\nEnter the operation: ")
            except KeyboardInterrupt :
                print("Keyboard interrupt")
                exit()

        print(self)
        self.__init__()

    def __str__(self) :
        try :                      return f"                     {self.expression} = {str(self.calculate())}"
        except Exception as e :    return f"                     {e}"



    '''                                                                               ATTRIBUTES                                                                                    '''
    @property   # Expression
    def expression(self) : return self._expression
    @expression.setter
    def expression(self, expr) :
        try :                   self._expression = self.parse(expr)[3]
        except Exception as e : print(f"    Syntax error: {e}.")
    '''                                                                               ATTRIBUTES                                                                                    '''


    '''                                                                                 METHODS                                                                                     '''
    def parse(self, expr: str = None) :                 # Storing all variables, operations and parenthesized variables in order of appeareance
        if expr == "" : return self.variables, self.operations, self.parenthesis, ""
        if expr[0] in Calculator.operators_penalty : expr = "0" + expr

        vars    = []
        ops     = []
        pars    = [0, 0]
        v = 0   # Variable ID 
        o = 0   # Operator ID

        for c in expr :
            if c.isdigit() or c in '().' : 
                try :           vars[v] = vars[v] + c
                except:         vars.append(c)
                if c == '(' :   pars[0] += 1
                if c == ')' :
                    pars[1] += 1
                    if pars[1] > pars[0] : raise Exception(f"Missing opening parenthesis '('")
            elif c in Calculator.operators_penalty :
                if pars[0] > pars[1] : vars[v] = vars[v] + c
                else:
                    ops.append(c)
                    o +=1
                    v +=1
            else : raise Exception(f"Character '{c}' is not recognized by this measly calculator. Please double check and, if correct, lower your standards..")

        # Error checking
        if pars[0] > pars[1] :             raise Exception("Missing closing parenthesis ')'")
        if not (len(vars) == len(ops)+1) : raise Exception("Operator without operand")

        # Save parsed expresion as instance variables (only when it's the main expression, so that recursion won't overwrite the main epxression parsed)
        if self.expression == "" :
            self.variables = vars
            self.operations = ops
            self.parenthesis = pars

        return vars, ops, pars, expr

    def operate(self, variables: list, operators: list, id: int) :
        match operators.pop(id) :
            case "+" :  variables[id] += variables.pop(id+1)
            case "-" :  variables[id] -= variables.pop(id+1)
            case "*" :  variables[id] *= variables.pop(id+1)
            case "/" :
                try :                      variables[id] /= variables.pop(id+1)#
                except ZeroDivisionError : raise Exception(f"Dividing by 0 is not allowed in mathematics.")

    def calculate(self, varsopspars : tuple = None) :
        if varsopspars == None : varsopspars = (self.variables, self.operations, self.parenthesis, self.expression)
        vars, ops, pars, expr = varsopspars

        # Convert stored variables to float
        for i in range(len(vars)) :
            try :   vars[i] = float(vars[i])
            except: vars[i] = self.calculate(self.parse(vars[i][1:len(vars[i])-1]))   # Substitute parenthesized variable for the result of its calculation

        while len(vars) > 1 :
            first = (99, 99) # first = (operator, penalty)
            for i in reversed(range(len(ops))) :    # Check operator penalty and update 'first' recursively, from right to left (as the lefmost item is the first by default)
                penalty = Calculator.operators_penalty[ops[i]]
                if penalty <= first[1] : first = (i, penalty)
            i = first[0]
            try :                   self.operate(vars, ops, i)
            except Exception as e : raise Exception (f"Mathematical error: {e}")

        if vars[0].is_integer() : vars[0] = int(vars[0])
        try :    return vars[0]
        except : raise Exception (f"Something very wrong here, no 'vars[0]'. Line 113")
    '''                                                                                 METHODS                                                                                     '''



if __name__ == '__main__':
    main()
