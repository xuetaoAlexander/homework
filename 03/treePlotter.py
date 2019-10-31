#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
 
 
# 定义文本框和箭头格式
decisionNode = dict(boxstyle = "sawtooth", fc = "0.8") # fc 应该是颜色深浅
leafNode = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")
 
 
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    # centerPt 箭头指向坐标， parentPt 箭头终点坐标
    createPlot.ax1.annotate(nodeTxt, xy = parentPt,\
    xycoords = 'axes fraction',\
    xytext = centerPt, textcoords = 'axes fraction',\
    va = "center", ha = "center", bbox = nodeType, arrowprops = arrow_args)
 

def plotMidText(cntrPt, parentPt, txtString): # 在父子节点间填充文本信息 
    # 计算父节点和子节点的中间位置
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)
 
 
def plotTree(myTree, parentPt, nodeTxt): # 计算树的宽与高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW,\
                            plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt) # 标记子节点属性值
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD # 减少 y 偏移
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),\
                cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks = [], yticks = [])
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree)) # 储存树的宽度
    plotTree.totalD = float(getTreeDepth(inTree)) # 储存树的深度
    plotTree.xOff = -0.5 / plotTree.totalW; plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
