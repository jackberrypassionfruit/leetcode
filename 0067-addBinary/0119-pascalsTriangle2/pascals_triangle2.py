def getRow(rowIndex):
  
  
  """ My idea
    - Lay Pascal's triangle on its side
    - notice that each column has a sequence with a pattern
    - the number in each row is just the successive sum of all of the numbers that came before it, and...
    - the numbers that come before it all increment by a number that grow at an increasing rate.
    - in fact, that rate is increasing at a higher order, depedning on the index that it is in the array.
    - THis is kind of like the test to determine the order of a polynomial function
    - use this fact to non-iteratively calculate each successive sum of each series, and populate each row of the triangle
  
  """