

class StoreService:
    """
    Interface for store service.
    """
    
    

class MenuService:
    """
        1) new_user:  add_store, join_store
        2) owner: product(l,e), order(r), 
        3) sales: order(l,e), customer(l,e)
    """
    
    @staticmethod
    def visitor_menu():
        html = """
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <p class="navbar-text ">Current user: site visitor</p>
                    </li>
                </ul>
            </div>
        """
        return html
    
    @staticmethod
    def owner_menu(user, store):
        html = """
        
        <div id="navbar" class="navbar-collapse collapse">

            <ul class="nav navbar-nav">
                <li><a href="/sales/product/new/{1}">Add Product</a></li>
                <li><a href="/sales/products/{1}">Products</a></li>
                <li><a href="/sales/orders/{1}">customers</a></li>
                <li><a href="/sales/orders/{1}">Orders</a></li>
            </ul>
            
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <p class="navbar-text ">Signed in as owner {0}</p>
                </li>
                <li>
                    <p class="navbar-text ">In Store: {2}</p>
                </li>
                <li>
                    <button onclick="window.location.href='/account/logout'" type="button" class="btn btn-default navbar-btn">Logout</button>
                </li>
            </ul>
        </div>
        
        """.format(user.username, store.id, store.name)
        return html
    
    @staticmethod
    def sales_menu(user, store):
        html = """
        
        <div id='navbar' class='navbar-collapse collapse'>

            <ul class='nav navbar-nav'>
                <li><a href='/sales/customer/new/'>Add Customer</a></li>
                <li><a href='/sales/customers/'>Customers</a></li>
                <li><a href='/sales/order/add/'>Create order</a></li>
                <li><a href='/sales/orders/'>Orders</a></li>
            </ul>
            
            <ul class='nav navbar-nav navbar-right'>
                <li>
                    <p class='navbar-text '>Signed in as agent {0}</p>
                </li>
                <li>
                    <p class='navbar-text '>In Store: {2}</p>
                </li>
                <li>
                    <button onclick='window.location.href='/account/logout'' type='button' class='btn btn-default navbar-btn'>Logout</button>
                </li>
            </ul>
        </div>
        
        """.format(user.username, store.id, store.name)
        
        return html
    
    @staticmethod
    def unapproved_sales_menu(user, store):
        html = """
        
        <div id="navbar" class="navbar-collapse collapse">

            <ul class="nav navbar-nav">
                <li><a href="/store/new">Create Store</a></li>
                <li><a href="/store/join">Join Store</a></li>
            </ul>
            
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <p class="navbar-text ">Signed in as unapproved agent {0}</p>
                </li>
                <li>
                    <button onclick="window.location.href='/account/logout'" type="button" class="btn btn-default navbar-btn">Logout</button>
                </li>
            </ul>
        </div>
        
        """.format(user.username)
        return html
        
    @staticmethod
    def new_user_menu(user):
        html = """
        
        <div id="navbar" class="navbar-collapse collapse">

            <ul class="nav navbar-nav">
                <li><a href="/store/new">Create Store</a></li>
                <li><a href="/store/join">Join Store</a></li>
            </ul>
            
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <p class="navbar-text ">Signed in as new user {0}</p>
                </li>
                <li>
                    <button onclick="window.location.href='/account/logout'" type="button" class="btn btn-default navbar-btn">Logout</button>
                </li>
            </ul>
        </div>
        
        """.format(user.username)
        return html
    
    