class ClassName:

    def __init__(self, id, size, brand: int = 13, weight: int = 1, shape: int =1, breed: int = 10):
        self.x = id
        self.y = size
        self.z = brand
        self.m = weight
        self.n = shape
        self.v = breed

    def print_out_instance_attributes(self):
        print(self.z)
        print(self.v)

if __name__ == "__main__":

    test_argument = {"id": 1, "size": 2, "brand": 3, "weight": 4, "shape":5}

    a = ClassName(**test_argument)
    a.print_out_instance_attributes()
