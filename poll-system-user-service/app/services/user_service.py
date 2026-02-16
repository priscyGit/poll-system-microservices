from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user: UserCreate):
        existing_user = self.user_repository.get_user_by_email(db, user.email)
        if existing_user:
            raise ValueError("Email already exists")

        return self.user_repository.create_user(db, user)

    def get_user(self, db: Session, user_id: int):
        return self.user_repository.get_user_by_id(db, user_id)

    def register_user(self, db: Session, user_id: int):
        return self.user_repository.register_user(db, user_id)

    def delete_user(self, db: Session, user_id: int):
        return self.user_repository.delete_user(db, user_id)

    def get_all_users(self, db: Session):
        return self.user_repository.get_all_users(db)

    def update_user(self, db: Session, user_id: int, user: UserUpdate):
        existing_user = self.user_repository.get_user_by_id(db, user_id)
        if not existing_user:
            return None

        if user.email:
            email_owner = self.user_repository.get_user_by_email(db, user.email)
            if email_owner and email_owner.id != user_id:
                raise ValueError("Email already exists")

        update_data = user.dict(exclude_unset=True)
        return self.user_repository.update_user(db, user_id, update_data)