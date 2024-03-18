import time

def forward_packet(packet):
    print("packet {} forwarded".format(packet))

def drop_packet(packet):
    print("packet {} dropped".format(packet))

class FixedWindow:
    def __init__(self,capacity,time_unit,forward,drop):
        self.capacity = capacity
        self.time_unit = time_unit
        self.forward = forward
        self.drop = drop
        
        self.count = 0
        self.current_time = time.time()
    
    def handle(self,packet):
        if time.time()-self.current_time>self.time_unit:
            self.count = 0
            self.current_time = time.time()
        
        if self.count>=self.capacity:
            return self.drop(packet)
        
        self.count+=1
        return self.forward(packet)



obj = FixedWindow(1,1,forward_packet,drop_packet)

for p in [i for i in range(10)]:
    obj.handle(p)
    time.sleep(0.5)
        
