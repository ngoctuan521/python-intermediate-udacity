"""Declare QuoteModel class."""


class QuoteModel():
    """QuoteModel class."""

    def __init__(self, body: str, author: str):
        """Init instance."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Show info of instance."""
        return f"{self.body} - {self.author}"
