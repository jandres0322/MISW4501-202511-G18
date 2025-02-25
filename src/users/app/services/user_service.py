from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_all():
        return UserRepository.get_all()

    @staticmethod
    def get_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def get_by_email(email):
        return UserRepository.get_by_email(email)

    @staticmethod
    def create(user_data):
        return UserRepository.create(user_data)