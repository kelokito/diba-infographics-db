from dataclasses import dataclass

@dataclass
class BibliographicRecord:
    id: int
    title: str
    author: str
    year: int
