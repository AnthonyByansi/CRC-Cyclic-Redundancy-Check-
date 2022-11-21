# CRC-Cyclic-Redundancy-Check-
Commonly used in digital networks and storage devices to identify unintentional alterations to digital data. CRC or Cyclic Redundancy Check is a method of detecting accidental changes/errors in the communication channel.

The MODULO algorithm serves as the foundation for the CRC, a complicated algorithm evolved from the CHECKSUM error detection technique. For executing the computations, it is relied on the value of polynomial coefficients in binary format.
Here, we'll look at how to employ this technique in the data link layer to find errors on the receiver end. Additionally, you'll see the data format that the sender and receiver use to communicate.

Say a sender wishes to send data with a length of M. Let's now assume that the highest degree generator polynomial function, R, is what produces the CRC bits. The sender follows up by sending a total of M+R data bits to the recipient.
# Ilustration  
![CRC demostration](./crc.jpg)
