class fneb:
    def __init__(self) -> None:
        pass



class Bisection:
    def __init__(self,*args):
        self.a,self.b = 3,4
    def midpoint(self):
        # a,b=self.range
        midpoint = (self.a+self.b)/2
        self.mp = midpoint
        return midpoint
        # calculates the midpoint and returns the midpoint
    def calculate_functional_value(self,x):
        # f(x) = x^2-3
        if x == 0:
            functional_value = (self.mp*self.mp)-3
        else:
            functional_value = (x*x)-3
        return functional_value
        #calculates and returns the functional value
        #for each new function, the equation should be hard-coded
    def set_points(self):
        #multiply functional value with older functional value 
        if self.calculate_functional_value(self.a)*self.calculate_functional_value(0)<0:
            self.a = self.a
            self.b = self.mp
        else:
            self.a = self.b
            self.b = self.mp


def main():
    eqn = Bisection()
    no_of_iterations = 6
    print('|----iterations----midpoint------------value----|')
    for i in range(no_of_iterations):
        mp = eqn.midpoint()
        value = eqn.calculate_functional_value(0)
        eqn.set_points()
        print('|----',str(i),'------------',str(mp),'------------',str(value),'----|')
    print('-----------------------------------------------------')
    print('optimal value: ', str(eqn.mp))
    
if __name__ == "__main__":
    main()