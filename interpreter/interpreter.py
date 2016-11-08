#!/usr/bin/env python
# coding=utf-8
class Context:
    out = 0
    def __init__(self, str):
        self.str = str

class AbstractExpression(object):
    def interpret(self):
        pass

class AddExpression(AbstractExpression):
    def interpret(self, con):
        con.out+=1

class MinusExpression(AbstractExpression):
    def interpret(self, con):
        con.out-=1

class ConExpression(AbstractExpression):
    def interpret(self, con):
        con.out = (int)((con.str.split('='))[1])

class PrintExpression(AbstractExpression):
    def interpret(self, con):
        print(con.out)

class ContralExpression(AbstractExpression):
    Exp = {}
    Exp['+'] = AddExpression()
    Exp['-'] = MinusExpression()
    Exp['='] = ConExpression()
    Exp['p'] = PrintExpression()
    def interpret(self, con):
        statement = con.str.split(';')
        for state in statement:
            con.str = state
            if '+' in state:
                self.Exp['+'].interpret(con)
            elif '-' in state:
                self.Exp['-'].interpret(con)
            elif '=' in state:
                self.Exp['='].interpret(con)
            elif 'print' in state:
                self.Exp['p'].interpret(con)
            else:
                pass

if __name__ == '__main__':
    str = 'i=3;i++;i--;i++;print i;'
    con = Context(str)
    exp = ContralExpression()
    exp.interpret(con)




