import numpy as np
import os
from PIL import Image

skinArray = np.zeros((256, 256, 256), dtype=float)
nonSkinArray = np.zeros((256, 256, 256), dtype=float)
probabilityArray = np.zeros((256, 256, 256), dtype=float)

originalFilesPath = "D:\MIT-181922\ImageProcessingTask\IBTD\Original\\"
maskFilesPath = "D:\MIT-181922\ImageProcessingTask\IBTD\Mask\\"

for filename in os.listdir(originalFilesPath):
    originalImagePath = originalFilesPath + filename
    originalImageFile = Image.open(originalImagePath, "r")
    originalImage = originalImageFile.load()
    maskImagePath = maskFilesPath + filename.replace("jpg", "bmp")
    maskImageFile = Image.open(maskImagePath, "r")
    maskImage = maskImageFile.load()
    [width, height] = maskImageFile.size

    for x in range(0, width):
        for y in range(0, height):
            [r, g, b] = maskImage[x, y]
            if r > 220 and g > 220 and b > 220:
                [r, g, b] = originalImage[x, y]
                nonSkinArray[r, g, b] += 1
            else:
                skinArray[r, g, b] += 1

skinArraySum = np.sum(skinArray)
nonSkinArraySum = np.sum(nonSkinArray)
skinProbabilityArray = np.array(skinArray) / skinArraySum
nonSkinProbabilityArray = np.array(nonSkinArray) / nonSkinArraySum

for index, value in np.ndenumerate(probabilityArray):
    if nonSkinProbabilityArray[index] > 0:
        probabilityArray[index] = round(skinProbabilityArray[index] / nonSkinProbabilityArray[index], 4)
    else:
        probabilityArray[index] = 0.0000

outputFilePath = "D:\MIT-181922\ImageProcessingTask\probability.txt"
outputFile = open(outputFilePath, "w")

for index, value in np.ndenumerate(probabilityArray):
    strIndex = str(index)
    outputFile.write(strIndex)
    outputFile.write(" ")
    strValue = str(value)
    outputFile.write(strValue)
    outputFile.write("\n")
