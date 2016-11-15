#!/usr/bin/env python
# coding=utf-8

class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs


class HasQuarterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You cannot insert another quarter")
    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    def turnCrank(self):
        print("You turned...")
        self.gumballMachine.setState(self.gumballMachine.getSoldState())
        def dispense(self):
            print("No gumball dispense")

class SoldOutState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Candy sold out")
    def ejectQuarter(self):
        print('Haven''t insert yet')
    def turnCrank(self):
        print("No gumball")
    def dispense(self):
        print("No gumball dispense")

class NoQuanterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
    def ejectQuarter(self):
        print("Haven't inserted quarter")
    def turnCrank(self):
        print("Turned, but there's no quarter")
    def dispense(self):
        print("Need to pay first")

class SoldState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount()>0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs

        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuanterState(self)
        self.hasQuartState = HasQuarterState(self)
        self.soldState = SoldState(self)

        if self.count > 0:
            self.state = self.noQuarterState

    def getSoldOutState(self):
        return self.soldOutState
    def getNoQuarterState(self):
        return self.noQuarterState
    def getHasQuarterState(self):
        return self.hasQuartState
    def getSoldState(self):
        return self.soldState
    def setState(self, state):
        self.state = state

    def insertQuarter(self):
        self.state.insertQuarter()
    def ejectQuarter(self):
        self.state.ejectQuarter()
    def turnCrank(self):
        if self.state == self.hasQuartState:
            self.state.turnCrank()
            self.state.dispense()
        else:
            self.state.turnCrank()

    def releaseBall(self):
        print("Gumball roll out now")
        if self.count != 0:
            self.count -= 1

    def getState(self):
        print(self.state)
    
    def getCount(self):
        return self.count

def main():
    gumballMachine = GumballMachine(2)
    gumballMachine.getCount()
    gumballMachine.getState()
    print('----------------------------')
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.ejectQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    gumballMachine.getCount()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    print('-----------------------------')
    gumballMachine.turnCrank()

if __name__ == '__main__':
    main( )

