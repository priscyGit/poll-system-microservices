from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import httpx

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate

POLL_SERVICE_URL = "http://poll-service:8000"

class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user: UserCreate):
        existing_user = self.user_repository.get_user_by_email(db, user.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        return self.user_repository.create_user(db, user)

    def get_user(self, db: Session, user_id: int):
        user = self.user_repository.get_user_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    def register_user(self, db: Session, user_id: int):
        user = self.user_repository.register_user(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    POLL_SERVICE_URL = "http://poll-service:8002"  

    async def delete_user(self, db: Session, user_id: int):
        user = self.user_repository.delete_user(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # 🔥 Notify Poll Service to delete answers
        async with httpx.AsyncClient() as client:
            await client.delete(
                f"{POLL_SERVICE_URL}/answers/user/{user_id}"
            )

        return user

    def get_all_users(self, db: Session):
        return self.user_repository.get_all_users(db)

    def update_user(self, db: Session, user_id: int, user: UserUpdate):
        existing_user = self.user_repository.get_user_by_id(db, user_id)

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user.email:
            email_owner = self.user_repository.get_user_by_email(db, user.email)
            if email_owner and email_owner.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )

        update_data = user.dict(exclude_unset=True)
        return self.user_repository.update_user(db, user_id, update_data)