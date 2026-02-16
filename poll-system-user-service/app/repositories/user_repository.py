from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    def create_user(self, db: Session, user: UserCreate):
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            age=user.age,
            address=user.address,
            joining_date=user.joining_date
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    def register_user(self, db: Session, user_id: int):
        user = self.get_user_by_id(db, user_id)
        if not user:
            return None

        user.is_registered = True
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = self.get_user_by_id(db, user_id)
        if not user:
            return None
        db.delete(user)
        db.commit()
        return user

    def get_all_users(self, db: Session):
        return db.query(User).all()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def update_user(self, db: Session, user_id: int, user_data: dict):
        user = self.get_user_by_id(db, user_id)
        if not user:
            return None

        for key, value in user_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        return user
