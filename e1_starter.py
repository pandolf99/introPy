"""
Simple Functions
"""

def sphere_volume(radius: float) -> float:
    """Return the volume of a sphere with a certain radius.
    Assume pi = 3.
    Note: Look up the formula for volume of a sphere online if 
    you can't remember.
    
    >>> sphere_volume(1.0)
    4.0
    >>> sphere_volume(3.5)
    171.5
    """

    #Your code here
    
def multiple_spheres_volume(radius: float, num_spheres: int) -> float:
    """Return the total volume of num_spheres spheres of the same radius.
    Note: You are *required* to call your sphere_volume function (it's part of 
    your marks for this part).

    >>> multiple_spheres_volume(1.0, 2)
    8.0
    >>> multiple_spheres_volume(3.5, 1)
    171.5
    """

    #Your code here
    
def total_cups(total: int, amount_per_cup: int) -> int:
    """Return the number of full cups you can make with total millilitres of 
    coffee if every cup can hold amount_per_cup millilitres.
    
    >>> total_cups(200, 100)
    2
    >>> total_cups(350, 100)
    3
    """
    
    #Your code here
    
def trip_distance(speed: float, travel_days: int, travel_hours: float) -> float:
    """Return the distance travelled (in km) when travelling with
    speed kilometers per hour for travel_days days and travel_hours hours. 
    Assume uninterrupted travel.

    >>> trip_distance(40.0, 2, 20.0)
    2720.0
    >>> trip_distance(90.0, 0, 3.5)
    315.0
    """

    #Your code here

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
