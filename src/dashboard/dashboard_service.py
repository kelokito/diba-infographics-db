from src.bibliographics.bibliographics_repository import BibliographicsRepository
from src.users.users_repository import UsersRepository
from src.general.general_repository import GeneralRepository

class DashboardService:

    def load_dashboard_data(self):
        return {
            "bibliographics": BibliographicsRepository.get_all(),
            "users": UsersRepository.get_all(),
            "general": GeneralRepository.get_all()
        }
