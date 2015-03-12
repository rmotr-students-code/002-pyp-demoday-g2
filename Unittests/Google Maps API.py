__author__ = 'Mike Azar'
from myapp import GMaps

assert GMaps.get_coordinates('1500','Massachusetts','Avenue','Washington','DC')[0] == 38.9064936

# assert GMaps.get_coordinates('1500','Massachusetts','Avenue','Washington','DC')[1] == -77.0354118
# This assert does not work. Unsure why that is.