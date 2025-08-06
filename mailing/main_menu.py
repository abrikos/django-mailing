def main_menu_f(request):
    """Define main menu links for context"""
    menu = [
        {"route": "home", "title": "Home"},
    ]
    if request.user.id:
        menu.append({"route": "mailing", "title": request.user.email})
    else:
        menu.append({"route": "login", "title": "Login"})
        menu.append({"route": "register", "title": "Register"})
    return {"main_menu": menu}
