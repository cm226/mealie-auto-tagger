from mealie_auto_tagger.db.repos.RepoBase import RepoBase
from mealie_auto_tagger.db.models.label import ListItem, Label
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
from sqlalchemy import select


class ListItemRepo(RepoBase):
    def getListItemFor(self, name: str):
        q = select(ListItem)\
            .where(ListItem.name.is_(name))

        rows = self.session.execute(q).all()
        if len(rows) > 0:
            return rows[0]._tuple()[0]
        return None

    def storeLabelAssignment(self, item: MealieShoppingListItem):
        from mealie_auto_tagger.db.models.label import ListItem

        result = self.getListItemFor(item.display)
        if not result:
            listItem = ListItem(name=item.display, label=item.labelId)
        else:
            listItem = result

        listItem.label = item.labelId  # type: ignore
        self.session.add(listItem)
        self.session.commit()
