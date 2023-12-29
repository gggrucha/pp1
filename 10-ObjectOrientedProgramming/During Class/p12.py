'''
12.	In the TV class, add the channel_no attribute indicating the number of the TV channel displayed by the TV set. 
Initially, the TV is set to channel 1. Modify the show_status() method so that it also displays the TV channel number, 
but only if the TV is turned on:
TV is on, channel 1
Then, try using the TV set.
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
        elif self.is_on == True:
            return 'TV is on'
        else:
            return 'TV if off'
    
tele = TV()
tele.is_on=True
print(tele.show_status())
    
