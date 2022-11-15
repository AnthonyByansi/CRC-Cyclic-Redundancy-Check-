frompycrc.crclib import *
def main():

  
#Sender Side
div = str(input("Input divisor in binary type: "))
#user_dataword = str(raw_input("Input dataword in binary type: "))
userdataword = '1001'
print ("
Sender:")
sen = Sender(bin2dec(userdataword), div)
sen.send()
print ("arg_dataword:", sen.arg_dataword2)
print ("remainder:", sen.remainder2)
print ("codeword:", sen.codeword2)

       
       
       
#Channel
print ("
Channel:")
ch = Channel(sen.codeword)
print ("Through to the channel get channel codeword:", dec2bin(ch.ch_codeword))

       
       
#Receiver Side
print ("
Receiver:")
rcv = Receiver(ch.ch_codeword, div)
rcv.receive()
print ("syndrome:", rcv.syndrome2)
print ("Discard or not?", rcv.discard)
print ("rx_dataword:", rcv.rx_dataword2)
if __name__ == '__main__':
   main()
