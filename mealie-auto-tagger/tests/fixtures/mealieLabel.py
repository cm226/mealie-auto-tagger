import pytest
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel

@pytest.fixture
def test_label1():
    return MealieLabel(name="test_label1", color="blue", groupId="123",id="1")


@pytest.fixture
def test_label2():
    return MealieLabel(name="test_label2", color="blue", groupId="123",id="2")