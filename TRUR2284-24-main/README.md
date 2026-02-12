# Code for the TRUR2284 Software Testing unit at Truro and Penwith College

# Scenario

TruroTech are developing a series of retro games, using ascii art made up of a collection of geometric shapes. TruroTech want you to develop
a program to create such scenes.

# User stories

These should be given from a users perspective, each specify something a user wants to acheive from the program. These should not depend on the actual implementation details.

1. As a retro game developer I want to start with a blank screen of given size
2. As a retro game developer I want to select a range of different shapes, specify their size and position and add it to an existing scene
3. As a retro game developer I want to output the current scene  

# Revised user stories

1. As a retro game developer I want to start with a blank screen of given size
2a. As a retro game developer I want to select a shape from a range of possibilities
2b. As a retro game developer, when shape is select I want to specify its size and position
2c. As a retro game developer, when shape, size and position is selected I want to add it to an existing scene
3. As a retro game developer I want to output the current scene  

# Acceptance criteria

"notes about what the story must do in order for the product owner to accept it as complete" they can be written in Given-When-Then format
or as a set of bullet points.

1. GIVEN the program has started WHEN the user specifies a size and shape THEN a blanks sceen is created
2. GIVEN the program has started THEN a menu of options is presented including the possible shapes AND an option to display the current scene
3. GIVEN the menu is displayed WHEN the user selects a shape THEN a prompt for the size and position is displayed
4. GIVEN a prompt for size and shape is displayed WHEN the user enters the data THEN a shape is created AND it is added to the sceen
5. GIVEN the menu is displayed WHEN the user selects the option to display the scene THEN the scene is printed


