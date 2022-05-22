"""Deletes a user from the database."""
def main():
    from bgserver.database.models import User
    from mongoengine import connect, NotUniqueError
    import os
    import sys

    username = sys.argv[1]

    connect('bullseyegolf', host='MongoDB')

    user = User.objects(username=username).first()
    user.delete()

    print(f"User {user.username} was successfully deleted.")


if __name__ == "__main__":
    main()

