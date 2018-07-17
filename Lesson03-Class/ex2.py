class Map:
    def set_map(self,n):
        self.record = n
        self.map = [None] * n
        for i in range(n):
            self.map[i] = ['*'] * n
    def display(self):
        for i in range(self.record):
            for j in range(self.record):
                print(self.map[i][j],end='')
            print()
    def set_pattern(self,p):
        if(p == 1):
            self.map[self.record//2-1][self.record//2-1] = '0'
            self.map[self.record//2-1][self.record//2] = '0'
            self.map[self.record//2-1][self.record//2+1] = '0'
            self.map[self.record//2][self.record//2-1] = '0'
            self.map[self.record//2+1][self.record//2] = '0'

my_map=Map()
my_map.set_map(5)
my_map.display()
print()
my_map.set_pattern(1)
my_map.display()

print()
my_map.set_map(7)
my_map.display()
print()
my_map.set_pattern(1)
my_map.display()           

