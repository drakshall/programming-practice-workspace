from cmath import rect
import unittest
from shapes import *
import io
from contextlib import redirect_stdout

class TestScreen(unittest.TestCase):

    def test_create_screen(self):
        screen =  Screen(5, 8)
        self.assertEqual(screen.width, 5) 
        self.assertEqual(screen.height, 8)
        self.assertEqual(len(screen.cells),8)   # is this part of the public API?
        self.assertEqual(len(screen.cells[0]),5)   # is this part of the public API?
    
    def test_the_str_method_of_a_blank_screen_creates_a_string_with_spaces_separeted_by_newlines(self):
        screen =  Screen(5, 10)
        self.assertEqual(str(screen), (" " * 5 + "\n") * 10)

class TestRectangle(unittest.TestCase):
        def test_create_a_rectangle(self):
            foo = Rectangle(3, 2, 1, 1)
            foo.width == 3
            foo.height == 2
            foo.x == 1
            foo.y == 1
    
        def test_rectangle_outside_screen_draws_nothing(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(3, 2, 6, 6)
            # act
            rect.draw(screen)
            # assert
            expected = (
                "     \n"
                "     \n"
                "     \n"
                "     \n"
                "     \n"
            )
            self.assertEqual(str(screen), expected)
            
        def test_rectangle_on_enclosing_screen_draws_fills_in_stars(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(3, 2, 1, 1)
            # act
            rect.draw(screen)
            # assert
            expected = (
                "     \n"
                " *** \n"
                " *** \n"
                "     \n"
                "     \n"
            )
            self.assertEqual(str(screen), expected)

        def test_rectangle_draw_overlapping_right_edge(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(7, 2, 1, 1)
            # act
            rect.draw(screen)
            # assert
            expected = (
                "     \n"
                " ****\n"
                " ****\n"
                "     \n"
                "     \n"
            )
            self.assertEqual(str(screen), expected)

        def test_rectangle_draw_overlapping_left_edge(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(5, 2, -1, 1)
            # act
            rect.draw(screen)
            # assert
            expected = (
                "     \n"
                "**** \n"
                "**** \n"
                "     \n"
                "     \n"
            )
            self.assertEqual(str(screen), expected)

        def test_rectangle_draw_overlapping_top_edge(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(3, 2, 1, -1)
            # act
            rect.draw(screen)
            print()
            print("-----")
            print(screen)
            # assert
            expected = (
                " *** \n"
                "     \n"
                "     \n"
                "     \n"
                "     \n"
            )
            self.assertEqual(str(screen), expected)

        def test_rectangle_draw_overlapping_bottom_edge(self):
            # arrange
            screen = Screen(5, 5)
            rect = Rectangle(3, 2, 1, 4)
            # act
            rect.draw(screen)
            print()
            print("-----")
            print(screen)
            # assert
            expected = (
                "     \n"
                "     \n"
                "     \n"
                "     \n"
                " *** \n"
            )
            self.assertEqual(str(screen), expected)

class TestStars(unittest.TestCase):

    # normal value tests
    def test_stars_produces_a_string_with_works_with_positive_arguments(self):
        self.assertEqual(stars(1), '*')
        self.assertEqual(stars(2), '**')
        self.assertEqual(stars(5), '*****')

    # boundary value test
    def test_stars_method_produces_an_empty_string_with_zero_argument(self):
        self.assertEqual(stars(0), '')

    # erronous test
    def test_stars_method_produces_an_empty_string_with_one_argument(self):
        self.assertEqual(stars(-1), '')

class TestShapes(unittest.TestCase):
    def setUp(self):
        self.shapes = Shapes()
    
    def test_creation(self):
        self.assertEqual(self.shapes.screen.width, 40)
        self.assertEqual(self.shapes.screen.height, 20)
        self.assertEqual(len(self.shapes.screen.cells), 20)
        self.assertEqual(len(self.shapes.shapes), 0)

    # Uses the contextLib to redirect stdout
    def test_draw_with_a_blank_screen(self):
        with redirect_stdout(io.StringIO()) as f:
            self.shapes.draw()
        s = f.getvalue()
        self.assertEqual(s, (" " * 40 + "\n") * 20)

    def test_add_rectangle(self):
        self.shapes.add_shape("rect",10,10,15,5)
        self.shapes.render()


