from fizzbuzz import FizzBuzz


fb = FizzBuzz()

for index in range(1, 101):
    fb.SetValue( index )
    if index % 2 == 0 :
        print( fb )
    else:
        print( fb.GetResult() )