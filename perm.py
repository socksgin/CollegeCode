"""I have never spent more time for 10 points, and had help. Facinateing stuff.
Went to a math lab to understand ordering permutations: Made a complete list of 1-3, and 1-4, some of the 1-5 permuation.

I can't take credit for this, but I'm showing what I learned.
Worked with other students to understand the programming, I had multiple  programs to reference:
Multiple stackoverflow references
The power of Pythons yield
Itertools permutation

I spent time online and in class to figure out how generators, and iterables interact with each other. This video
http://www.youtube.com/watch?v=E_kZDvwofHY&feature=related, and skip to 26:28, it really helped explain things for me"""

class Permutation:
    def __init__(self, lst):
        self.refer = lst[0:5]
        self.new = []

    def __iter__(self):
        return self.next()

    def next(self):
        for value in self.refer:

            if value not in self.new:
                self.new.append(value)

                if len(self.new) == len(self.refer):
                    yield self.new[0:5]#Yield evaluates to true if it does not find a variable in the specified sequence and false otherwise."""

                else:
                    for v in self.next():
                        yield v
                        
                self.new.pop()#pass the pop to the append function


lst = [1,2,3,4,5]
for var in Permutation(lst):
    print (var)
