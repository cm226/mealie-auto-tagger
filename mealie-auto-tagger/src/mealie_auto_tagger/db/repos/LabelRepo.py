from sqlalchemy import Select

from mealie_auto_tagger.db.repos.RepoBase import RepoBase
from mealie_auto_tagger.db.models.label import Label

from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel as MealieLabel

class LabelRepo(RepoBase):
    def storeAllMealieLabels(self, mealieLabels: list[MealieLabel]):

        labelIds = {label.id for label in mealieLabels}
        existing = self.session.execute(
            Select(Label.id).where(Label.id.in_(labelIds))
        ).scalars().all()

        missingLabels = set(labelIds) - set(existing)
        
        for missing in missingLabels:
            self.session.add(Label(id = missing))

        self.session.commit()