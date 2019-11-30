class Computer:
    
    def __init__(self,cpu,ram,disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
    def config(self):
        print(self.cpu,self.ram,self.disk)
        
if __name__ == "__main__":
    com1 = Computer('i7', '16gb','1TB')
    com2 = Computer('i8', '8gb','2TB')
    com1.config()
    com2.config()

            