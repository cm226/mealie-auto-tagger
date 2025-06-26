from typing import Optional
from pydantic import BaseModel

class MealieLabel(BaseModel):
    name: str
    color: str
    groupId: str
    id: str

class MealieShoppingListItemFood(BaseModel):
    id: str
    name: Optional[str]
    pluralName: Optional[str]
    description: Optional[str]
    extras: Optional[dict]
    labelId: Optional[str]
    aliases: list
    householdsWithIngredientFood: list
    label: Optional[MealieLabel]
    
    createdAt: str
    updatedAt: str

class MealieShoppingListItemUnit(BaseModel):
    id: str
    name: Optional[str]
    pluralName: Optional[str] 
    description: Optional[str]
    fraction: Optional[bool]
    abbreviation: Optional[str]
    pluralAbbreviation: Optional[str]
    useAbbreviation: Optional[bool]
    aliases: list
    createdAt: str
    updatedAt: str

class MealieShoppingListItem(BaseModel):
  quantity: float
  unit: Optional[MealieShoppingListItemUnit]
  food: Optional[MealieShoppingListItemFood]
  note: Optional[str]
  isFood: Optional[bool]
  disableAmount: bool
  display: str
  shoppingListId: str
  checked: bool
  position: int
  foodId: Optional[str]
  labelId: Optional[str]
  unitId: Optional[str]
  extras: Optional[dict]
  id: str
  groupId: str
  householdId: str
  label: Optional[MealieLabel]
  recipeReferences: Optional[list]
  createdAt: str
  updatedAt: str
