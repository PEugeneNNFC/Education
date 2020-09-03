class FizzBuzz(object):
    __Three  = 3
    __Five   = 5
    __Zero   = 0
    __ResultFizz     = "Fizz"
    __ResultBuzz     = "Buzz"
    __ResultFizzBuzz = __ResultFizz + __ResultBuzz 

    def __init__(self):
        self.__value = self.__Zero

    def __str__(self):
        return "Число : {} \t Результат : {}".format(self.__value, self.__Result())


    def SetValue(self, value : int):
        self.__value = value

    def GetResult(self)->str:
        return self

    def __CheckThree(self)->bool:
        return (self.__value % self.__Three == self.__Zero)
            
    def __CheckFive(self)->bool:
        return (self.__value % self.__Five == self.__Zero)

    def __CheckThreeFive(self)->bool:
        return (self.__CheckThree() & self.__CheckFive())

    def __Result(self)->str:
        if self.__CheckThreeFive():
            return self.__ResultFizzBuzz
        elif self.__CheckThree() : 
            return self.__ResultFizz
        elif self.__CheckFive() :
            return self.__ResultBuzz
        else:
            return str(self.__value)