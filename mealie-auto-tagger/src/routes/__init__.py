import json
from fastapi import APIRouter
from model.mealie.notifiedMessage import NotifiedMessage, ShoppingListUpdate
from model.mealie.shoppingListItem import Label
from services.mealieShoppingList import mealieShoppingList

def makeRouter(labels : list[Label]):
    router = APIRouter(prefix="/webhooks")


    @router.post("/post/")
    def notified_from_meaile(update: NotifiedMessage):

        #some werid patch/diff format from apraise/mealie? TODO
        docData = update.document_data.replace('+', '')
        parsed = json.loads(docData)
        details = ShoppingListUpdate(**parsed)

        for itemID in details.shoppingListItemIds:

            chosenLabel = labels[0]
            listItem = mealieShoppingList.getListItem(itemID)
            
            if listItem.labelId == chosenLabel.id:
                continue

            listItem.labelId = chosenLabel.id
            listItem.label = chosenLabel
            mealieShoppingList.updateListItem(listItem)

        return 200
    return router