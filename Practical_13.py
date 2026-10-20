#Write a program to define a class "2DPoint" with coordinates x and y as attributes.
# Create relevant methods and print the objects.
# Also define a method distance to calculate the distance between any two point objects. 


import math


class Point2D:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"2DPoint({self.x}, {self.y})[cite: 1]"

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# --- Test / Example Usage (Required to see output) ---
if __name__ == "__main__":
  print("=== Practical 13: 2DPoint Output ===")
  p1 = Point2D(2, 3)
  p2 = Point2D(5, 7)
  print("Point 1:", p1)
  print("Point 2:", p2)
  print(
      "Distance between 2D points:", round(p1.distance(p2), 2)
  )  #[cite: 1]
