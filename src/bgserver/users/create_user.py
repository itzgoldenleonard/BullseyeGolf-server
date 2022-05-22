"""Creates a new user in the database."""
def main():
    from bgserver.database.models import User
    from mongoengine import connect, NotUniqueError
    import os
    import sys

    username = sys.argv[1]

    key = os.urandom(16).hex()

    connect('bullseyegolf', host='MongoDB')

    try:
        user = User(username=username, key=key).save()
    except NotUniqueError:
        print('User already exists.')
        return

    print("New user created:")
    print(f"Username: {user.username}")
    print(f"Key: {user.key}")


if __name__ == "__main__":
    main()

