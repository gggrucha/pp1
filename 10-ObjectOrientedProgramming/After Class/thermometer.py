class Thermometer():
    def __init__(self,turned_on=False) -> None:
        self.turned_on = turned_on

    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False
  
    def measurement(self, object):
        if object>=37 and object<41:
            print(str(object)+'C'+' (fever)')
        elif object>=41:
            print(str(object)+'C'+' (CRITICAL TEMPERATURE)')
        else:
            print(str(object)+'C')
            
    