def main_menu_f(request):
    """Define main menu links for context"""
    menu = [
        {'route': 'home', 'title': 'Home'},

    ]
    if request.user.id:
        menu.append({'route': 'cabinet', 'title': request.user.email})
    else:
        menu.append({'route': 'login', 'title': 'Login'})
        menu.append({'route': 'register', 'title': 'Register'})
        menu.append({'route': 'password-restore', 'title': 'Restore password'})
    return {"main_menu": menu}
