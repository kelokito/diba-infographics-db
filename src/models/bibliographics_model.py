from dataclasses import dataclass

@dataclass
class BibliographicRecord:
    id: int
    call: str
    cdu: str
    year_edition: int
    mat_type: str
    lang: str
