
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


################################################
## Production Image
################################################
FROM python-base AS production

COPY --from=builder /dist /dist/
RUN pip install /dist/mealie_auto_tagger-0.1.0-py3-none-any.whl

ENTRYPOINT ["mealieAT"]