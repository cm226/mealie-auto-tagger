echo "| model | accuracy score |"
echo "| --- | --- |"

SCRIPT=src/mealie_auto_tagger/modelEval.py
poetry run python $SCRIPT all-MiniLM-L12-v2
poetry run python $SCRIPT all-MiniLM-L6-v2
poetry run python $SCRIPT paraphrase-MiniLM-L6-v2
poetry run python $SCRIPT DivyaMereddy007/RecipeBert_v5
poetry run python $SCRIPT GPTasty/TastyRecipeEmbedder
poetry run python $SCRIPT BAAI/bge-small-en-v1.5
