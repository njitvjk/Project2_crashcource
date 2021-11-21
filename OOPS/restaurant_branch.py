from OOPS.restaurant import Restaurant


class RestaurantBranch(Restaurant):
    """Represents aspects of restaurant specific to a branch """

    def __init__(self, name, cuisine_type, location):
        """Initialize attributes of parent class"""
        super().__init__(name, cuisine_type, location)
        # setting a default value for attribute
        self.speciality = 'sweets & savouries'

    def restaurant_speciality(self):
        """print the speciality of this branch"""
        print(f"This restaurant is famous for {self.speciality}")

    # Overriding method from parent
    def update_restaurant_rating(self, rating):
        """modifying an attribute's value through method"""
        self.restaurant_rating = rating


restaurant_branch = RestaurantBranch('SPICES', 'Indian_cuisine', 'Newark')
print(restaurant_branch.get_descriptive_name())

# Call child class method
restaurant_branch.restaurant_speciality()

# Checking method overriding
restaurant_branch.update_restaurant_rating(3)
restaurant_branch.read_restaurant_rating()
