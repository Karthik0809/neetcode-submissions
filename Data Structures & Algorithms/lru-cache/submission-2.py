from collections import OrderedDict

class LRUCache:
    """
    LRU = Least Recently Used Cache
    
    Problem: Store key-value pairs with limited capacity
    When full, remove the LEAST RECENTLY USED item
    
    Example:
    capacity = 2
    put(1, 1)     → cache: {1: 1}
    put(2, 2)     → cache: {1: 1, 2: 2}
    get(1)        → returns 1, move 1 to end (most recent)
    put(3, 3)     → cache full! Remove 2 (least recent)
                 → cache: {1: 1, 3: 3}
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache
        
        OrderedDict: Remembers insertion order (Python 3.7+)
        In OrderedDict, items at the START = least recently used
                        items at the END = most recently used
        """
        # Use OrderedDict to maintain order of access
        # Keys are stored in order: [oldest ... newest]
        self.cache = OrderedDict()
        
        # Maximum number of items we can store
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Get value for key
        If found: mark it as recently used (move to end)
        If not found: return -1
        """
        # ========== CASE 1: KEY NOT IN CACHE ==========
        if key not in self.cache:
            return -1  # Not found, return -1
        
        # ========== CASE 2: KEY EXISTS ==========
        # Move this key to END (mark as most recently used)
        # move_to_end(key) moves key to the end of OrderedDict
        # This shows we just accessed it
        self.cache.move_to_end(key)
        
        # Return the value associated with key
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        """
        Put (insert/update) a key-value pair
        If key exists: update value and mark as recently used
        If key is new: add it and evict least recently used if needed
        """
        # ========== CASE 1: KEY ALREADY EXISTS ==========
        if key in self.cache:
            # Update the value
            self.cache[key] = value
            
            # Move to end (mark as most recently used)
            # Even though we're updating, we accessed it, so it's recent
            self.cache.move_to_end(key)
        
        # ========== CASE 2: NEW KEY ==========
        else:
            # Add new key-value pair to cache
            self.cache[key] = value
        
        # ========== CAPACITY CHECK ==========
        # If cache exceeds capacity, remove least recently used item
        if len(self.cache) > self.capacity:
            # popitem(last=False) removes the FIRST item (least recent)
            # last=False → pop from beginning (oldest)
            # last=True → pop from end (newest, not what we want)
            self.cache.popitem(last=False)
            
            # The removed item is the one that was accessed longest ago
        
        
