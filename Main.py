import sys
from Recommended_Books import Library


def main():
    create_menu()


def create_menu():
    on_menu = True
    lib = Library("https://www.casadellibro.com/libros-recomendados")
    while on_menu:
        print("Select Option: 1 - for loading 2 - for saving 3 -for display 4 - for sending an email 5- for exit")

        selection = input()
        try:
            if selection == "1":
                lib.load()
            elif selection == "2":
                lib.save_Books()
            elif selection == "3":
                lib.display()
            elif selection == "4":
                lib.send_email()
            elif selection == "5":
                on_menu = False
            else:
                raise myException("Not accepted Value")
        except myException as e:

            print(e, file=sys.stderr)


class myException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "This is a special Exception"

    def __str__(self):

        return 'MyCustomError, {0} '.format(self.message)


main()
