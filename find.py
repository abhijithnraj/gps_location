import sys
z=sys.argv[1].split()
accuracy=float(z[-1].strip("accuracy="))
open("got.txt","w").write(sys.argv[1])
locator_string=z[3].strip("lat=")+","+z[2].strip("lon=")
#print(locator_string)
#print(accuracy)

#if accuracy<100:
#	print "ok"
#else:
#	print "not okay"

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse(locator_string)
print(location)
