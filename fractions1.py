def gcd(a,b):
   r = a%b
   if r==0:
     return b
   return gcd(b,r)
 
class Fraction:
  def __init__(self,n,d):
     if d==0:
       print('Error')
     self.sign = n*d<0
     if n<0:
       self.num = -n
     else:
       self.num = n
     if d<0:
       self.den = -d
     else:
       self.den = d
     g = gcd(self.num,self.den)
     self.num //= g
     self.den //= g

  def __sub__(self,other):
      n1 = self.den * other.num
      n2 = other.den * self.num
      n = n1 - n2
      d = self.den * other.den
      if self.sign and not other.sign or not self.sign and other.sign:
         n = -n
      return Fraction(n,d)

  def __add__(self,other):
      n1 = self.den * other.num
      n2 = other.den * self.num
      n = n1 + n2
      d = self.den * other.den
      if self.sign and not other.sign or not self.sign and other.sign:
         n = -n
      return Fraction(n,d)
 
  def __mul__(self,other):
    n = self.num*other.num
    d = self.den*other.den
    if self.sign and not other.sign or not self.sign and other.sign:
      n = -n
    return Fraction(n,d)
 
  def __truediv__(self,other):
    n = self.num*other.den
    d = self.den*other.num
    if self.sign and not other.sign or not self.sign and other.sign:
      n = -n
    return Fraction(n,d)
 
  def __str__(self):
    if self.sign:
      s = '-'
    else:
      s =''
    s += (str(self.num)+'/'+str(self.den))
    return s

  

x = Fraction(2,4)
y = Fraction(1,6)
d = x.__sub__(y)
a = x.__add__(y)
b = x.__mul__(y)
c = x.__truediv__(y)
print(a)
print(b)
print(c)
print(d)
