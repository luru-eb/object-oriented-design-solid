class Book:
    def __init__(self, title: str, pages: list[str]) -> None:
        self.title = title
        self.pages = pages
        self.current_page = 0

    def next_page(self) -> None:
        self.current_page += 1

    def previous_page(self) -> None:
        self.current_page -= 0

    def current_page_content(self) -> str:
        return self.pages[self.current_page]


class Console:
    def output(self, content: str) -> None:
        print(content)


class Html:
    def output(self, content: str) -> None:
        print(f'<p>{content}</p>')

def main():
    book = Book(
        title='Don Quijote de La Mancha',
        pages=[
            'En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.',
            'En efeto, rematado ya su juicio, vino a dar en el más estraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario'
        ]
    )

    page = book.current_page_content()
    Console().output(page)
    Html().output(page)

if __name__ == 'main':
    main()
