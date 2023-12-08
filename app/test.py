# import serial



# class ElfSerial:



#     def __init__(self) -> None:
        
#         # Parameters
#         COM_NUMBER_SEARCH   = 32
#         BAUDRATE            = 115200


#         # Detect available serial port
#         self.port_list = []
#         for i in range(COM_NUMBER_SEARCH):
#             try:
#                 ser = serial.Serial(f'COM{i}', BAUDRATE)
#             except:
#                 continue
#             else:
#                 self.port_list.append(f'COM{i}')


# elf_serial = ElfSerial()
# print(elf_serial.port_list)