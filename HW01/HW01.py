import unittest
import math

def classify_triangle(a, b, c):
    triangles = 'This triangle is: '
    #Check if equilateral
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b and b == c and a == c:
            triangles += 'equilateral '
        #Check if isosceles
        if (a == b or b == c or a == c) and not(b == c and a == b):
            triangles += 'isosceles '
        #check if scalene
        if a != b and b != c and a != c:
            triangles += "scalene "
        #check if right
        if (a*a) + (b*b) == (c*c):
            triangles += "and right"
    else:
        triangles += "not a triangle"
    return triangles

class classify_triangle_test(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), 'This triangle is: equilateral ')
        self.assertEqual(classify_triangle(7, 7, 7), 'This triangle is: equilateral ')
        self.assertEqual(classify_triangle(2, 2, 2), 'This triangle is: equilateral ')
        self.assertNotEqual(classify_triangle(2, 3, 4), 'This triangle is: equilateral ')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'This triangle is: equilateral ')
        self.assertNotEqual(classify_triangle(5, 6, 7), 'This triangle is: equilateral ')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 5), 'This triangle is: isosceles ')
        self.assertEqual(classify_triangle(4, 4, 7), 'This triangle is: isosceles ')
        self.assertEqual(classify_triangle(2, 2, 3), 'This triangle is: isosceles ')
        self.assertNotEqual(classify_triangle(6, 6, 6), 'This triangle is: isosceles ')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'This triangle is: isosceles ')
        self.assertNotEqual(classify_triangle(5, 5, 5), 'This triangle is: isosceles ')

    def test_isoscelesright(self):
        self.assertEqual(classify_triangle(1, 1, 2**0.5), 'This triangle is: isosceles and right')
        self.assertEqual(classify_triangle(6.5, 6.5, 9.19238815543), 'This triangle is: isosceles and right')
        self.assertNotEqual(classify_triangle(4, 5, 6), 'This triangle is: isosceles and right')
        self.assertNotEqual(classify_triangle(3, 3, 3), 'This triangle is: isosceles and right')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'This triangle is: isosceles and right')

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'This triangle is: scalene ')
        self.assertEqual(classify_triangle(6, 7, 8), 'This triangle is: scalene ')
        self.assertEqual(classify_triangle(2, 3, 4), 'This triangle is: scalene ')
        self.assertNotEqual(classify_triangle(3, 3, 3), 'This triangle is: scalene ')
        self.assertNotEqual(classify_triangle(4, 4, 7), 'This triangle is: scalene ')
        self.assertNotEqual(classify_triangle(2, 2, 2), 'This triangle is: scalene ')

    def test_scaleneright(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'This triangle is: scalene and right')
        self.assertEqual(classify_triangle(5, 12, 13), 'This triangle is: scalene and right')
        self.assertEqual(classify_triangle(9, 12, 15), 'This triangle is: scalene and right')
        self.assertNotEqual(classify_triangle(5, 4, 3), 'This triangle is: scalene and right')
        self.assertNotEqual(classify_triangle(2, 3, 4), 'This triangle is: scalene and right')
        self.assertNotEqual(classify_triangle(5, 6, 7), 'This triangle is: scalene and right')
        self.assertNotEqual(classify_triangle(1, 2, 3), 'This triangle is: scalene and right')

    def test_NotTriangle(self):
        self.assertEqual(classify_triangle(3, 2, 8), 'This triangle is: not a triangle')
        self.assertEqual(classify_triangle(1, 2, 7), 'This triangle is: not a triangle')
        self.assertEqual(classify_triangle(4, 3, 9), 'This triangle is: not a triangle')
        self.assertNotEqual(classify_triangle(3, 3, 3), 'This triangle is: not a triangle')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'This triangle is: not a triangle')
        self.assertNotEqual(classify_triangle(2, 3, 4), 'This triangle is: not a triagle')

if __name__ == "__main__":
    unittest.main()
