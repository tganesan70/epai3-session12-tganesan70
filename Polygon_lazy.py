##########################################################################
# Session12 assignment for EPAi3 - Module PolygonLazy
#
# Ganesan Thiagarajan, 25th July 2021
##########################################################################
#
from functools import wraps
import math
#from functools import lru_cache
from functools import reduce

# Timed decorator for all functions - but using a global variable for elapsed time in case we want it at __main__ level
elapsed_time = 0

# Function decorator for checking the docstring of functions
def check_doc_string(
        fn: 'Function name that needs to be parsed') -> 'Returns True if the function has 50 words of description':
    """
    This function checks whether the function passed on to this has atleast 50 words of
    description.
    :param fn: Function name that is passed to this function
    :return: Returns a closure which allows the free variables can be accessed later
             The inner function Returns True if it has 50 or more words in its docstring description, else False
    Question: Will the docstring include the argument description function as well?  A BIG NO!
    """
    comment_len = 50
    """
    Doc string for inner function
    :param args: Positional arguments for the function
    :param kwargs:Function arguments for the function
    :return: The function output
    """
    if fn.__doc__ is None:
        return False
    else:
        fn_doc_string = fn.__doc__.split(sep=" ")
        # print(f'No. of words in the docstring comment for {fn.__name__}() is : {len(fn_doc_string)}')
        if len(fn_doc_string) < comment_len:
            return False
        else:
            return True


class PolygonLazy:
    """
    An Lazy iterable Class definition for a regular Polygon with n equal sides and n-vertices
    Args:
        n - Max no. of polygon sides
        R - circum radius - i.e., distance between the center and one of the vertices

    Returns:
        An iterable Polygon class object
    """

    def __init__(self, n, R):
        """
        Sets the initial values of the internal variables n (#sides) and R (circum radius)
        Args:
            n - No. of edges (or sides)
            R - circum radius - i.e., distance between the center and one of the vertices
        """
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R

    def __len__(self):
        """
        Compute the number of polygons in the iterator

        Returns:
            The number of polygons in the iterator starting with a polygon of edges=3 as the starting polynomial
        """
        return self._n - 2

    def __repr__(self):
        """
        __repr__() for the Polygon class objects. The Polygon Iterator is intialized to make it iterable

        Returns:
            Prints the class objects internal variables
        """
        return f'Polygon(n={self._n}, R={self._R})'

    def __iter__(self):
        """
        Iteration function to make the Polygon Class object as iterable
        Returns:
            The Polygon iterator Class object
        """
        return self.PolygonIter(self._n, self._R)

    class PolygonIter:
        """
        Definition for Polygon Iterator Class object
        """
        #nonlocal max_efficiency_polygon, max_efficiency

        def __init__(self, n, r):
            """
            Initializes the Polygon Iterator object
            Args:
                n: Maximum number of edges in the sequence of polygons
                r: Circum radius for the polygon
            Returns:
                None
                But computes the internal list of polygons in self._polygons
                And sets the current_poly as 3 to make it iterable
            """
            self._n = n
            self._r = r
            self._init_poly = 3  # Staring value of iteration
            self.max_efficiency_polygon = 3
            self.max_efficiency = 0

        def __iter__(self):
            return self

        def __next__(self):
            """
            next function to make this sequence as iterable
            Returns:
                The current poly and increments the counter until the maximum limit
            """
            # print(f'Current polygon inside _next() is : {self._current_poly}')
            if self._init_poly >= self._n:
                raise StopIteration
            else:
                result = self._polygon(self._init_poly, self._r)
                self._init_poly += 1
                # Update the maximum efficiency polygon
                if self.max_efficiency < result.polygon_efficiency:
                    result.max_efficiency = result.polygon_efficiency
                    result.max_efficiency_polygon = result.count_edges
                return result

        def max_efficiency(self):
            return self.max_efficiency

        def max_efficiency_polygon(self):
            return self.max_efficiency_polygon

        def __len__(self):
            """
            Get the number of polygons in the sequence
            Returns:
                self.n-2 since first valid polygon has 3 sides always
            """
            return self._n - 2

        def __repr__(self):
            """
            __repr__() function for the PolygonIterator class object
            Returns:
                The format string with m and R information
            """
            return f'Polygons(n={self._n}, R={self._r})'

        class _polygon:
            def __init__(self, n, r):
                self._n = n
                self._r = r
                #self._max_efficiency = 0
                #self._max_efficiency_polygon = 3
                self._count_vertices = None
                self._count_edges = None
                self._area = None
                self._perimeter = None
                self._interior_angle = None
                self._apothem = None
                self._circum_radius = None
                self._side_length = None
                self._polygon_efficiency = None

            @property
            def count_vertices(self):
                """
                Count the number of vertices in the polygon as a property, i.e., Object.count_vertices
                Returns:
                    The number of vertices
                """
                if self._count_vertices == None:
                    self._count_vertices = self._n
                return self._count_vertices

            @property
            def count_edges(self):
                """
                Count the number of edges in the polygon as a property, i.e., Object.count_edges
                Returns:
                    The number of edges
                """
                if self._count_edges == None:
                    self._count_edges = self._n
                return self._count_edges

            @property
            def circumradius(self):
                """
                Get the circum radius as a property, i.e., Object.circumradius
                Returns:
                    Returns the circum radius
                """
                if self._circum_radius == None:
                    self._circum_radius = self._r
                return self._circum_radius

            @property
            def interior_angle(self):
                """
                Compute the interior angle and return as a property, i.e., Object.interior_angle
                Returns:
                    Returns the interior angle in degrees
                """
                if self._interior_angle == None:
                    self._interior_angle = (self._n - 2) * 180 / self._n
                return self._interior_angle

            @property
            def side_length(self):
                """
                Compute the length of the edges and return as a property, i.e., Object.side_length
                Returns:
                    Returns the side_length in the same units as the circum radius
                """
                if self._side_length == None:
                    self._side_length = 2 * self._r * math.sin(math.pi / self._n)
                return self._side_length

            @property
            def apothem(self):
                """
                Compute the length of the apothem nd return as a property, i.e., Object.apothem
                Returns:
                    Returns the apothem in the same units as the circum radius
                """
                if self._apothem == None:
                    self._apothem = self._r * math.cos(math.pi / self._n)
                return self._apothem

            @property
            def area(self):
                """
                Compute the area of the polygon nd return as a property, i.e., Object.area
                Returns:
                    Returns the area in the same units as the circum radius**2
                """
                if self._area == None:
                    self._area = self._n / 2 * self.side_length * self.apothem
                return self._area

            @property
            def perimeter(self):
                """
                Compute the perimeter of the polygon return as a property, i.e., Object.perimeter
                Returns:
                    Returns the apothem in the same units as the circum radius
                """
                if self._perimeter == None:
                    self._perimeter = self._n * self.side_length
                return self._perimeter

            @property
            def polygon_efficiency(self):
                """
                Compute the area efficiency (ratio of area to perimeter) for all polygons in the sequence
                and return the one with maximum efficiency
                Returns:
                    The polygon class object with maximum efficiency as a property, i.e., seqObject.max_efficiency_polygon
                """
                if self._polygon_efficiency == None:
                    self._polygon_efficiency = self.area / self.perimeter
                return self._polygon_efficiency

            def __eq__(self, other):
                """
                Checks if two given polygons (self and other) are equal.
                Equality is true when the no. of edges and circum radius are equal
                Args:
                    self - self Polygon object
                    other - other Polygon objects
                Returns:
                    Returns True if the no. of edges and circum radius are equal, else False
                """
                if isinstance(other, self.__class__):
                    return True if (self.count_edges == other.count_edges
                                    and self.circumradius == other.circumradius) else False
                else:
                    raise TypeError("other is not an instance of Polygon class")
                    # return NotImplemented

            def __gt__(self, other):
                """
                Checks if one of the given polygons (self and other) is relatively greater than the other
                Relative operator gt is true when the no. of edges is self is greater than that in other

                Args:
                    self - self Polygon object
                    other - other Polygon objects
                Returns:
                    Returns True if the no. of edges in self is greater than that of other
                """
                if isinstance(other, self.__class__):
                    return True if (self.count_vertices > other.count_vertices) else False
                else:
                    raise TypeError("other is not an instance of Polygon class")
                    # return NotImplemented

# End of file
