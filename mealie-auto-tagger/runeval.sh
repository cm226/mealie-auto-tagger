echo "| model | accuracy score |"
echo "| --- | --- |"
poetry run python src/modelEval.py all-MiniLM-L12-v2
poetry run python src/modelEval.py all-MiniLM-L6-v2
poetry run python src/modelEval.py paraphrase-MiniLM-L6-v2
poetry run python src/modelEval.py DivyaMereddy007/RecipeBert_v5
poetry run python src/modelEval.py GPTasty/TastyRecipeEmbedder
poetry run python src/modelEval.py BAAI/bge-small-en-v1.5
