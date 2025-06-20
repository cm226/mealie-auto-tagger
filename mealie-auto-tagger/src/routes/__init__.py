import json
from fastapi import APIRouter
from model.mealie.notifiedMessage import NotifiedMessage, ShoppingListUpdate
from model.mealieLableEmbeddings import MealieLabelEmbeddings
from services.mealieShoppingList import mealieShoppingList
from services.embedding.embeddingService import EmbeddingService


embeddingService = EmbeddingService()

def makeRouter(labelEmbeddings : MealieLabelEmbeddings):
    router = APIRouter(prefix="/webhooks")


    @router.post("/post/")
    def notified_from_meaile(update: NotifiedMessage):

        #some weird patch/diff format from apraise/mealie? TODO
        docData = update.document_data.replace('+', '')
        parsed = json.loads(docData)
        details = ShoppingListUpdate(**parsed)

        for itemID in details.shoppingListItemIds:

            listItem = mealieShoppingList.getListItem(itemID)
            
            chosenLabel = embeddingService.findClosest(listItem.display, labelEmbeddings)
            if listItem.labelId == chosenLabel.label.id:
                continue

            listItem.labelId = chosenLabel.label.id
            listItem.label = chosenLabel.label
            mealieShoppingList.updateListItem(listItem)

        return 200
    return router