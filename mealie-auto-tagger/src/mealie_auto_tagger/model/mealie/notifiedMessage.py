

from pydantic import BaseModel

class ShoppingListUpdate(BaseModel):
    shoppingListId: str
    shoppingListItemIds : list[str]

class NotifiedMessage(BaseModel): 
    version: str
    title: str
    message: str
    attachments: list
    type: str
    event_type: str
    integration_id: str
    document_data: str
    event_id: str
    timestamp: str