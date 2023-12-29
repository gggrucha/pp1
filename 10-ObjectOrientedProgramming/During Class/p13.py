'''
13.	Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. 
Then try using the TV set.
a.	Create a TV set
b.	Show TV status
c.	Turn TV on
d.	Show TV status
e.	Change TV channel to 5
f.	Show TV status
g.	Turn TV off
h.	Show TV status 
'''
class TV():
    def __init__(self,is_on=False,channel_no=1):
        self.is_on = is_on
        self.channel_no = channel_no
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on and self.channel_no==1:
            return 'TV is on, channel 1'
        elif self.is_on == True and self.channel_no!=1:
            return 'TV is on, on other channel'
        else:
            return 'TV if off'
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

telewiz = TV()
print(telewiz.show_status())
telewiz.turn_on()
print(telewiz.show_status())
telewiz.set_channel(5)
print(telewiz.show_status())
telewiz.turn_off()
print(telewiz.show_status())