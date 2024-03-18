import time

def forward_packet(packet):
    print("packet {} forwarded".format(packet))

def drop_packet(packet):
    print("packet {} dropped".format(packet))



class SlidingWindow:
    def __init__(self,capacity,time_unit,forward,drop):
        self.capacity = capacity
        self.time_unit = time_unit
        self.forward = forward
        self.drop = drop
        
        self.prev_count = capacity
        self.count = 0
        self.current_time = time.time()
    
    def handle(self,packet):
        if time.time()-self.current_time>self.time_unit:
            self.prev_count = self.count
            self.count = 0
            self.current_time = time.time()
        
        ec = self.count + self.prev_count*((self.time_unit - (time.time()-self.current_time))/self.time_unit)
        
        if ec>self.capacity:
            return self.drop(packet)
        
        self.count+=1
        return self.forward(packet)
    


obj = SlidingWindow(1,1,forward_packet,drop_packet)

for p in [i for i in range(10)]:
    obj.handle(p)
    time.sleep(0.5)
        
