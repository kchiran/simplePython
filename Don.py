

def get_sum(self):
    a=0
    for i in self:
        a = a + i
    return a




def list_sum(self):
   if len(self) == 1:
        return self[0]
   else:
        return self[0] + list_sum(self[1:])



def get_sum_a(self):
    total = 0
    ele = 0
    while(ele < len(self)): 
        total = total + self[ele] 
        ele += 1
    return total

p=[1,2,3]
print(get_sum(p))
print(list_sum(p))
print(get_sum_a(p))