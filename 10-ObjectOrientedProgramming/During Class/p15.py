'''
15.	In the TV class, make changes to the show_status() method so that it displays not only the selected channel number but also its name. 
When the selected channel number exceeds the list of available channels, the channel name is not displayed.
TV is on, channel 4 (TVN)
Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers and display TV status every time.
'''

class TV():
    def __init__(self,channels,is_on=False,channel_no=1):
        self.is_on = is_on
        self.channel_no = channel_no
        self.channels = channels
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on and self.channel_no<len(self.channels):
            return f'TV is on, channel {self.channel_no} {self.channels[self.channel_no-1]}'
        elif self.is_on == True and self.channel_no>len(self.channels):
            return 'TV is on, (nieistniejący kanał)'
        else:
            return 'TV if off'
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self,channels_list):
        self.channels = channels_list

    def show_channels(self):
        wynik = ''
        for i in enumerate(self.channels):
            a = str(i[0]+1) + ' ' + str(i[1]) + '\n'
            wynik+=a
        return wynik 
    

polish_channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
tele = TV(polish_channels_list)
print(tele.show_status())
tele.turn_on()
print(tele.show_status())
tele.set_channel(10)
print(tele.show_channels())
print(tele.show_status())
tele.turn_off()