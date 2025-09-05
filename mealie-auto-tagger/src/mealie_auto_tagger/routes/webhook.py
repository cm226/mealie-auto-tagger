# pylint: disable=missing-module-docstring

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


def get_label_assignment(
        session: Session,
        list_item: MealieShoppingListItem,
        label_embeddings: MealieLabelEmbeddings):
    user_selected_list_item_label = \
        get_repositories(session)\
        .listItemRepo\
        .getListItemFor(list_item.display)
    if user_selected_list_item_label is not None:
        user_label = label_embeddings.getLabelByID(
            user_selected_list_item_label.label)
        if user_label is None:
            logger.error(
                "Inconsistant user selected database cache detected!!")
        return user_label
    return embeddingService.findClosest(list_item.display, label_embeddings)


def assign_label_to_list_item(list_item: MealieShoppingListItem, session, label_embeddings):
    chosen_label = get_label_assignment(session, list_item, label_embeddings)
    if chosen_label is not None:
        list_item.labelId = chosen_label.label.id
        list_item.label = chosen_label.label
    return list_item


def make_router():
    router = APIRouter(prefix="/webhooks")

    @router.post("/post/")
    def notified_from_meaile(
            update: NotifiedMessage,
            session=Depends(fast_API_depends_generate_session)):

        # some weird patch/diff format from apraise/mealie?
        doc_data = update.document_data.replace('+', '')
        parsed = json.loads(doc_data)
        details = ShoppingListUpdate(**parsed)
        for item_id in details.shoppingListItemIds:
            try:
                list_item = mealieShoppingList.getListItem(item_id)
                if not list_item.labelId:
                    list_item = assign_label_to_list_item(
                        list_item, session, labelEmbeddings)
                    mealieShoppingList.updateListItem(list_item)
                get_repositories(
                    session).listItemRepo.storeLabelAssignment(list_item)
            # pylint: disable=broad-exception-caught
            except Exception as e:
                logger.error("Failed to process list item: %s", str(e))
        return 200
    return router
