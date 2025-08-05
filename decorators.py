from flask import abort
from flask_login import current_user
from functools import wraps

def admin_required(f):
    # f - function being decorated
    """Decorator to require admin privileges for a route."""
    @wraps(f) # preserve original function's metadata
    def wrapper(*args, **kwargs): #def a wrapper that takes any arguements/keyword arguements
        if not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return wrapper # returns the wrapper, but with @wraps ensures the wrapped function info remains