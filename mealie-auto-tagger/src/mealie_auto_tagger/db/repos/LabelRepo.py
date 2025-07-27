from sqlalchemy import Select

from mealie_auto_tagger.db.repos.RepoBase import RepoBase
from mealie_auto_tagger.db.models.label import Label

from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel as MealieLabel

class LabelRepo(RepoBase):
    def storeAllMealieLabels(self, mealieLabels: list[MealieLabel]):

        labelIds = {label.id for label in mealieLabels}
        existing = self.session.execute(
            Select(Label.id)
        ).scalars().all()

        missingLabels = set(labelIds) - set(existing)
        
        for missing in missingLabels:
            self.session.add(Label(id = missing))

        extraLabeld = set(existing) - set(labelIds)
        for extra in extraLabeld:
            label = self.session.get(Label, extra)
            self.session.delete(label)


        self.session.commit()