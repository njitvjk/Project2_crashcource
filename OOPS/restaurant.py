class Restaurant:
    """A simple method to represent a Car"""

    def __init__(self, name, cuisine_type, location):
        """Initialize attributes to describe a restaurant """
        # data members (instance variables)
        print('Inside Constructor')
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.restaurant_location = location
        # setting a default value for attribute
        self.restaurant_rating = 0
        print('All variables initialized')

    # Behavior (instance methods)
    def get_descriptive_name(self):

        """Return a neatly formatted descriptive name """
        long_name = f"{self.restaurant_name} {self.cuisine_type} {self.restaurant_location} "
        return long_name.title()

    # Behavior (instance methods)
    def read_restaurant_rating(self):
        """Print a statement showing car mileage"""
        print(f"This restaurant has rating {self.restaurant_rating} ")

    def update_restaurant_rating(self, rating):
        """modifying an attribute's value through method"""
        self.restaurant_rating = 4


# Make an instance and call method of class
# create object of a class
restaurant = Restaurant('SPICES', 'Indian_cuisine', 'Jersey City')
print(restaurant.get_descriptive_name())

# Call odometer
restaurant.read_restaurant_rating()

# Update Odometer reading
restaurant.update_restaurant_rating(5)
restaurant.read_restaurant_rating()

# Set an attribute
restaurant.restaurant_rating = 5
restaurant.read_restaurant_rating()
