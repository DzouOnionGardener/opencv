def SortColor(image):
    for index in range(1, len(image)):
        red = image[index][0]
        temp = image[index]
        position = index
        ## do insertion sort on red values
        while((position > 0) and (image[position - 1][0] > red)):
            image[position] = image[position - 1]
            position = position - 1
        image[position] = temp
        print()
        ## sort green values
        for Index in range(1, range(image)):
            if(image[Index - 1][0] == image[Index][0]):
                if(image[index-1][1] > image[Index][1]):
                    temp2 = image[Index]
                    image[Index] = image[Index - 1]
                    image[Index - 1] = temp2
        ## sort blue values
        for Index in range(1, range(image)):
            if ((image[Index - 1][0] == image[Index][0]) and (image[Index-1][1] == image[Index][1])):
                if(image[Index-1][2] > image[Index][2]):
                    temp2 = image[Index]
                    image[Index] = image[Index - 1]
                    image[Index - 1] = temp2