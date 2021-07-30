# Session 12 Readme file 
# Assignment details:

# Problem #1
The starting point for this project is the Polygon class and the 
Polygons sequence type we created in the previous project.
 o Goal 1:
     - Refactor the Polygon class so that all the calculated properties 
       are lazy properties, i.e. they should still be calculated properties, 
       but they should not have to get recalculated more than once 
       (since we made our Polygon class "immutable").
 o Goal 2:
     - Refactor the Polygons (sequence) type, into an iterable. 
       Make sure also that the elements in the iterator are 
       computed lazily - i.e. you can no longer use a list 
       as an underlying storage mechanism for your polygons.

# Solution - Part 1
    * The Polygon Class given and Polygon class from last assignment were named
    as Polygon() and MyPolygon()
    
    Both were tested for the tests given 

    The __repr__() function prints the following information
        * Regular polygon with {self.edges} sides and circum radius = {self.radius}')
        The class object with the following parameters initialized')
            + edges     --> No. of edges = {self.edges}
            + radius    --> circum radius = {self.radius}
            + int_angle --> Interior angle = {self.int_angle}
            + edge_len  --> length of one edge = {self.edge_len}
            + apothem   --> distance between the center and line joining two verticesi = {self.apothem}
            + area      --> area of the polygon = {self.area}
            + perimeter --> perimeter  = {self.perimeter}
            + vertices  --> No of vertices = {self.vertices}
    
    
# Solution - Part 2
    In order to make the Polygon class object as iterable, the PolygonSequence
    class object is modified as PolygonIterator Class where iter() function
    and next() function are added and the one test case checks for the iteration
    on this object.
    
    * The properties were made lazy by intializing all internal variables
      corresponding to the properties are made none and calculated once on demand
      when its value is None, otherwise, precalculated value is returned
      
    The Class PolygonSeq from last assignment is renamed as MyPolygonSeq.
    
   * The MyPolygonSeq class object initialized as follows
        self.n = n  # Maximum no. of polygon available in the sequence
        self.r = r
        self.max_eff_n = 3
        self.max_eff = 0
        self.curr_poly = n  # default polygon index
     and the maximum efficiency polygon is computed as follows
        max_eff = 0
        for i in range(3, n + 1):
            temp_poly = self._polygon(i, r)
            eff = temp_poly.area / temp_poly.perimeter
            if self.max_eff < eff:
                self.max_eff = eff
                self.max_eff_n = i
    where the getitem for each entry in the sequence is computed and cached used lru_cache
    @staticmethod
    @lru_cache(maxsize=100)
    def _polygon(s, r):
        """
        Computes the polygon of given order and radius
        Args:
            s: Polygon order
            r: Circum radius of the polygon
        Returns:
            The polygon class object
        """
        return MyPolygon(s, r)

    * The __repr__() function displays the following
        + Polygon sequence of length = {self.n} with radius = {self.r}
        + The maximum efficiency polygon is with edges = {self.max_eff_n}
        + The maximum efficiency (area/perimeter) is {self.max_eff}

# Test cases

   * The following test cases are added:
   
     o Test case 1: Checks invalid polygon order
     
     o Test case 2: Checks the function outputs and internal variables
     
     o Test case 3: Checks the computation of perimeter, side_length and area
     
     o Test case 4: Checks the computation  of apothem and interior angle 
     
     o Test case 5: Checks the computation  of apothem and interior angle for different settings
     
     o Test case 6: Checks the comparison operations
     
     o Test case 7: Checks the Polygon Sequence creation and iteration
     
     o Test case 8: Checks the Polygon iterator and iterable
     
     o Test case 9 & 10: Checks the lazy computation of properties
     
     o Test case 11: Checks the comparison of polygons which are iterable
     
     o Test case 12: Checks the individual polygons under the iterator class
     
     o Test case 13: Checks the next() function
     
     o Test case 14-22: Checks the old Polygon class from last session and docstrings for all functions, readme file contents.
     
# A readme file 
    * (this file) describes the code and solution approach and the test cases. 

# A py notebook 
    * which tests the above are given for verification in colab. 

# End of file
 