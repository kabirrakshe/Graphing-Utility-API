import turtle
import time
tp = turtle
tp.setpos(0,0)
tp.ht()
colors = ["red", "yellow", "green", "blue", "black"]
class FunctionGrapher():
    def __init__(self, coefficients, exponents): #Initializes equation as lists of corresponding coefficients and exponents
        self.coefficients = coefficients
        self.exponents = exponents
        self.origin = (0,0)

    def output(self, x): #Used for I/O Returning
        final = (sum([x ** self.exponents[i] * self.coefficients[i] for i in range(len(self.coefficients))]))
        return final

    # def graph(self, end): DRAFT Graphing Functino
    #     ymax = self.output(end)
    #     currentx = end
    #     for i in range(ymax + 1):
    #         ycoord = ymax - i
    #         if currentx == end+1:
    #             break
    #         output_for_currentx = self.output(currentx)
    #         if output_for_currentx == ycoord:
    #             print(str(ycoord) + '|' + (' ' * (currentx)) + '*')
    #             currentx -= 1
    #             continue
    #         print(str(ycoord) + '|')
    #     print('  ' + '_' * (end+1))
    #     print('  ', end = '')
    #     for i in range((end + 1)):
    #         print(i, end = '')
    def turtlegraph(self, start, end, skip = False): #Main Graphing Function
        global colors
        if skip == False:
            tp.pd()
            tp.forward(end)
            tp.pu()
            tp.setpos(self.origin)
            tp.left(180)
            tp.pd()
            tp.forward(end)
            tp.pu()
            tp.right(180)
            tp.setpos(self.origin)
            tp.left(90)
            tp.pd()
            ymax = self.output(end)
            tp.forward(self.output(end))
            tp.pu()
            tp.setpos(self.origin)
            tp.left(180)
            tp.pd()
            tp.forward(self.output(end))
            tp.pu()
            tp.right(180)
            tp.setpos(self.origin)
        tp.pencolor(colors[-1])
        tp.setpos(start, self.output(start))
        eq = []
        for i in range(len(self.coefficients)):
            exp = '^' + str(self.exponents[i])
            coe = str(self.coefficients[i])
            if self.exponents[i] == 1:
                exp = ''
            if self.coefficients[i] == 1:
                coe = ''
            eq.append(f'{coe}x{exp}')
        tp.setpos(300, len(colors) * 60)
        tp.pd()
        tp.write('y = ' + '+'.join(eq), align = "right", font = ("Arial", 20, 'normal'))
        colors.pop()
        tp.pu()
        tp.setpos(start, self.output(start))
        tp.pd()
        for i in range(start, end+1):
            tp.goto(i, self.output(i))
            tp.dot()
        tp.pu()
