from typing import Optional
from pydantic import BaseModel

class MealieLabel(BaseModel):
    name: str
    color: str
    groupId: str
    id: str

class MealieShoppingListItemFood(BaseModel):
    id: str
    name: Optional[str] = None
    pluralName: Optional[str] = None
    description: Optional[str] = None
    extras: Optional[dict] = None
    labelId: Optional[str] = None
    aliases: list
    householdsWithIngredientFood: list
    label: Optional[MealieLabel] = None
    
    createdAt: str
    updatedAt: str

class MealieShoppingListItemUnit(BaseModel):
    id: str
    name: Optional[str] = None
    pluralName: Optional[str]  = None
    description: Optional[str] = None
    fraction: Optional[bool] = None
    abbreviation: Optional[str] = None
    pluralAbbreviation: Optional[str] = None
    useAbbreviation: Optional[bool] = None
    aliases: list
    createdAt: str
    updatedAt: str

class MealieShoppingListItem(BaseModel):
  quantity: float
  unit: Optional[MealieShoppingListItemUnit] = None
  food: Optional[MealieShoppingListItemFood] = None
  note: Optional[str]
  isFood: Optional[bool] = None
  disableAmount: Optional[bool] = None
  display: str
  shoppingListId: str
  checked: bool
  position: int
  foodId: Optional[str] = None
  labelId: Optional[str] = None
  unitId: Optional[str] = None
  extras: Optional[dict] = None
  id: str
  groupId: str
  householdId: str
  label: Optional[MealieLabel] = None
  recipeReferences: Optional[list] = None
  createdAt: str
  updatedAt: str
