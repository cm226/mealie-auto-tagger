import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.mealie.notifiedMessage import NotifiedMessage, ShoppingListUpdate
from model.mealieLableEmbeddings import MealieLabelEmbedding, MealieLabelEmbeddings
from services.mealieShoppingList import mealieShoppingList
from services.embedding.embeddingService import embeddingService
from model.mealie.shoppingListItem import MealieShoppingListItem

from db.repos.all_repositories import get_repositories
from db.init import fast_API_depends_generate_session

def getLabelAssignment(session: Session, listItem : MealieShoppingListItem, labelEmbeddings : MealieLabelEmbeddings) -> MealieLabelEmbedding:
    userSelectedListItemLabel = get_repositories(session).listItemRepo.getListItemFor(listItem.display)
    if userSelectedListItemLabel != None:
        return labelEmbeddings.getLabelByID(userSelectedListItemLabel.label)
        
    return embeddingService.findClosest(listItem.display, labelEmbeddings)
    

def makeRouter(labelEmbeddings : MealieLabelEmbeddings):
    router = APIRouter(prefix="/webhooks")

    @router.post("/post/")
    def notified_from_meaile(update: NotifiedMessage, session = Depends(fast_API_depends_generate_session)):
        #some weird patch/diff format from apraise/mealie?
        docData = update.document_data.replace('+', '')
        parsed = json.loads(docData)
        details = ShoppingListUpdate(**parsed)
        for itemID in details.shoppingListItemIds:

            listItem = mealieShoppingList.getListItem(itemID)

            if not listItem.labelId:
                chosenLabel = getLabelAssignment(session, listItem, labelEmbeddings) 
                listItem.labelId = chosenLabel.label.id
                listItem.label = chosenLabel.label
                mealieShoppingList.updateListItem(listItem)

            get_repositories(session).listItemRepo.storeLabelAssignment(listItem)



        return 200
    return router