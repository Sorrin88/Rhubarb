import math

class Vector:

    # Initialiser
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns a string representation of the vector
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        return not self.__eq__(other)

        # Returns a tuple with the point corresponding to the vector

    def inte(self):
        return Vector(int(self.x), int(self.y))

    def getP(self):
        return (self.x, self.y)

    def getPx(self):
        return (self.x)

    def getPy(self):
        return (self.y)

    # Returns a copy of the vector
    def copy(self):
        return (self.x,self.y)

    # Adds another vector to this vector
    def add(self, other):
        #result = (self.x+other.x,self.y+other.y)
        self.x+=other.x
        self.y+=other.y
        return self

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        return self.multiply(-1)

    # Subtracts another vector from this vector
    def subtract(self, other):
        self.x-=other.x
        self.y-=other.y
        return self

    # Multiplies the vector by a scalar
    def multiply(self, k):
        #return (self.x*k,self.y*k)
        self.x*=k
        self.y*=k
        return self
    def multiplyVectors(self, other):
        #return (self.x*k,self.y*k)
        self.x = self.x*other.x
        self.y = self.y*other.y
        return self
    # Divides the vector by a scalar
    def divide(self, k):
        return (self.x/k,self.y/k)

    def getMagnitude(self):
        return math.sqrt(self.x**self.x + self.y**self.y)
    # Normalizes the vector
    def normalize(self):
        return self.divide(self.lengh())
    # Returns a normalized version of the vector
    def getNormalized(self):
        mag = self.getMagnitude()
        return self.x/mag, self.y/mag

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y + other.y
    # Returns the squared length of the vector
    def lengthSquared(self):
        # self.getMagnitude()*self.getMagnitude()
        return self.x**2 + self.y**2
    def lengh(self):
        return math.sqrt(self.lengthSquared())
    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.multiply(2*self.dot(normal))
        self.subtract(n)
        return self

    # Returns the angle between this vector and another one
    # You will need to use the arccosine function:
    # acos in the math library
    def angle(self, other):
        return math.cosh((self.dot(other))/(self.getMagnitude()*other.getMagnitude()))