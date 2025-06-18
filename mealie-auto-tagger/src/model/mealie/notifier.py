from typing import Optional
from pydantic import BaseModel


class NoritierOptions(BaseModel):
    testMessage: bool
    webhookTask : bool
    recipeCreated : bool
    recipeUpdated : bool
    recipeDeleted : bool
    userSignup : bool
    dataMigrations : bool
    dataExport : bool
    dataImport : bool
    mealplanEntryCreated : bool
    shoppingListCreated : bool
    shoppingListUpdated : bool
    shoppingListDeleted : bool
    cookbookCreated : bool
    cookbookUpdated : bool
    cookbookDeleted : bool
    tagCreated : bool
    tagUpdated : bool
    tagDeleted : bool
    categoryCreated : bool
    categoryUpdated : bool
    categoryDeleted : bool
    id : str


class Notifier(BaseModel):
  id: str
  name: str
  appriseUrl: str = ""
  enabled: bool
  groupId: str
  householdId: str
  options: NoritierOptions

