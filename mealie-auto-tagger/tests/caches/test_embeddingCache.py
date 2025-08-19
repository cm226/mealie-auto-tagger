import pytest

from mealie_auto_tagger.caches.embeddingCache import __EmbeddingCache
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel

@pytest.fixture
def new_cache():
    return __EmbeddingCache()


def test_cache_creates(new_cache: __EmbeddingCache, test_label1: MealieLabel, test_label2: MealieLabel):
    embedding1 = new_cache.getLabelEmbedding(test_label1)
    embedding2 = new_cache.getLabelEmbedding(test_label2)
    assert embedding1 != None
    assert embedding2 != None
    assert embedding1 != embedding2

def test_cache_caches(new_cache: __EmbeddingCache, test_label1: MealieLabel):
    embedding1 = new_cache.getLabelEmbedding(test_label1)
    embedding2 = new_cache.getLabelEmbedding(test_label1)
    assert embedding2 == embedding1
