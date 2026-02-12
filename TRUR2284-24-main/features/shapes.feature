Feature: The Shapes program

  Scenario: Program startup
     Given the program is loaded
      When the program starts
      Then a blank scene of size 40x20 is created

  Scenario Outline: Adding a rectangle to a blank screen
    Given the program has started
      When a rectangle with size <width>x<height> at position <x>x<y> is added
      Then the screen will have a rectangle size <width>x<height> at position <x>x<y>

    Examples: Unclipped shapes
     | width | height | x | y |
     | 1     | 1      | 0 | 0 |
     | 2     | 2      | 1 | 1 |