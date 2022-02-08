class Array:
    def __init__(self, array_length):
        self.array_length = array_length
        self.array = []
        
    def createArray(self):
        for i in range(0, self.array_length):
            self.input_number = int(input("Enter your input : "))
            self.array.append(self.input_number)
        print("The Array formed is 👉🏻",self.array)    
        
        

array_creation = Array(int(input("Enter The length : ")))
array_creation.createArray()
