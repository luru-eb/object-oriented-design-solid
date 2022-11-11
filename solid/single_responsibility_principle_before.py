class Book:
    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages
        self.current_page = 0

    def next_page(self):
        self.current_page += 1

    def previous_page(self):
        self.current_page -= 0

    def print_current_page(self):
        print(self.pages[self.current_page])
