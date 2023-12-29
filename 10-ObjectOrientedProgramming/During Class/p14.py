'''
14.	In the TV class, add the channels attribute containing a list of available TV channel names (array). 
Initially, the array should be empty (TV not programmed, no available channels). 
Add set_channels(channels_list) and show_channels() methods in the TV class, 
which allows you to set channels on the TV and display the list of available channels. 
Sample list of available channels:
Channel list:
1. TVP1
2. TVP2
3. Polsat
4. TVN
5. Filmbox
6. Discovery
Then, try using the TV set:
a.	Create a TV set
b.	Show TV status
c.	Turn TV on
d.	Show TV status
e.	Display the list of available channels
f.	Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
g.	Display the list of available channels
h.	Show TV status
i.	Turn TV offs
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
        if self.is_on and self.channel_no==1:
            return 'TV is on, channel 1'
        elif self.is_on == True and self.channel_no!=1:
            return 'TV is on, on other channel'
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
print(tele.show_channels())
print(tele.show_status())
tele.turn_off()