'''
name: Jack Pauley
discription: this code takes in a certain set of peramiters and gives you the amount of money you owe to the post office to ship a package
log:1.0
bugs:doesn't print the right numbers depending on what numbers are inputed 
Bonus features: None
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
    elif size == "large postcard": 
        return .37+.03*distance 
    elif size == "Envelope": 
        return .37+.04*distance 
    elif size == "Large Envelope": 
        return .60+.05*distance 
    elif size == "Package": 
        return 2.95+.25*distance 
    elif size == "Large Package": 
        return 3.95+.35*distance 

def get_zone(zipcode):
    '''
    finds the zone based on the inputed zipcodes

    Args:
        (zipcode) if the zipcode is greater than user input and less than user inputed zipcode
    Returns:
        returns which zone it will be put into
    Raises:
        (value error) if the input is a negitive or greater than 99999
    '''
    if 1<= zipcode <= 6999: 
        return 1 
    elif 7000<= zipcode <= 19999: 
        return 2 
    elif 20000<= zipcode <= 35999: 
        return 3 
    elif 36000<= zipcode <= 62999: 
        return 4 
    elif 63000<= zipcode <= 84999:
        return 5
    elif 85000<= zipcode <= 99999:
        return 6 

def getType(L, H, W):   
    '''
    finds the package type

    Args: (getType) if the length is within certain bounds, if width is within certain bounds, if height is within certain bounds

    Returns:
        returns the package type to the user based on the user input
    Raises:
        (value error)if the dimmensions are negitive or greater then the largest package
    '''
    if (L >=3.5 and L<=4.25 and W >=0.007 and W <=0.016 and H >=3.5 and H <=6): 
        return "Postcard" 
    elif (L >=4.25 and L<= 6 and W >=0.007 and W <= 0.015 and H >=6 and H <= 11.5): 
        return  "Large postcard" 
    elif (L >=3.5 and L<=6.125 and W >= 0.016 and W <= 0.25 and H >=5 and H <= 11.5): 
        return "Envelope" 
    elif (L >= 6.125 and L <= 24 and W >=0.25 and W <=0.5 and H >= 11 and H <=18): 
        return "Large Envelope"
    elif (L+2*H+2*W<=84):
        return "Package" 
    elif (L+2*H+2*W<=130):
        return "Large Package"  
    else:
        print("doesn't meet any package requirments. Not Mailable") 
