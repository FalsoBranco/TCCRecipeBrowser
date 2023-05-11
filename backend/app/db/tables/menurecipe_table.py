from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.account_table import Account
from app.db.tables.base_class import Base, IdMixin
from app.db.tables.recipe_table import Recipe


class MenuRecipe(Base, IdMixin):
    __tablename__ = "menu_recipes"

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"))
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))
