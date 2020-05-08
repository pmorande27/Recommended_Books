from Recommended_Books import Library


def main():
    lib = Library("https://www.casadellibro.com/libros-recomendados")
    lib.load()
    lib.display()
    lib.save_Books()


main()
