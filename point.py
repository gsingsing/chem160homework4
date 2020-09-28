import math
class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    def dist(p1,p2):
        return math.sqrt((p1.data[0]-p2[0])**2+(p1.data[1]-p2[1])**2+(p1.data[2]-p2[2])**2)
    def mirror(self):
        mirror=[]
        self.data=[]
        for i in range(self.dim):
            mirror.append((self.data[i])*(self.data[i]))
        mirror=sum(mirror)
        return mirror
            
        
        
        



