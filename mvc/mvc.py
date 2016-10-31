#!/usr/bin/env python
# coding=utf-8
tuple_instance = ('list', 'tuple', 'dictionary', 'function')

class QuoteModel(object):
    def __init__(self):
        pass
    def get_quote(self, n):
        try:
            value = tuple_instance[n]
        except IndexError:
            value = 'No such value'
        return value

class QuoteView(object):
    def __init__(self):
        pass
    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))
    def showerr(self, msg):
        print('Error: {}'.format(msg))
    def select_quote(self):
        return raw_input('Which one would you like to select? ')

class QuoteController(object):
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteView()
    def run(self):
        valid_input = False
        while not valid_input:
            self._n = self.view.select_quote()
            try:
                n = int(self._n)
            except ValueError:
                self.view.showerr('Incorrect number {}'.format(self._n))
                return 0
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)
    def runend(self):
        if self._n == 'end':
            return False
        else:
            return True

def main():
    controller = QuoteController()
    indicator = True
    while indicator:
        controller.run()
        indicator = controller.runend()

if __name__ == '__main__':
    main()





