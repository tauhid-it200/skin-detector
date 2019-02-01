import numpy as np
import os
from PIL import Image

probabilityArray = np.zeros((256, 256, 256), dtype=float)
dataFilePath = "D:\MIT-181922\ImageProcessingTask\probability.txt"
dataFile = open(dataFilePath, 'r').read()
dataList = dataFile.split("\n")

for x in dataList:
    if x:
        temp = x.split(")")
        temp[0] = temp[0].replace("(", "").replace(" ", "")
        # temp[0] = temp[0].replace(" ", "")
        rgb = temp[0].split(",")
        r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
        probability = float(temp[1])
        probabilityArray[r, g, b] = probability

testFolderPath = "D:\MIT-181922\ImageProcessingTask\Test\\"

for filename in os.listdir(testFolderPath):
    testFilePath = testFolderPath + filename
    testFile = Image.open(testFilePath)
    testImage = testFile.load()
    [width, height] = testFile.size

    for x in range(0, width):
        for y in range(0, height):
            [r, g, b] = testImage[x, y]
            if probabilityArray[r, g, b] > 0.40:
                testImage[x, y] = (255, 255, 255)
            else:
                testImage[x, y] = (0, 0, 0)

    testFile.save(testFilePath.replace("Test", "Output"))
