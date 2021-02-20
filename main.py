from machine import UART  # Universal synchronous receiver / transmitter



uart = UART(bits=8, baudrate=9600, parity=None, stop=1, timeout_chars=100 pins('P3', 'P4'))
# bits = number of bits per character 5,6,7 or 8
# baudrate = clock rate
# parity = check error
# stop = number of stop bits 1 or 2
# timeout_chars = RX timeout in number of characters
# pins = pin 3 & 4 are our RX and TX pins on the microcontroller

while True:
    header_byte = uart.read(1)
    while header_byte != b'\XFF'):
        header_byte = uart.read(1)

    DATA_H = int(uart.read(1)[0])
    Data_L = int(uart.read(1)[0])
    SUM = int(uart.read(1)[0])

    if DATA_H + DATA_L == SUM
        distance = (Data_H*256)+ Data_L
        print(distance)
