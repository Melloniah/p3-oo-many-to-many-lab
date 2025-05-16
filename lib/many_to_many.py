from datetime import datetime

class Author:
    all = []  # Class variable to track all Author instances

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return all contracts where this author is the author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return all books associated with this author's contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create and return a new Contract
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum royalties from all contracts
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []  # Class variable to track all Book instances

    def __init__(self, title):
        self.title = title
        Book.all.append(self)


class Contract:
    all = []  # Class variable to track all Contract instances

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        try:
            datetime.strptime(value, "%Y-%m-%d")  # Validate format
        except ValueError:
            raise Exception("date must be in YYYY-MM-DD format")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number")
        if value < 0:
            raise Exception("royalties must be non-negative")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts matching a specific date
        return [contract for contract in cls.all if contract.date == date]
