# LeetCode-Soluion-in-C-Java

    
146. LRU Cache
    

9 Feb 2023

    

Medium

C++:

// Time Complexity : O(1) for all the operations and space complexity is O(n) where n is the capacity of the cache

class LRUCache {
    int capacity;  // variable to store the capacity of the cache
    list<pair<int, int>> cache;  // list to store the key, value and frequency of the cache
    unordered_map<int, list<pair<int, int>>::iterator> pos;  // map to store the key and the position of the key in the list of keys of the cache
public:
    LRUCache(int capacity) {
        this->capacity = capacity;  // initialize the capacity of the cache
    }
    
    int get(int key) {
        if(pos.find(key) == pos.end()){  // if the key is not present in the cache
            return -1;  // return -1
        }
        int value = pos[key]->second;  // get the value of the key
        cache.erase(pos[key]);  // erase the key from the list of keys of the cache
        cache.push_front({key, value});  // push the key to the list of keys of the cache
        pos[key] = cache.begin();  // update the position of the key in the list of keys of the cache
        return value;  // return the value of the key
    }
    
    void put(int key, int value) {
        if(capacity == 0){  // if the capacity of the cache is 0
            return;  // return
        }
        if(pos.find(key) != pos.end()){  // if the key is present in the cache
            cache.erase(pos[key]);  // erase the key from the list of keys of the cache
        }
        else if(cache.size() == capacity){  // if the size of the cache is equal to the capacity of the cache
            int lastKey = cache.back().first;  // get the last key of the list of keys of the cache
            cache.pop_back();  // pop the last key from the list of keys of the cache
            pos.erase(lastKey);  // erase the key from the map
        }
        cache.push_front({key, value});  // push the key to the list of keys of the cache
        pos[key] = cache.begin();  // update the position of the key in the list of keys of the cache
    }
};


Java:

4 Approaches

1st Method

// Time Complexity : O(1) for all the operations and space complexity is O(n) where n is the capacity of the cache

class LRUCache {
    int capacity;  // variable to store the capacity of the cache
    HashMap<Integer, Node> map;  // map to store the key and the node of the key in the double linked list of keys of the cache
    Node head;  // head of the double lid list of keys of the cache
    Node tail;  // tail of the double linked list of keys of the cache
    public LRUCache(int capacity) {
        this.capacity = capacity;  // initialize the capacity of the cache
        map = new HashMap<>();  // initialize the map
        head = new Node();  // initialize the head of the double linked list of keys of the cache
        tail = new Node();  // initialize the tail of the double linked list of keys of the cache
        head.next = tail;  // connect the head and the tail of the double linked list of keys of the cache
        tail.prev = head;  // connect the head and the tail of the double linked list of keys of the cache
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){  // if the key is not present in the cache
            return -1;  // return -1
        }
        Node node = map.get(key);  // get the node of the key in the double linked list of keys of the cache
        remove(node);  // remove the node from the double linked list of keys of the cache
        add(node);  // add the node to the double linked list of keys of the cache
        return node.value;  // return the value of the key
    }
    
    public void put(int key, int value) {
        if(capacity == 0){  // if the capacity of the cache is 0
            return;  // return
        }
        if(map.containsKey(key)){  // if the key is present in the cache
            remove(map.get(key));  // remove the node of the key from the double linked list of keys of the cache
        }
        else if(map.size() == capacity){  // if the size of the cache is equal to the capacity of the cache
            map.remove(tail.prev.key);  // remove the last key from the map
            remove(tail.prev);  // remove the last node from the double linked list of keys of the cache
        }
        Node node = new Node(key, value);  // create a new node for the key
        map.put(key, node);  // add the key and the node of the key to the map
        add(node);  // add the node to the double linked list of keys of the cache
    }

    // function to remove the node from the double linked list of keys of the cache
    public void remove(Node node){
        node.prev.next = node.next;  // connect the previous node of the node to the next node of the node
        node.next.prev = node.prev;  // connect the next node of the node to the previous node of the node
    }

    // function to add the node to the double linked list of keys of the cache
    public void add(Node node){
        node.next = head.next;  // connect the next node of the node to the next node of the head
        node.prev = head;  // connect the previous node of the node to the head
        head.next.prev = node;  // connect the previous node of the next node of the head to the node
        head.next = node;  // connect the next node of the head to the node
    }

    // class to represent the node of the double linked list of keys of the cache
    class Node{
        int key;  // variable to store the key
        int value;  // variable to store the value of the key
        Node prev;  // variable to store the previous node of the node
        Node next;  // variable to store the next node of the node
        public Node(int key, int value){
            this.key = key;  // initialize the key
            this.value = value;  // initialize the value of the key
        }
        public Node(){
        }
    }
}


2nd Method

// Time Complexity : O(1) for all the operations and space complexity is O(n) where n is the capacity of the cache


class LRUCache {
    int capacity;  // variable to store the capacity of the cache
    HashMap<Integer, Node> map;  // map to store the key and the node of the key in the double linked list of keys of the cache
    Node head;  // head of the double linked list of keys of the cache
    Node tail;  // tail of the double linked list of keys of the cache
    public LRUCache(int capacity) {
        this.capacity = capacity;  // initialize the capacity of the cache
        map = new HashMap<>();  // initialize the map
        head = new Node();  // initialize the head of the double linked list of keys of the cache
        tail = new Node();  // initialize the tail of the double linked list of keys of the cache
        head.next = tail;  // connect the head and the tail of the double linked list of keys of the cache
        tail.prev = head;  // connect the head and the tail of the double linked list of keys of the cache
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){  // if the key is not present in the cache
            return -1;  // return -1
        }
        Node node = map.get(key);  // get the node of the key in the double linked list of keys of the cache
        remove(node);  // remove the node from the double linked list of keys of the cache
        add(node);  // add the node to the double linked list of keys of the cache
        return node.value;  // return the value of the key
    }
    
    public void put(int key, int value) {
        if(capacity == 0){  // if the capacity of the cache is 0
            return;  // return
        }
        if(map.containsKey(key)){  // if the key is present in the cache
            Node node = map.get(key);  // get the node of the key in the double linked list of keys of the cache
            remove(node);  // remove the node from the double linked list of keys of the cache
            node.value = value;  // update the value of the key
            add(node);  // add the node to the double linked list of keys of the cache
        }
        else if(map.size() == capacity){  // if
            Node node = tail.prev;  // get the last node of the double linked list of keys of the cache
            remove(node);  // remove the node from the double linked list of keys of the cache
            map.remove(node.key);  // remove the key from the map
            node.key = key;  // update the key
            node.value = value;  // update the value of the key
            add(node);  // add the node to the double linked list of keys of the cache
            map.put(key, node);  // add the key to the map
        }
        else{
            Node node = new Node(key, value);  // create a new node
            add(node);  // add the node to the double linked list of keys of the cache
            map.put(key, node);  // add the key to the map
        }
    }

    public void remove(Node node){  // function to remove the node from the double linked list of keys of the cache
        node.prev.next = node.next;  // remove the node from the double linked list of keys of the cache
        node.next.prev = node.prev;  // remove the node from the double linked list of keys of the cache
    }

    public void add(Node node){  // function to add the node to the double linked list of keys of the cache
        node.next = head.next;  // add the node to the double linked list of keys of the cache
        node.prev = head;  // add the node to the double linked list of keys of the cache
        head.next.prev = node;  // add the node to the double linked list of keys of the cache
        head.next = node;  // add the node to the double linked list of keys of the cache
    }

    class Node{  // class to represent the node of the double linked list of keys of the cache
        int key;  // variable to store the key
        int value;  // variable to store the value of the key
        Node prev;  // variable to store the previous node of the current node
        Node next;  // variable to store the next node of the current node
        public Node(int key, int value){  // constructor to initialize the key and the value of the key
            this.key = key;  // initialize the key
            this.value = value;  // initialize the value of the key
        }
        public Node(){  // constructor to initialize the key and the value of the key
        }
    }
}


3rd Method

class LRUCache extends LinkedHashMap<Integer, Integer>{       
    int capacity;
    public LRUCache(int capacity) {
        super(capacity, 1.0f, true);
        this.capacity = capacity;
    }
    
    public int get(int key) {
        return super.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        super.put(key, value);
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer,Integer> eldest){
        return this.size() > this.capacity;

    }
}


4th Method

// Time Complexity : O(1) for all the operations and space complexity is O(n) where n is the capacity of the cache

class LRUCache {
    class Node{
        int key;
        int value;
        Node prev;
        Node next;
        public Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }
    private void addToHead(Node node){
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
    private void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    private Node popTail(){
        Node res = tail.prev;
        removeNode(res);
        return res;
    }
    private HashMap<Integer, Node> map;
    private int size;
    private int capacity;
    private Node head, tail;
    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        map = new HashMap<>();
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        Node node = map.get(key);
        if(node == null) return -1;
        removeNode(node);
        addToHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        Node node = map.get(key);
        if(node == null){
            Node newNode = new Node(key, value);
            map.put(key, newNode);
            addToHead(newNode);
            ++size;
            if(size > capacity){
                Node tail = popTail();
                map.remove(tail.key);
                --size;
            }
        }else{
            node.value = value;
            removeNode(node);
            addToHead(node);
        }
    }
}

