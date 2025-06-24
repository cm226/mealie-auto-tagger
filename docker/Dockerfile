
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
# pre-install CPU torch, to keep the image size down. Otherwise pip will install GPU version as well (~10GB)
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r /dist/requirements.txt

ENTRYPOINT ["mealieAT"]