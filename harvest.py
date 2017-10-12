############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.name = name
        self.reporting_code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.reporting_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""


    # Fill in the rest
    muskmelon = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    muskmelon.add_pairing(["mint"])
    casaba = MelonType("Casaba", "cas", 2003, "orange", False, False)
    casaba.add_pairing(["strawberries", "mint"])
    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    crenshaw.add_pairing(["proscuitto"])
    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013,
                                    "yellow", False, True)
    yellow_watermelon.add_pairing(["ice cream"])

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    return all_melon_types

def melon_pairs_with(melon_list):


    for melon in melon_list:
        print "{} pairs with" .format(melon.name)
        for food in melon.pairings:
            print "-{}".format(food)
       
 
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for item in melon_types:
        melon_dict[item.reporting_code] = item.name
    print melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


all_melon_types = make_melon_types()
melon_pairs_with(all_melon_types)
make_melon_type_lookup(all_melon_types)