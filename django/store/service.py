from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

class MenuService:
    
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
    def owner_menu():
        html = ""
        return html
    
    @staticmethod
    def sales_menu():
        html = ""
        return html
    
    @staticmethod
    def new_user_menu(user):
        html = """
        
        <div id="navbar" class="navbar-collapse collapse">

            <ul class="nav navbar-nav">
                <li><a href="/store/new">Create Store</a></li>
            </ul>
            
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <p class="navbar-text ">Signed in as {0}</p>
                </li>
                <li>
                    <button onclick="window.location.href='/account/logout'" type="button" class="btn btn-default navbar-btn">Logout</button>
                </li>
            </ul>
        </div>
        
        """.format(user.username)
        return html