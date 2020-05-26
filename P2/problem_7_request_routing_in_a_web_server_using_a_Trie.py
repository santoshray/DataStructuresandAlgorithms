#HTTPRouter using a Trie

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional
class RouteTrieNode:
	def __init__(self, path_handler=None):
		# Initialize the node with children as before, plus a handler
		self.children = {}
		self.path_handler = path_handler
		#print("Trie node : children:{}, path_handler:{}".format(self.children,self.path_handler))

	def insert(self, path):
		# Insert the node as before
		self.children[path] = RouteTrieNode()
		#print("Trienode Insert : children:{}, path:{}".format(self.children,path))


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler, not_found_handler="404 Page not found"):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self,path_part_list,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        trie_node = self.root
        #print("RouteTrie : path_part_list:{} , handler:{}".format(path_part_list,handler))
        for path in path_part_list:
            if path not in trie_node.children:
                trie_node.insert(path)
            trie_node = trie_node.children[path]

        #last trie node has the Handler 
        trie_node.path_handler = handler
	    #print("trie_node: path_handler :{} , children:{}".format(trie_node.path_handler,trie_node.children))

        
    def find(self,path_part_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        trie_node = self.root

        for path in path_part_list:
            if path not in trie_node.children:
                return None
            trie_node = trie_node.children[path]

        return trie_node.path_handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler="404 page not found"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(handler)
        self.routes.insert("/", handler)
        self.not_found = not_found_handler


    def add_handler(self,path,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_part_list  =  self.split_path(path)
        #print("path_part_list:{}".format(path_part_list))

        self.routes.insert(path_part_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_part_list = self.split_path(path)
        response  = self.routes.find(path_part_list)
        if ( response !=None):
        	return response
        else:
        	return self.not_found 

    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if (path =="/"):
        	path_part_list = ["/"]

        else :
            if path[-1] == "/":
                path = path[:-1]
            path_part_list = path.split('/')



        return path_part_list

if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation
    print("\n---Test case 1---")
    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' as the code handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one        

    print("\n---Test case 2---")
    # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home", "home page handler")  # add a route
    router.add_handler("/contacts/customer_service", "Customer Service handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print home page handler
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/contacts/about/")) # should print '404 page not found'
    print(router.lookup("/contacts/customer_service/")) # should print 'Customer Service handler'


    print("\n---Test case 3---")
    # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # # should print '404 page not found'
    print(router.lookup("/home/about")) # should print '404 page not found'
    print(router.lookup("/contacts/about/")) # should print '404 page not found'
    print(router.lookup("/contacts/customer_service/")) # should print '404 page not found'

    print("\n---Test case 4---")
    # create the router and add a route
    router = Router(None,None)  # remove the 'not found handler' if you did not implement this
    # some lookups with the expected output
    print(router.lookup("/")) # should print None
    print(router.lookup("/home")) # should print None

