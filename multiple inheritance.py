class Device:
    def __init__(self,device_name,status):
        self.device_name=device_name
        self.status=status
    def turn_on(self):
        print('Device Turned On')
    def turn_off(self):
        print('Device Turned Off')
    def display(self):
        print(f"Device Name: {self.device_name}")
        print(f"Status: {self.status}")

class SmartLight(Device):
    def __init__(self,device_name,status,brightness):
        super().__init__(device_name,status)
        self.brightness=brightness
    def turn_on(self):
        super().turn_on()
    def turn_off(self):
        super().turn_off()
    def display(self):
        super().display()
        print(f"Brightness: {self.brightness}%")
    def set_brightness(self):
        self.brightness=int(input('Enter brightness to be set(in %): '))
        print('Brightness set successfully.')
        
class SmartSpeaker(Device):
    def __init__(self,device_name,status,volume):
        super().__init__(device_name,status)
        self.volume=volume
    def turn_on(self):
        super().turn_on()
    def turn_off(self):
        super().turn_off()
    def display(self):
        super().display()
        print(f"Volume: {self.volume}%")
    def set_volume(self):
        self.volume=int(input('Enter volume to be set(in %): '))
        print('Volume set successfully.')
        
class SmartHome(SmartLight, SmartSpeaker):
    def __init__(self, device_name, status, brightness, volume):
        Device.__init__(self, device_name, status)
        self.brightness = brightness
        self.volume = volume

    def display(self):
        Device.display(self)
        print(f"Brightness: {self.brightness}%")
        print(f"Volume: {self.volume}%")

home = SmartHome("My Smart Home", "ON", 70, 40)
home.display()