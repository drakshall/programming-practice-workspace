from pathlib import Path

class InfoWrapper:                                                                                      # Intermediate class to store raw file inputs as discrete objects.

    def __init__(self, type, mod, locX, locY):
        self.type = type
        self.mod = mod
        self.locX = locX
        self.locY = locY

class InputHandler:

    def __init__(self, filename):
        self.filename = Path(__file__).parent / filename                                                # Ensures portability by avoiding absolute addresses.
        self.gridDimensions = (0, 0)
        self.rawShapeInstances = []

    def InformationScraper(self):                                                                       # This method iterates through the 2D array and compiles each type value & its modifiers into
        workingDir = self.filename                                                                      # temporary objects.
        with open(workingDir) as InputFileObject:
            yCount = 0
            xCount = 0
            for line in InputFileObject:                                                
                yCount += 1                                                                             # Counts number of lines to derive the vertical grid size.
                xCountTemp = 0                                                                         
                xIndex = 0
                print(line) 
                line = line.rstrip('\n')                                                                # Strips the newline character automatically appended to the line strings by Python.
                for character in line:                                                                  
                    xIndex += 1                                                                         # Indexes the string being iterated through.
                    if character.isalpha() == True or character.isspace() == True:                      # Tests if the character being iterated is a type value.
                        xCountTemp += 1                                                                 # Counts the number of valid type values on a given line to derive the horizontal grid size.
                        tempMod = []                                                                    
                        for characterSubset in line[xIndex:]:                                           # Uses the string index for the character iteration's type value as a position to iterate 
                            if characterSubset.isalpha() == True or characterSubset.isspace() == True:  # through the modifier value(s) associated with that type value, the presence of another type
                                self.rawShapeInstances.append(                                          # value is the signal to construct an InfoWrapper instance, append it to the raw instances
                                    InfoWrapper(character, tempMod, xCountTemp, yCount)                 # list, and move onto the next character iteration.
                                    )
                                break
                            else:
                                tempMod.append(characterSubset)                                         # Appends modifier values to a temporary list that to be encoded in an InfoWrapper instance.
                        else:
                            self.rawShapeInstances.append(                                              # The innermost loop doesn't break when it reaches the final type value in a string, the for-
                                    InfoWrapper(character, tempMod, xCountTemp, yCount)                 # else catches that exception without creating unecessary instances when the inner loop breaks.
                                    )

                if xCountTemp > xCount:                                                                 # Compares the number of characters & spaces in a line to the previously recorded highest value 
                    xCount = xCountTemp                                                                 # to find the correct horizontal size of the grid.

            self.gridDimensions = (xCount, yCount)                                                 


InputHandler1 = InputHandler("InputFile.txt")
InputHandler1.InformationScraper()
print("\n=== All Instances ===")
for i, instance in enumerate(InputHandler1.rawShapeInstances):
    print(f"Instance {i}:")
    print(f"  Type: '{instance.type}'")
    print(f"  Modifiers: {instance.mod}")
    print(f"  Position: (X={instance.locX}, Y={instance.locY})")
print(InputHandler1.gridDimensions)

