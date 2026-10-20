# Inherit the above class to create a "3Dpoint" with additional attribute z. 
# Override the method defined in "2DPoint" class , to calculate distance between two points of the "3DPoint" class


import math


class Point2D:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"2DPoint({self.x}, {self.y})[cite: 1]"

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Point3D(Point2D):

  def __init__(self, x, y, z):
    super().__init__(x, y)  # Inheriting x and y attributes from Point2D
    self.z = z

  def __str__(self):
    return f"3DPoint({self.x}, {self.y}, {self.z})[cite: 1]"

  def distance(self, other):  # Overriding the distance method for 3D points
    return math.sqrt(
        (self.x - other.x) ** 2
        + (self.y - other.y) ** 2
        + (self.z - other.z) ** 2
    )


# --- Test / Example Usage ---
if __name__ == "__main__":
  print("=== Practical 14 Test Execution ===")

  # Creating two 3DPoint objects
  p1 = Point3D(1, 2, 3)
  p2 = Point3D(4, 6, 8)

  # Displaying the points using __str__
  print("First Point:", p1)
  print("Second Point:", p2)

  # Calculating and printing the distance using the overridden method
  dist = p1.distance(p2)
  print(f"Distance between 3D points: {round(dist, 2)}")