import time

def forward_packet(packet):
    print("packet {} forwarded".format(packet))

def drop_packet(packet):
    print("packet {} dropped".format(packet))

    
class TockenBucket:
    def __init__(self,capacity,time_unit,forward,drop):
        self.capacity = capacity
        self.time_unit = time_unit
        self.forward = forward
        self.drop = drop
        
        self.bucket = capacity
        self.last_check = time.time()
    
    def handle(self,packet):
        elapsed = time.time() - self.last_check
        self.last_check = time.time()
        
        self.bucket+=elapsed*(self.capacity/self.time_unit)
        
        if self.bucket<1:
            return self.drop(packet)
        
        self.bucket-=1
        return self.forward(packet)


obj = TockenBucket(1,1,forward_packet,drop_packet)

for p in [i for i in range(10)]:
    obj.handle(p)
    time.sleep(0.5)
        
