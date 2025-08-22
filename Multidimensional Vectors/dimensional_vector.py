class DimensionalVector:
    def __init__(self, d):
        #Create a d-dimensional vector of zeros.
        #Example: Vector(3) → <0, 0, 0>
        self._coords = [0] * d #internal list of coordinates
    def __len__(self):
        #Return the size (dimension) of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        #Return the j-th coordinate of the vector.
        #allows the indexing to access a coordinate
        return self._coords[j]
    def __setitem__(self, j, value):
        #Set the j-th coordinate of the vector to given value.
        #enables the indexing to set a value for coordinate
        self._coords[j] = value
    def __add__(self, other):
    #Return sum of two vectors.
     if isinstance(other, DimensionalVector):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = DimensionalVector(len(self)) #create a new vector
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
     elif isinstance(other, list):   # case: Vector + list
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            result = DimensionalVector(len(self))
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result
     else:
            raise TypeError("Operand must be Vector or list")
            #Throws error if addition is attempted with unsupported type.

    
    def __eq__(self, other):
        #Return True if vector equals other.
        if isinstance(other, DimensionalVector):
            return self._coords == other._coords
        elif isinstance(other, list):
            return self._coords == other
        return False
    def __ne__(self, other):
        #Return True if vector differs from other.
        return not self == other
    def __str__(self):
        #Produce string representation of vector.
         return "<" + str(self._coords)[1:-1] + ">"
    
