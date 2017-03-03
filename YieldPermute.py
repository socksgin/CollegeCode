def permute(inputData, outputSoFar):
    for elem in inputData:
        if elem not in outputSoFar:
            outputSoFar.append(elem)
            if len(outputSoFar) == len(inputData):
                print (outputSoFar)
            else:
                permute(inputData, outputSoFar)  # --- Recursion
            outputSoFar.pop()

permute([1, 2, 3, 4, 5], [])
