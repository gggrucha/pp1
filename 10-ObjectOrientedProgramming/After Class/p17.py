'''
17.	In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0. 
Add two methods to increase and decrease the TV volume level by one. 
Note that you cannot increase or decrease the volume beyond the specified range. 
Display the current volume level in the show_status() method. 
Then check the operation of the TV by adjusting and displaying its volume level.
'''
class TV():
    def __init__(self,channels, volume=0,is_on=False,channel_no=1):
        self.is_on = is_on
        self.channel_no = channel_no
        self.channels = channels
        self.volume = volume
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on and self.channel_no<len(self.channels):
            return f'TV is on, channel {self.channel_no} {self.channels[self.channel_no-1]}' + f' volume is: {self.volume}'
        elif self.is_on == True and self.channel_no>len(self.channels):
            return 'TV is on, (nieistniejący kanał)' + f' volume is: {self.volume}'
        else:
            return 'TV if off' + f' volume is: {self.volume}'
        
        
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
    
    def vol_incr(self):
        if self.volume < 10 and self.is_on==True:
            self.volume+=1
    
    def vol_decr(self):
        if self.volume > 0 and self.is_on==True:
            self.volume-=1

telewizor = TV(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
telewizor.turn_on()
print(telewizor.show_status())
telewizor.vol_incr()
print(telewizor.show_status())
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
telewizor.vol_incr()
print(telewizor.show_status())
telewizor.vol_incr()
print(telewizor.show_status())