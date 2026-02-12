from behave import *
from shapes import *

@given('the program is loaded')
def step_impl(context):
    pass

@when('the program starts')
def step_impl(context):
    context.shapes = Shapes()

@then('a blank scene of size 40x20 is created')
def step_impl(context):
    assert context.shapes.width == 40
    assert context.shapes.height == 20   

@Given('the program has started')
def step_impl(context):
    context.shapes = Shapes()

@When('a rectangle with size {width}x{height} at position {x}x{y} is added')
def step_impl(context,width,height,x,y):
    context.shapes.add_shape('rectangle', int(width), int(height), int(x), int(y))

@Then('the screen will have a rectangle size {width}x{height} at position {x}x{y}')
def step_impl(context,width,height,x,y):
    context.shapes.draw()
    lines = context.shapes.get_cells()
    blank_line = ' '*40
    w = int(width)
    h = int(height)
    x = int(x)
    y = int(y)
    for i in range(y):
        assert lines[i] == blank_line

    for i in range(y, y+h):
        for j in range(x):
            assert lines[i][j] == ' '
        for j in range(x, x+w):
            assert lines[i][j] == '*'     
        for j in range(x+w, 40):
            assert lines[i][j] == ' '

    for i in range(y+h  , 20):
        assert lines[i] == blank_line