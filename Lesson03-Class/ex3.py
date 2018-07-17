class Map:
    def __init__(self,n,p):
        self.record = n
        self.map=[None]*n
        for i in range(n):
            self.map[i]=['*']*n
        if(p == 1):
            self.map[self.record//2-1][self.record//2-1] = '0'
            self.map[self.record//2-1][self.record//2] = '0'
            self.map[self.record//2-1][self.record//2+1] = '0'
            self.map[self.record//2][self.record//2-1] = '0'
            self.map[self.record//2+1][self.record//2] = '0'
    def display(self):
        for i in range(self.record):
            for j in range(self.record):
                print(self.map[i][j],end='')
            print()

my_map02=Map(5,1)
my_map02.display()
