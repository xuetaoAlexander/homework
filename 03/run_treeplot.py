#!/usr/bin/env python
# coding=utf-8
import treePlotter
"""
print '>>> treePlotter.createPlot()'
treePlotter.createPlot()
print '***************************************\n'
reload(treePlotter)
print '>>> treePlotter.retrieveTree(1)'
print treePlotter.retrieveTree(1)
print '>>> myTree = treePlotter.retrieveTree(0)'
print '>>> treePlotter.getNumLeafs(myTree)'
myTree = treePlotter.retrieveTree(0)
print treePlotter.getNumLeafs(myTree)
print '>>> treePlotter.getTreeDepth(myTree)'
print treePlotter.getTreeDepth(myTree)
"""
reload(treePlotter)
myTree = treePlotter.retrieveTree(0)
print(treePlotter.createPlot(myTree))
