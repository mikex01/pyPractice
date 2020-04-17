# LIBRARY
from IPython import get_ipython
    
class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
# Heights Student
class HashMap:
    
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0
    
    def put(self, key, value):
        
        bucket_index = self.get_bucket_index(key) #hash(key) = indice
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]
        
        # hashExist?
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        # crear a new entry 
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
    
    def get(self, key):
        pass
    
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets
            hash_code_compres = hash_code % num_buckets
        return hash_code_compres
    
    def size(self):
        return self.num_entries


def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code
    

# funcion que imprime
def print_01():
    """
    # AUTO TEST

    # TODO: Print a list of all cities in the USA in 
    alphabetic order.
    
    # TODO: Print all cities in Asia, in alphabetic order, 
    next to the name of the country
    """
    locations = {'North America': {'USA': ['Mountain View']}}
    locations['North America']['USA'].append('Atlanta')
    locations['Asia'] = {'India': ['Bangalore']}
    locations['Asia']['China'] = ['Shanghai']
    locations['Africa'] = {'Egypt': ['Cairo']}
    
    """PROGRAM"""
    
    usa_sorted = sorted(locations['North America']['USA'])
    asia_cities = []
    
    print (1)
    for city in usa_sorted:
        print (city)
    
    print (2)
    for countries, cities in locations['Asia'].items():
        city_country = cities[0] + " - " + countries 
        asia_cities.append(city_country)
    asia_sorted = sorted(asia_cities)
    for city in asia_sorted:
        print (city)
        
        
if __name__ == '__main__':
    get_ipython().magic('clear')
    hash_map = HashMap()

    hash_map.put("one", 1)
    hash_map.put("two", 2)
    hash_map.put("three", 3)
    hash_map.put("neo", 11)
    
    print("size: {}".format(hash_map.size()))
    
    
    print("one: {}".format(hash_map.get("one")))
    print("neo: {}".format(hash_map.get("neo")))
    print("three: {}".format(hash_map.get("three")))
    print("size: {}".format(hash_map.size()))