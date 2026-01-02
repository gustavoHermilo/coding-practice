#  Exercise   Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    #
    # We divide the liters used by 3.785... (the amount of liters in one US gallon)
    gallon=liters/3.785411784     # 1 American mile = 1609.344 metres;
                                                  #1 American gallon = 3.785411784 litres.
    #  Convert the 100km distance into Miles
    # (100km * 1000m) converts km to meters, then we divide by meters-per-mile
    miles= (100*1000)/ 1609.344
                                                 # Miles divided by Gallons tells us how far we go on one unit of fuel
    return miles/gallon
    

def miles_gallon_to_liters_100km(miles):
    
    liters=1*3.785411784     # 1 American mile = 1609.344 metres;
                                                  #1 American gallon = 3.785411784 litres.
    # Define the fuel amount as exactly 1 US Gallon (in liters)
    hundred_kilometers= (miles* 1609.344)/(1000*100)
    # (miles * meters-per-mile) gives total meters, then divided by 100,000 meters (which is 100km
    return liters/hundred_kilometers
    # Total liters used divided by how many "100km units" were traveled
    #
