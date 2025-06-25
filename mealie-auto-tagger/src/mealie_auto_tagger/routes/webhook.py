import json
from logging import getLogger
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from mealie_auto_tagger.model.mealie.notifiedMessage import NotifiedMessage, ShoppingListUpdate
from mealie_auto_tagger.model.mealieLableEmbeddings import MealieLabelEmbedding, MealieLabelEmbeddings
from mealie_auto_tagger.services.mealieShoppingList import mealieShoppingList
from mealie_auto_tagger.services.embedding.embeddingService import embeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem

from mealie_auto_tagger.db.repos.all_repositories import get_repositories
from mealie_auto_tagger.db.init import fast_API_depends_generate_session

logger = getLogger()

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
            try:
                listItem = mealieShoppingList.getListItem(itemID)
                if not listItem.labelId:
                    chosenLabel = getLabelAssignment(session, listItem, labelEmbeddings) 
                    listItem.labelId = chosenLabel.label.id
                    listItem.label = chosenLabel.label
                    mealieShoppingList.updateListItem(listItem)

                get_repositories(session).listItemRepo.storeLabelAssignment(listItem)
            except Exception as e:
               logger.error("Failed to process list item: "+ str(e)) 

        return 200
    return router