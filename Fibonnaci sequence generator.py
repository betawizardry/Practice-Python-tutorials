#program that asks the user how many fibonnaci numbers to generate
#then prints them as a list

def Fibonnaci(usernum):
    '''
    generates a list of fibonnaci numbers in sequence
    for as many numbers as the usernum.
    usernum must be a positive integer
    '''
    Fibnum = [1,1]
    count = 1
    if usernum == 1:
        return Fibnum[0]
    elif usernum == 2:
        return Fibnum
    
    else:
        while count < usernum-1:
            x = Fibnum[count-1] + Fibnum[count]
            Fibnum.append(x)
            count += 1    
        return Fibnum
