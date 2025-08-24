import json
from logging import getLogger
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from mealie_auto_tagger.model.mealie.notifiedMessage import NotifiedMessage, ShoppingListUpdate
from mealie_auto_tagger.model.mealieLableEmbeddings import MealieLabelEmbeddings
from mealie_auto_tagger.services.mealieShoppingList import mealieShoppingList
from mealie_auto_tagger.services.embedding.embeddingService import embeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
from mealie_auto_tagger.services.embedding.labelEmbeddingsService import labelEmbeddingsService

from mealie_auto_tagger.db.repos.all_repositories import get_repositories
from mealie_auto_tagger.db.init import fast_API_depends_generate_session

logger = getLogger()
labelEmbeddings = labelEmbeddingsService.computeLabelEmbeddings()

def getLabelAssignment(
    session: Session,
    listItem : MealieShoppingListItem,
    labelEmbeddings : MealieLabelEmbeddings):
    userSelectedListItemLabel = \
        get_repositories(session)\
            .listItemRepo\
            .getListItemFor(listItem.display)
    if userSelectedListItemLabel != None:
        userLabel = labelEmbeddings.getLabelByID(userSelectedListItemLabel.label)
        if userLabel == None:
            logger.error("Inconsistant user selected database cache detected!!")
        return userLabel
    return embeddingService.findClosest(listItem.display, labelEmbeddings)

def assignLabelToListItem(listItem : MealieShoppingListItem, session, labelEmbeddings):
    chosenLabel = getLabelAssignment(session, listItem, labelEmbeddings)
    if chosenLabel != None:
        listItem.labelId = chosenLabel.label.id
        listItem.label = chosenLabel.label
    return listItem

def makeRouter():
    router = APIRouter(prefix="/webhooks")

    @router.post("/post/")
    def notified_from_meaile(
        update: NotifiedMessage,
        session = Depends(fast_API_depends_generate_session)):
        global labelEmbeddings

        #some weird patch/diff format from apraise/mealie?
        docData = update.document_data.replace('+', '')
        parsed = json.loads(docData)
        details = ShoppingListUpdate(**parsed)
        for itemID in details.shoppingListItemIds:
            try:
                listItem = mealieShoppingList.getListItem(itemID)
                if not listItem.labelId:
                    listItem = assignLabelToListItem(listItem, session, labelEmbeddings)
                    mealieShoppingList.updateListItem(listItem)
                get_repositories(session).listItemRepo.storeLabelAssignment(listItem)
            except Exception as e:
                logger.error("Failed to process list item: "+ str(e))
        return 200
    return router
