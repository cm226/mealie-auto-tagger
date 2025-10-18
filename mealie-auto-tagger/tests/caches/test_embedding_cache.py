import pytest

from mealie_auto_tagger.caches.embedding_cache import _EmbeddingCache
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel


@pytest.fixture
def new_cache():
    return _EmbeddingCache()


def test_cache_creates(new_cache: _EmbeddingCache,  # pylint: disable=redefined-outer-name
                       test_label1: MealieLabel,
                       test_label2: MealieLabel):
    embedding1 = new_cache.get_label_embedding(test_label1)
    embedding2 = new_cache.get_label_embedding(test_label2)
    assert embedding1 is not None
    assert embedding2 is not None
    assert embedding1 != embedding2


def test_cache_caches(new_cache: _EmbeddingCache,  # pylint: disable=redefined-outer-name
                      test_label1: MealieLabel):
    embedding1 = new_cache.get_label_embedding(test_label1)
    embedding2 = new_cache.get_label_embedding(test_label1)
    assert embedding2 == embedding1
