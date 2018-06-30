import time
image = [[60, 150, 3], [0, 15, 90], [255, 255, 251], [60, 25, 111], [60, 25, 110], [60, 250, 30], [150, 250, 150], [60, 25, 111],[60, 150, 3], [0, 5, 90], [60, 25, 121], [60, 25, 130],[60, 25, 9], [60, 150, 5],[60, 150, 9], [80, 150, 250], [60, 25, 109], [60, 150, 1], [60, 25, 113], [0, 0, 6]]
print(len(image))
print()
for index in range(0, len(image)):
    red = image[index][0]
    temp = image[index]
    position = index
    ## do insertion sort for red values
    while (( position > 0 ) and (image[position - 1][0] > red)):
        image[position] = image[position-1]
        position = position - 1
        image[position] = temp
        print(image)
        print()
        ## switch indexes of pixels based on green values
        for Index in range(1, len(image)):
            if image[Index][0] == image[Index - 1][0]:
                if(image[Index-1][1] > image[Index][1]):
                   temp2 = image[Index]
                   image[Index] = image[Index-1]
                   image[Index-1] = temp2
        ## switch indexes of pixels based on blue values
        for Index in range(1, len(image)):
            if image[Index][0] == image[Index - 1][0] and image[Index][1] == image[Index-1][1]:
                if(image[Index-1][2] > image[Index][2]):
                    temp2 = image[Index]
                    image[Index] = image[Index-1]
                    image[Index-1] = temp2
            elif image[Index][0] == image[Index - 1][0] and image[Index-1][1] > image[Index][1]:
                Temp = image[Index]
                image[Index] = image[Index - 1]
                image[Index - 1] = Temp
        
        time.sleep(1)
        print(image)
        print()
