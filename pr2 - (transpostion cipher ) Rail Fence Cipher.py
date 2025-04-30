# Python3 program to illustrate
# Rail Fence Cipher Encryption and Decryption

def encryptRailFence(text, key):
    # create the matrix to cipher
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    # to find the direction
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        # check the direction of flow
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        # place the character
        rail[row][col] = text[i]
        col += 1
        
        # move to next row
        row += 1 if dir_down else -1
    
    # construct the cipher text
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return "".join(result)

def decryptRailFence(cipher, key):
    # create the matrix to decipher
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
    # to find the direction
    dir_down = None
    row, col = 0, 0
    
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        row += 1 if dir_down else -1
    
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    # now read the matrix in zig-zag manner
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        result.append(rail[row][col])
        col += 1
        
        row += 1 if dir_down else -1
    
    return "".join(result)

if __name__ == "__main__":
    # Encryption
    print(encryptRailFence("attack at once", 2))
    print(encryptRailFence("HOWAREYOU", 2))
    print(encryptRailFence("defend the wall", 3))
    
    # Decryption
    print(decryptRailFence("atc toctaka ne", 2))
    print(decryptRailFence("HWRYUOAEO", 2))
    print(decryptRailFence("dnhaweedtees alf tl", 3))
