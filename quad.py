def main():
    print("this function soves quadratic equations with real solutions")
    try:
        a,b,c=eval(input('Three coeffeicents seperated by commas '))
        d = math.sqrt(b*b-4*a*c)
        s1 = (-b+d)/2/a
        s2 = (-b-d)/(2*a)
        print('solution: '+str(s1))
        print('solution: '+str(s2))
    except SyntaxError:
        print("use commas")
    except TypeError:
        print("Three numbers Seperated by commas")
    except ValueError as e:
        if str(e)=="math domain error":
            print("no real roots")
        else:
            print("Please type 3 numbers" + str(e))
    else:
        print("made it")
        

        
    
