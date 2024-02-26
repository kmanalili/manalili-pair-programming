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

# Suggestions for improving the documentation of this function:
# 1. Add inline comments explaining what each line of code does. This can be especially helpful for readers who are not familiar with the math involved in converting polar coordinates to Cartesian coordinates.
# 2. Include an example in the docstring showing how to use the function and what output to expect. This provides a clear usage guide for the function.
# 3. Remember, the right amount of comments depends on the complexity of the code and the audience. Too many comments can make the code cluttered and harder to read, while too few can leave readers confused. Strive to find the right balance.


import unittest

class TestPolarToCartesian(unittest.TestCase):
    def test_polar_to_cartesian(self):
        # Test with r=1, theta=0, expected result is (1, 0)
        self.assertEqual(polar_to_cartesian(1, 0), (1.0, 0.0))

        # Test with r=1, theta=pi/2, expected result is (0, 1)
        self.assertEqual(polar_to_cartesian(1, math.pi/2), (0.0, 1.0))

        # Test with r=2, theta=pi, expected result is (-2, 0)
        self.assertEqual(polar_to_cartesian(2, math.pi), (-2.0, 0.0))

        # Test with r=0, theta=pi/2, expected result is (0, 0)
        self.assertEqual(polar_to_cartesian(0, math.pi/2), (0.0, 0.0))

    def test_invalid_input(self):
        # Test with non-numeric r
        with self.assertRaises(AssertionError):
            polar_to_cartesian('a', 0)

        # Test with non-numeric theta
        with self.assertRaises(AssertionError):
            polar_to_cartesian(1, 'b')

if __name__ == '__main__':
    unittest.main()