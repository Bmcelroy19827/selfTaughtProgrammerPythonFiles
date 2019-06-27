# Recursive Algorithms rely on functions that call themselves
# Must have a 'base case'-  ending condition
# Inside the function calls itself and each time moves closer to the base case

def bottles_of_beer(bob):
    """Prints 99 bottles of Beer on the Wall lyrics.
        :param bob: Must be a positive integer
    """
    if bob < 1:
        print("""No more bottles
                of beer
                on the wall.
                No more
                bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of
            beer on the wall. {} bottles
            of beer. Take one
            down, pass it
            around, {} bottles
            of beer n the wall.
            """.format(tmp, tmp, bob))
    bottles_of_beer(bob)


bottles_of_beer(99)

# leetcode.com for algorithm problems
