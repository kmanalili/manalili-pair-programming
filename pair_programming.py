# prompt 2
import math

def polar_to_cartesian(r, theta):
    """Convert polar coordinates to cartesian coordinates
    
    Parameters
    
    r : int or float
        distance from the origin
    theta: int or float
        angle, in radians
    
    Returns
    
    x : float
        cartesian x coordinate, rounded to 3 decimals
    y : float
        cartesian y coordinate, rounded to 3 decimals

    """
    
    assert(type(r)==int or type(r)==float),"r should be float or int"
    assert(type(theta)==int or type(theta)==float),"theta should be float or int"
    
    x = round(r * math.cos(theta), 3)
    y = round(r * math.sin(theta), 3)
    
    return x, y