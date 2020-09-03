class QuadraticEquation(object):
    
    def __init__(self, valueA : float, valueB : float, valueC : float):
        self.__a      = valueA
        self.__b      = valueB
        self.__c      = valueC
        self.__x1     = 0
        self.__x2     = 0

    def __Discriminant(self)->float:
        return ( ( self.__b ** 2 ) - ( 4 * self.__a * self.__c ) )
    
    def __NotRoots(self):
        return "Квадратное уравнение не имеет корней!"

    def __OneRoot(self):
        return "Квадратное уравнение имеет один корень : x = " + str( ( ( -( self.__b ) / ( 2 * self.__a ) ) ) )
    
    def __TwoRoots(self):
        self.__x1 = ( -self.__b + self.__d ** (1/2) ) / ( 2 * self.__a )
        self.__x2 = ( -self.__b - self.__d ** (1/2) ) / ( 2 * self.__a )
        return "Квадратное уравнение имеет два корня : x1 = " + str( self.__x1 )  + " ; x2 = " + str( self.__x2 ) 

    def __LineEquation(self)->str:
        return "Уравнение принимает линейный вид, x = " + str( self.__c / self.__b )

    def __Cal(self):
        if self.__a == 0 :
            return self.__LineEquation()
        else : 
            self.__d = self.__Discriminant()
            if self.__d < 0 :
                return self.__NotRoots()
            elif self.__d == 0 :
                return self.__OneRoot()
            elif self.__d > 0 :
                return self.__TwoRoots() 

    def GetResult(self):
        return self.__Cal()
    