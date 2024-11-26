# -*- coding: utf-8 -*-
"""
JobCode : F1C
JobDes  : Final LAB F1C 

StudID  : 6710301021
StudName: Sirawit Wirayaarthon
Date    : 2024-10-03
"""
import math

#*****************************
#***** class TriangleSet *****
#*****************************
class TriangleSet:
    """class for Triangle Set """
    def __init__(self, triCode, sizeA, sizeB, sizeC, area ):
        """Constructor Method to create TriangleSet instance """
        #*** Created by Student  
        self._triCode = triCode
        self._sizeA = sizeA
        self._sizeB = sizeB
        self._sizeC = sizeC
        self._area = area


    def __str__(self):
        #*** Created by Student    
        return f'{self._:4}{self._sizeA:10}{self._sizeB:4}{self._sizeC:4}{self._area:4}'


#***** Read Triangle File To triangle Memory *****
def triangleFile2TriMem(inFN):
    """ Read inFN(File) return trCol(Column), triMem(Memory) """    
    #*** Created by Student
    fin = open(inFN, 'r')

    trMem = []
    l = 0
    with fin:
        for wlRec in fin:
            triCode, sizeA, sizeB, sizeC, area = wlRec.split()

            if l:
                sizeB = int(sizeB)
                sizeC = int(sizeC)
                area = sizeB*sizeC
                trMem.append(TriangleSet(triCode, sizeA, sizeB, sizeC, area))          
            else:
                trCol = f'{triCode:6}{sizeA:16}{sizeB:>8}{sizeC:>6}{area:>10}'

            l += 1

    return trCol, trMem ,area


#***** Show All Triangle Memory *****
def showAlltriMem(trCol, trMem):
    """ Show All trMem(TriangleMem) return Total data, trQty, notrQty """
    #*** Created by Student 
    Total_Data = 0
    
    for mSet in trMem:
        Total_Data += mSet.area
        totData = Total_Data
        
    return totData, trQty, notrQty

# def totAlltriMem(trMem):
#     """ trMem(TriangleMem) return Total data, trQty, notrQty """
#     #*** Created by Student    
#     #*** ....
#     #*** ....
        
#     return totData, trQty, notrQty


# ***** Write Triangle Memory to File *****
def trMemToTriangleFile(trCol, trMem, outFN):
    """ Write trMem to Triangle file """
    fout = open(outFN, 'w')
    fout.write(trCol, trMem, outFN)
          
    return


# *************************************
# ***** subroutine from FlowChart *****
# *************************************
def bigAndSmall(a, b):
 #   """ return small, big"""
    #*** Created by Student  
    if a<b:
        big = b
        small = a
           
    else:
        big = a
        small = b

    return (small, big)

def biggestOfThree(a, b, c):
 #   """ return s1,s2,s3 that s3 is the biggest """   
    #*** Created by Student    
    s1, s2 = bigAndSmall(a, b)
    s2, s3 = bigAndSmall(s2, c)

    return (s1, s2, s3)

def isZero(a, b, c):
 #   """ return iz is qty of zero """   
    #*** Created by Student    
    iz = 0
    if a ==0 :
        iz += 1
    else:
        if b == 0:
            iz += 1
        else:
            if c == 0:
                iz += 1
                    
    return iz

def isNotTriangle(a, b, c):
 #   """ return ierr, errcode = 1,2,3,4 is not triangle """
    #*** Created by 
    ierr = isZero(a, b, c)
    if ierr == 0:
        s1, s2, s3 = biggestOfThree(a, b, c)
        
        if s3 >= (s1 + s2):
            ierr = 4
    

    return ierr

def trueTriangleArea(a, b, c):
    #""" return Cal. Triang;e Area from a, b, c """
    #*** Created by Student    
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))

 
    return area

def allTriangleArea(a, b, c):
 #   """ return Cal. Triang;e Area from a, b, c """
    #*** Created by Student    
    ierr = isNotTriangle(a, b, c)
    if ierr == 0:
        area = trueTriangleArea(a, b, c)
    else:
        if ierr == 1:
            area = -991
        else:
            if ierr == 2 :
                area = -992
            else:
                if ierr == 3:
                    area = -993
                else:
                    if ierr == 4:
                        area = -994
                    else:
                        area = -999
                    
                        
    return area

if __name__ == "__main__":
#********************
#*** Main Program ***
#********************
    inFN = 'InputData.txt'
    
    
# **** Test def bigAndSmall(a,b) ***
    x = 10
    y = 2 
    sm, bg = bigAndSmall(x, y)
    print(f'    x,   y = {x:8.2f},{y: 8.2f}')
    print(f'Small, Big = {sm:8.2f},{bg:8.2f}')
# **** end  Test ****

#**** Test def biggestOfThree(a, b, c) ***
    x = 15
    y = 10
    z = 25
    s1, s2, s3 = biggestOfThree(x, y, z)
    print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
    print(f's1, s2, s3 = {s1:8.2f},{s2:8.2f},{s3:8.2f}')
#**** end  Test ****

#**** Test def isZero(a, b, c) ***
    x = 20
    y = 0.0
    z = 0.15
    izero = isZero(x, y, z)
    print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
    print(f'There are {izero}')
#**** end  Test ****

#**** Test def isNotTriangle(a, b, c)  ***
    a = 3
    b = 4
    c = 5
    ierr = isNotTriangle(a, b, c)
    print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
    if ierr == 0:
        print(f'This is Triangle')
    else:
        print(f'This is not Triangle')
        
    print(f'ierr = {ierr}')
#**** end  Test ****

#**** Test def allTriangleArea(a, b, c)  ***
    a = 1
    b = 2
    c = 3
    area = allTriangleArea(a, b, c)
    print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
    if area > 0:
        print(f'\nThis is Triangle')
    else:
        print(f'\nThis is not Triangle')
        
    print(f'area = {area:8.2f}')
#**** end  Test ****

# **** Test Input, Output File from class TriangleSet:
    inFN = 'InputDataTest.txt'

    trCol, trMem = triangleFile2TriMem(inFN)
    totData, trQty, notrQty = showAlltriMem(trCol, trMem)
    print(f'\nTotal Data     = {totData:6,}')
    print(f'Total Triangle = {trQty:6,}')
    print(f'Total not Tri. = {notrQty:6,}')
    print(f'------ end ------')
    
    outFN = 'OutputData.txt'
    trMemToTriangleFile(trCol, trMem, outFN)
# **** end  Test ****
# Hello 