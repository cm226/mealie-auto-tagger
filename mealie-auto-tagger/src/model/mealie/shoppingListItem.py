from typing import Optional
from pydantic import BaseModel

class Label(BaseModel):
    name: str
    color: str
    groupId: str
    id: str

class ShoppingListItemFood(BaseModel):
    id: str
    name: str
    pluralName: str
    description: str
    extras: dict
    labelId: str
    aliases: list
    householdsWithIngredientFood: list
    label: Label
    
    createdAt: str
    updatedAt: str

class ShoppingListItemUnit(BaseModel):
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

class ShoppingListItem(BaseModel):
  quantity: int
  unit: Optional[ShoppingListItemUnit]
  food: Optional[ShoppingListItemFood]
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
  label: Optional[Label]
  recipeReferences: list
  createdAt: str
  updatedAt: str
