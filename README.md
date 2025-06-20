# Mealie auto label

Mealie auto label is a mealie add-on for automatically labeling items added to shopping lists. 


## Configuration

### host
> URL that mealie can use to reach mealie auto label

### mealie_url
> URL that mealie auto tagger can use to reach mealie

### mealie_user
> Username to use for mealie

### mealie_pw
> Password to use for mealie

### labels
> A list of labels to use for categorization


Configuration is applied though environment variables

## Accuracy 

Dataset used for evaluation : https://huggingface.co/datasets/Scuccorese/food-ingredients-dataset

Randomly sampled 100 cases

Accuracy = correct / total

[Current results](./mealie-auto-tagger/modelResults.md)