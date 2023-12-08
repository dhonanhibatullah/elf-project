import serial



class ElfSerial:



    def __init__(self) -> None:

        # Members
        self.port_list = ['None']


    
    def findPort(self) -> bool:

        COM_NUMBER_SEARCH   = 32
        BAUDRATE            = 115200
        retval              = False
        self.port_list      = ['None']
        
        for i in range(COM_NUMBER_SEARCH):
            try:
                ser = serial.Serial(f'COM{i}', BAUDRATE)
            except:
                continue
            else:
                self.port_list.append(f'COM{i}')
                retval = True

        return retval



    def getPortList(self) -> list:
        return self.port_list