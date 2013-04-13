"""

Team 4 
< Coding Standards />

Language: Python v2.7

***NOTE: Coding standards below are explained to an 
         experienced Python programmer. Some certain
         details are being left out assuming that further
         explaination is not necessary as this should be read
         by experienced Python programmers.

"""
#=====================
# methods
#=====================
# main method:
def main():
    print "Main method"

# calling method below
main()

# method names:
nameMethodsWithCamelCase()

# access methods:
# always start method name with "get"
getValueNameHere()

# mutator methods:
# always start method name with "set"
setValueNameHere()

#=====================
# Classes
#=====================

# class example below: 
class Vertex:
    def __init__(self, key, color = 'white', dist = 0, pred = None):
        self.id = key
        self.connectedTo = {}
        self.color = color
        self.predecessor = pred
        self.distance = dist
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setColor(self, newColor):
        self.color = newColor
        
#=====================
# Variables
#=====================

useCamelCaseForVariableNames

CONSTANT_VALUES_IN_THIS_FORMAT

#=====================
# Indentation
#=====================
# Indentation will be done in the Python standard of 4 spaces
# Use SPACES NOT TABS for your indentation*
# *Most/all IDEs can be set to use spaces instead of tabs in the settings of IDE

#=====================
# Commenting
#=====================
# Always do class wide descriptions explaining the purpose
# of the class. What it's responsibilities are, features it
# includes, helpful information, and assumptions.

# Make long variable and method names to fully describe the
# variable or method as best as possible to avoid excessive
# commenting. Comment only when you feel that a stranger to 
# the code will wonder why you did some action.

# In all source code, include references to all of the example
# code, library links, etc to all code used in this project. 
# Give thanks for thanks is due.

#=====================
# Git
#=====================
# Committing:
# Git commits are meant to highlight tasks completed. After each task
# that you complete such as "added ability for user to add email addresses"
# make a commit to git. Do not make commits "just coded the past 3 hours"
# Commit too much rather then too little.








