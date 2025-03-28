import binascii, logging, socket, struct

class impsocket :
    "improved socket class - this is REALLY braindead because the socket class doesn't let me override some methods, so I have to build from scratch"

    def __init__(self, sock = None) :
        if sock is None :
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else :
            self.s = sock


    def accept(self) :
        (returnedsocket, address) = self.s.accept()
        newsocket = impsocket(returnedsocket)
        newsocket.address = address

        return newsocket, address


    def bind(self, address) :
        self.address = address
        self.s.bind(address)


    def connect(self, address) :
        self.address = address
        self.s.connect(address)

        #logging.debug(str(self.address) + ": Connecting to address")


    def close(self) :
        self.s.close()


    def listen(self, connections) :
        self.s.listen(connections)


    def send(self, data, log = True) :
        sentbytes = self.s.send(data)

        #if log :
        #    logging.debug(str(self.address) + ": Sent data - " + binascii.b2a_hex(data))

        #if sentbytes != len(data) :
        #    logging.warning("NOTICE!!! Number of bytes sent doesn't match what we tried to send " + str(sentbytes) + " " + str(len(data)))

        return sentbytes

    def sendto(self, data, address, log = True) :
        sentbytes = self.s.sendto(data, address)

        #if log :
        #    logging.debug(str(address) + ": sendto Sent data - " + binascii.b2a_hex(data))

        #if sentbytes != len(data) :
        #    logging.warning("NOTICE!!! Number of bytes sent doesn't match what we tried to send " + str(sentbytes) + " " + str(len(data)))

        return sentbytes


    def send_withlen(self, data, log = True) :
        lengthstr = struct.pack(">L", len(data))

        #if log :
        #    logging.debug(str(self.address) + ": Sent data with length - " + binascii.b2a_hex(lengthstr) + " " + binascii.b2a_hex(data))

        totaldata = lengthstr + data
        totalsent = 0
        while totalsent < len(totaldata) :
            sent = self.send(totaldata, False)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent


    def recv(self, length, log = True) :
        data = self.s.recv(length)

        #if log :
        #    logging.debug(str(self.address) + ": Received data - " + binascii.b2a_hex(data))

        return data

    def recvfrom(self, length, log = True) :
        (data, address) = self.s.recvfrom(length)

        #if log :
        #    logging.debug(str(address) + ": recvfrom Received data - " + binascii.b2a_hex(data))

        return (data, address)

    def recv_all(self, length, to_log = True):
        data = b""
        while len(data) < length:
            chunk = self.recv(length - len(data), False)
            if chunk == -1:
                return -1
            if chunk == b'':
                #log.warning(f"Socket connection broken during Recieve with {str(self.address)}")
                self.track_broken_connection(str(self.address[0]))
            data = data + chunk
        #if to_log:
        #    log.debug(f"{str(self.address)}: Received all data - {binascii.b2a_hex(data).decode()}")
        return data

    def recv_withlen(self, to_log = True):
        lengthstr = self.recv(4, False)
        if lengthstr == -1:
            return -1
        if len(lengthstr) != 4:
            #log.debug(f'Command header not long enough, should be 4, is {str(len(lengthstr))}')
            return b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # DUMMY RETURN FOR FILESERVER
        else:
            length = struct.unpack(">L", lengthstr)[0]
            data = self.recv_all(length, False)
            #log.debug(f"{str(self.address)}: Received data with length  - {binascii.b2a_hex(lengthstr).decode()} {binascii.b2a_hex(data).decode()}")
            return data

    def getsockname(self) :
        return self.s.getsockname()


