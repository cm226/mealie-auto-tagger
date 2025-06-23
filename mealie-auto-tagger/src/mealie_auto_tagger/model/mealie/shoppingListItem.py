from typing import Optional
from pydantic import BaseModel

class MealieLabel(BaseModel):
    name: str
    color: str
    groupId: str
    id: str

class MealieShoppingListItemFood(BaseModel):
    id: str
    name: str
    pluralName: str
    description: str
    extras: dict
    labelId: str
    aliases: list
    householdsWithIngredientFood: list
    label: MealieLabel
    
    createdAt: str
    updatedAt: str

class MealieShoppingListItemUnit(BaseModel):
    id: str
    name: str
    pluralName: str 
    description: str
    fraction: bool
    abbreviation: str
    pluralAbbreviation: str
    useAbbreviation: bool
    aliases: list
    createdAt: str
    updatedAt: str

class MealieShoppingListItem(BaseModel):
  quantity: int
  unit: Optional[MealieShoppingListItemUnit]
  food: Optional[MealieShoppingListItemFood]
  note: str
  isFood: bool
  disableAmount: bool
  display: str
  shoppingListId: str
  checked: bool
  position: int
  foodId: Optional[str]
  labelId: Optional[str]
  unitId: Optional[str]
  extras: dict
  id: str
  groupId: str
  householdId: str
  label: Optional[MealieLabel]
  recipeReferences: list
  createdAt: str
  updatedAt: str
