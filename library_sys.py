class Book:
    def __init__(self, title: str, author: str, year_published: int):
        self.title = title
        self.author = author
        self.year_published = year_published

    def display_detail_book(self) -> str:
        return f"Título: {self.title}\nAutor: {self.author}\nAno de publicação {self.year_published}"

class Client:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def display_inf(self) -> str:
        return f"Nome: {self.name}\nemail: {self.email}"

class Request:
    def __init__(self, client):
        self.client = client
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_detail_request(self):
        detail = f"Detalhes do pedido:\n{self.client.display_inf()}\nLivros pedidos:"
        for b in self.books:
            detail += f"\n{b.display_detail_book()}"
        return detail


if __name__ == "__main__":

    livro1 = Book("Pai Rico", "Robert Kiosaky", 2010)
    client1 = Client("Felipe", "feh.neo@hotmail.com")
    pedido1 = Request(client1)
    pedido1.add_book(livro1)

    print(pedido1.display_detail_request())
