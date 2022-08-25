"""Validator Module"""
import re
from bson.objectid import ObjectId




def validate(data, regex):
    """Custom Validator"""
    return True if re.match(regex, data) else False




def validate_email(email: str):
    """Email Validator"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return validate(email, regex)




def validate_book(**args):
    """Book Validator"""
    if not args.get('title') or not args.get('image_url') \
        or not args.get('category') or not args.get('user_id'):
        return {
            'title': 'Title is required',
            'image_url': 'Image URL is required',
            'category': 'Category is required',
            'user_id': 'User ID is required'
        }
    if args.get('category') not in ['romance', 'peotry', 'politics' 'picture book', 'science', 'fantasy', 'horror', 'thriller']:
        return {
            'status': 'error',
            'message': 'Invalid category'
        }
    try:
        ObjectId(args.get('user_id'))
    except:
        return {
            'user_id': 'User ID must be valid'
        }
    if not isinstance(args.get('title'), str) or not isinstance(args.get('description'), str) \
        or not isinstance(args.get('image_url'), str):
        return {
            'title': 'Title must be a string',
            'description': 'Description must be a string',
            'image_url': 'Image URL must be a string'
        }
    return True

def validate_user(**args):
    """User Validator"""
    if not args.get('email') or not args.get('password') or not args.get('first_name') or not args.get("last_name"):
        return {
            'email': 'Email is required',
            'password': 'Password is required',
            'first_name': 'First name is required',
            'last_name': 'Last name is required'
        }

    if not isinstance(args.get('first_name'), str) or not isinstance(args.get('email'), str) \
        or not isinstance(args.get('password'), str) or not isinstance(args.get("last_name"), str):

        return {
            'email': 'Email must be a string',
            'password': 'Password must be a string',
            'first_name': 'First name must be a string',
            'last_name': 'Last name must be a string'
        }

    if not validate_email(args.get('email')):
        return {
            'email': 'Email is invalid'
        }


    if not 2 <= len(args['first_name']) <= 30:
        return {
            'first_name': 'First name must be between 2 and 30 words'
        }

    if not 2 <= len(args['last_name']) <= 30:
        return {
            'last_name': 'Last name must be between 2 and 30 words'
        }

    return True





def validate_email_and_password(email, password):
    """Checks email and password"""

    if not (email and password):
        return {
            'email': 'Email is required',
            'password': 'Password is required'
        }

    if not validate_email(email):
        return {
            'email': 'Email is invalid'
        }

    return True
