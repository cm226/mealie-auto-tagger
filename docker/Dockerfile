
###############################################
# Base Image
###############################################
FROM python:3.12-slim AS python-base


###############################################
# Builder Image
###############################################
FROM python-base AS builder

RUN pip install poetry
COPY ./mealie-auto-tagger /mealie-auto-tagger

WORKDIR /mealie-auto-tagger

RUN poetry build --output=/dist
RUN echo /dist/mealie_auto_tagger-$(poetry version --short)-py3-none-any.whl > /dist/requirements.txt


################################################
## Production Image
################################################
FROM python-base AS production

COPY --from=builder /dist /dist/
RUN pip install -r /dist/requirements.txt

ENTRYPOINT ["mealieAT"]