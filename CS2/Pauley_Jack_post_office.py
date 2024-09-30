'''
name: Jack Pauley
discription
log
bugs:
features
sources:https://www.geeksforgeeks.org/subtract-two-numbers-in-python/ 
'''

def main():
    data = input("Enter data in the order of Length,Width,Heigt and starting and ending zipcode")
    dimensions = data.split(",")
    L = float(dimensions[0]) 
    W = float(dimensions[1]) 
    H = float(dimensions[2]) 
    start = int(dimensions[3]) 
    end = int(dimensions[4])
    
    

    size = getType(L,H,W)
    distance = abs(get_zone(start)- get_zone(end))
    print(f'{get_cost(size,distance)}') 

def get_cost (size,distance): 
    '''
    calculates the cost depending on what type of package.

    Args:
        (size,distance): if the size of the package is equal to the package type charge the user depending on the size times the distance traveled
    Returns:
        returns final price of package
    Raises:
        (value error) if the size of package is to large or to small or there is negitive distances travled
    '''
    if size == "Postcard": 
        return .20+.03*distance  
    elif size == "large postcard": # if the size is equal to the dimensions of the large postcard
        return .37+.03*distance # return .37 plus .03 times the distance it travels, returns the final output
    elif size == "Envelope": # if the size is equal to the dimensions of the envlope
        return .37+.04*distance # return .37 plus .04 times the distance it travels, returns the final output
    elif size == "Large Envelope": # if the size is equal to the dimensions of the large envelope
        return .60+.05*distance # return .60 plus .05 times the distance it travels, returns the final output
    elif size == "Package": # if the size is equal to the dimensions of the package
        return 2.95+.25*distance # return 2.95 plus .25 times the distance it travels, returns the final output
    elif size == "Large Package": # if the size is equal to the dimensions of the large package
        return 3.95+.35*distance # return 3.95 plus .35 times the distance it travels, returns the final output

def get_zone(zipcode):# defines the get zone function and the zipcode
    if 1<= zipcode <= 6999: # if the zip code is more then one and less then 6999
        return 1 # return zone 1
    elif 7000<= zipcode <= 19999: # if the zipcode is more then 7000 and less that 1999
        return 2 # returns zone 2
    elif 20000<= zipcode <= 35999: # if the zipecode is more than 20000 and less than 35999
        return 3 # returns zone 3
    elif 36000<= zipcode <= 62999: # if the zipcode is more than 36000 and less than 62999
        return 4 # returns zone 4
    elif 63000<= zipcode <= 84999:# if the zipecode is more than 63000 and less than 84999
        return 5# returns zone 5
    elif 85000<= zipcode <= 99999:# if the zipcode is more than 85000 and less than 99999
        return 6 # returns zone 6

def getType(L, H, W):   # defines getType and L,W,H
    if (L >=3.5 and L<=4.25 and W >=0.007 and W <=0.016 and H >=3.5 and H <=6): # if length is greater than or equal to 3.5 and less than or equal to 4.25. if the width is greater than or equal to .007 and less than or equal to .016. if the height is greater than or equal to 3.5 and less than or equal to 6
        return "Postcard" # returns the package type
    elif (L >=4.25 and L<= 6 and W >=0.007 and W <= 0.015 and H >=6 and H <= 11.5): # if length is greater than or equal to 4.25 and less or equal to than 6. if the width is greater than or equal to .007 and less than or equal to .015. if the height is greater than or equal to 6 and less than or equal to 11.5
        return  "Large postcard" # returns the package type
    elif (L >=3.5 and L<=6.125 and W >= 0.016 and W <= 0.25 and H >=5 and H <= 11.5): # if length is greater than or equal to 3.5 and less than or equal to 6.125. if the width is greater than or equal to .016 and less than or equal to .25. if the height is greater than or equal to 5 and less than or equal to 11.5
        return "Envelope" # returns the package type
    elif (L >= 6.125 and L <= 24 and W >=0.25 and W <=0.5 and H >= 11 and H <=18): # if length is greater or equal to than 6.125 and less or equal to than 24. if the width is greater than or equal to .25 and less than or equal to .5. if the height is greater than or equal to 11 and less or equal to than 18
        return "Large Envelope"# returns the package type 
    elif (L+2*H+2*W<=84):# if the length plus two times height plus two times width is less than or equal to 84
        return "Package" # return the package type
    elif (L+2*H+2*W<=130):# if the length plus two times height plus two times width is less than or equal to 130
        return "Large Package" # returns 
    else:
        print("doesn't meet any package requirments. Not Mailable") # prints the phrase within the qoutations
main() # calls main function