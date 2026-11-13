def main():
    calc = Calculator()

class Calculator:
    operators_penalty = {
            '*' : 1,
            '/' : 1,
            '+' : 2, 
            '-' : 2
            }
    
    def __init__(self):
        self.expression     =   ""
        self.variables      =   []
        self.operations     =   []
        self.parenthesis    =   [0, 0]

        while self.expression == "" :
            try :
                self.expression = input("\n\n\nEnter the operation: ")
            except KeyboardInterrupt :
                print("Keyboard interrupt")
                exit()
            except : print("Looks like the setter failed, thus the parse")

        #print(f"        DEBUG - 26 - init - Expression has been evaluated correct. We move forward met the calculations.")
        print(f"\r\r{self}")

        self.__init__()

    def __str__(self) :
        try :   return self.expression + " = " +str(self.calculate())
        except : return ""

    '''                                                                               ATTRIBUTES                                                                                    '''
    @property   # Expression
    def expression(self) : return self._expression
    @expression.setter
    def expression(self, expr) :
        try :
            self.parse(expr)
            #print(f"        DEBUG - 42 - expression setter - 'try : parse()' successful")
            if expr != "" and expr[0] in Calculator.operators_penalty : expr = "0" + expr
            self._expression = expr
        except Exception as e :
            print(f"Syntax error: {e}.\nType a new expression:")
            self._expression = ""
    '''                                                                               ATTRIBUTES                                                                                    '''


    '''                                                                                 METHODS                                                                                     '''
    def parse(self, expr: str = None) :                 # Storing all variables, operations and parenthesis in order of appeareance
        #print(f"        DEBUG - 53 - parse() - Parsing '{expr}' ...")
        if expr == "" : return
        if expr[0] in Calculator.operators_penalty : expr = "0" + expr

        vars    = []
        ops     = []
        pars    = [0, 0]
        v = 0   # Variable ID 
        o = 0   # Operator ID

        for c in expr :
            #print(f"        DEBUG - 64 - parse() - Parsing character '{c}' ...")
            if c.isdigit() or c in '().' : 
                #print(f"        DEBUG - 66 - parse() - '{c}' is digit")
                try :           vars[v] = vars[v] + c
                except:         vars.append(c)
                if c == '(' :   pars[0] += 1
                if c == ')' :
                    pars[1] += 1
                    if pars[1] > pars[0] : raise Exception("Missing opening parenthesis '('")
            elif c in Calculator.operators_penalty :
                if pars[0] > pars[1] : vars[v] = vars[v] + c
                else:
                    ops.append(c)
                    o +=1
                    v +=1
            else :  raise Exception(f"Character {c} is not recognized as a mathematical expression (could be due to this calculator's limitations). Please double check and, if correct, lower your standards.")

        # Error checking
        if pars[0] > pars[1] : raise Exception("Missing closing parenthesis ')'")
        if not (0 < len(vars) == len(ops)+1) : raise Exception("Missing operator or operand")

        # Save parsed expresion as instance variables (only when it's the main expression, so that recursion won't overwrite the main epxression parsed)
        if self.expression == "" :
            #print(f"        DEBUG - 87 - parse() - self.expression == '' --> '{expr}'")
            self.variables = vars
            self.operations = ops
            self.parenthesis = pars

        return vars, ops, pars

    def operate(self, variables: list, operators: list, id: int) :
        match operators.pop(id) :
            case "+" :  variables[id] += variables.pop(id+1)
            case "-" :  variables[id] -= variables.pop(id+1)
            case "*" :  variables[id] *= variables.pop(id+1)
            case "/" :
                try :   variables[id] /= variables.pop(id+1)#
                except : raise Exception(f"Dividing by 0 is not allowed in mathematics.")
            case _ : raise Exception(f"Operator '{operators[id]}' not recognized by this measly calculator.")

    def calculate(self, varsopspars : tuple = None) :
        if varsopspars == None : varsopspars = (self.variables, self.operations, self.parenthesis)
        vars, ops, pars = varsopspars

        # Convert stored variables to float
        for i in range(len(vars)) :
            try :   vars[i] = float(vars[i])
            except:
                #print(f"        DEBUG - 112 - calculate() - Cannot convert variable '{vars[i]}' to float.\nNow we recurse: {vars[i]} -->  {vars[i][1:len(vars[i])-1]}")
                vars[i] = self.calculate(self.parse(vars[i][1:len(vars[i])-1]))   # Substitute the variable for the result of its calculation

        while len(vars) > 1 :
            first = (99, 99) # first = (operator, penalty)
            for i in reversed(range(len(ops))) :    # Check operator penalty and update 'first' recursively, from right to left (as the lefmost item is the first by default)
                penalty = Calculator.operators_penalty[ops[i]]
                if penalty <= first[1] :
                    first = (i, penalty)
            i = first[0]
            #print(f"        DEBUG - 122 - calculate() - vars = '{vars}' - ops = '{ops}' - id = '{i}'")
            try : self.operate(vars, ops, i)
            except Exception as e :
                print(f"Mathematical error: {e}")
                raise Exception

        try :   return vars[0]
        except :
            print("Nothing to return")
            return 0
    '''                                                                                 METHODS                                                                                     '''



if __name__ == '__main__':
    main()
