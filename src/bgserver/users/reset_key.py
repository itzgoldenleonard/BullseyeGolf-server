"""Creates a new user in the database."""
def main():
    from bgserver.database.models import User
    from mongoengine import connect, NotUniqueError
    import os
    import sys

    username = sys.argv[1]

    key = os.urandom(16).hex()

    connect('bullseyegolf', host='MongoDB')

    user = User.objects(username=username).first()
    user.update(set__key=key)

    print(f"New key for user {user.username}: {key}")


if __name__ == "__main__":
    main()

