from pydantic import BaseModel
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
from mealie_auto_tagger.model.mealie.notifier import Notifier, NoritierOptions
from mealie_auto_tagger.model.mealie.paginated import PaginatedQueryResp
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealie.notifiedMessage import NotifiedMessage


def shopping_list_item():
    return MealieShoppingListItem(
        quantity=1,
        display="",
        shoppingListId="",
        checked=False,
        position=1,
        id="sli1",
        groupId="",
        householdId="",
        createdAt="",
        updatedAt=""
    )


def notifier():
    return Notifier(id="", name="", appriseUrl="", enabled=True, groupId="", householdId="", options=NoritierOptions(
        testMessage=False,
        webhookTask=False,
        recipeCreated=False,
        recipeUpdated=False,
        recipeDeleted=False,
        userSignup=False,
        dataMigrations=False,
        dataExport=False,
        dataImport=False,
        mealplanEntryCreated=False,
        shoppingListCreated=False,
        shoppingListUpdated=False,
        shoppingListDeleted=False,
        cookbookCreated=False,
        cookbookUpdated=False,
        cookbookDeleted=False,
        tagCreated=False,
        tagUpdated=False,
        tagDeleted=False,
        categoryCreated=False,
        categoryUpdated=False,
        categoryDeleted=False,
        labelCreated=False,
        labelUpdated=False,
        labelDeleted=False,
        id=""))


def label():
    return MealieLabel(
        name="label",
        color="",
        groupId="",
        id="1")


def paginated[T](items: list[T]):
    return PaginatedQueryResp[T](
        page=0, per_page=len(items), total=len(items), total_pages=1, items=items, next=None, previous=None
    )


def notified_message(event: str, data: BaseModel):
    return NotifiedMessage(
        version="",
        title="",
        message="",
        attachments=[],
        type="",
        event_type=event,
        integration_id="",
        document_data=data.model_dump_json(),
        event_id="",
        timestamp="")
