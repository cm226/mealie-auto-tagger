import pytest

from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.db.repos.all_repositories import AllRepositories

from mealie_auto_tagger.db.models.label import Label
        
class hasID:
    def __init__(self, id):
        self.id = id
    def __eq__(self, other):
        return hasattr(other, 'id') and getattr(other, 'id') == self.id

def set_db_content(session, labels : list[int]):
    session.execute.return_value.scalars.return_value.all.return_value = labels


def test_store_new_labels(mocker, test_label1: MealieLabel):
    mock_session = mocker.MagicMock()
    all = AllRepositories(mock_session)
    lableRepo = all.labelRepo

    lableRepo.storeAllMealieLabels([test_label1])

    mock_session.add.assert_called_once_with(hasID(test_label1.id))
    mock_session.delete.assert_not_called()
    mock_session.commit.assert_called_once()

def test_delete_old(mocker, test_label1, test_label2):
    
    session = mocker.MagicMock()
    all = AllRepositories(session)
    lableRepo = all.labelRepo
    set_db_content(session, [test_label2.id])
    lableRepo.storeAllMealieLabels([test_label1])

    session.add.assert_called_once_with(hasID(test_label1.id))
    session.delete.assert_called_once_with(session.get(Label, test_label2.id))
    session.commit.assert_called_once()


def test_no_change(mocker, test_label1):
    
    session = mocker.MagicMock()
    set_db_content(session, [test_label1.id])
    all = AllRepositories(session)
    lableRepo = all.labelRepo

    lableRepo.storeAllMealieLabels([test_label1])

    session.add.assert_not_called()
    session.delete.assert_not_called()
    session.commit.assert_called_once()