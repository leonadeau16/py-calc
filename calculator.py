import tkinter as tk 

class Calculator:
    def __init__(self):
        self.answer = None
        self.operation = None
        self.last_ans = None
        self.entry = None

        self.window = tk.Tk()
        self.window.geometry("400x500")
        self.window.title("Calculator")
    
    def clear(self):
        self.__init__()
    
    def run(self):
        # self.create_widgets()
        self.window.mainloop()
    
    def computeParentheses(self, values):
        while "(" in values:
            x = values.index("(")
            y = values.index(")")
            values2 = values[x+1:y]
            if "(" in values2:
                self.computeParentheses(values2)
            else:
                values[x] = self.calculate(values2)
                del values[x+1:y+1]
        return values

    def calculate(self, values):
        while len(values) > 1:
            while "^" in values:
                z = values.index("^")
                values[z-1] = values[z-1] ** values[z+1]
                del values[z:z+2]
            while "*" in values:
                z = values.index("*")
                values[z-1] = values[z-1] * values[z+1]
                del values[z:z+2]
            while "/" in values:
                z = values.index("/")
                values[z-1] = values[z-1] / values[z+1]
                del values[z:z+2]
            while "+" in values:
                z = values.index("+")
                values[z-1] = values[z-1] + values[z+1]
                del values[z:z+2]
            while "-" in values:
                z = values.index("-")
                values[z-1] = values[z-1] - values[z+1]
                del values[z:z+2]
        return values[0]
    
    def checkMinus(self, values):
        while 

    def separateValues(self, entry):
        chars = entry.split()
        values = []
        for i in range(len(chars)):
            if chars[i].isdigit():
                for j in range(i+1, len(chars)):
                    if chars[j].isdigit():
                        continue
                    else:
                        values.append(float(chars[i:j])) if '.' in chars[i:j] else values.append(int(chars[i:j]))
            elif chars[i] == '-':
                if i == 0 or chars[i-1]:
                    

        '''
        values = []
        for i in range(len(entry)):
            if i == len(entry)-1:
                if entry[i].isdigit():
                    values.append(int(entry[i]))
                else:
                    values.append(entry[i])
            elif entry[i] == "-":
                if i == 0 or not entry[i-1].isdigit():
                    for j in range(i+1, len(entry)):
                        if j == len(entry[i:])-1:
                            if i == j-1:
                                values.append(int(entry[j]) * -1)
                            elif 

            elif entry[i].isdigit():
                for j in range(i+1, len(entry)):
                    if j == len(entry)-1:
                            values.append(float(entry[i:j])) if '.' in entry[i:j] else values.append(int(entry[i:j]))
                    elif entry[j].isdigit() or entry[j] == '.':
                        continue
                    else:
                        values.append(float(entry[i:j])) if '.' in entry[i:j] else values.append(int(entry[i:j]))
                        i=j
            else:
                values.append(entry[i])
        return values
        '''

    def compute(self, entry):
        self.entry = entry
        values = self.separateValues(self.entry)
        no_paren = self.computeParentheses(values)
        print(self.calculate(no_paren))

calc = Calculator()
calc.compute("-1")