FROM huggingface/transformers-pytorch-gpu


RUN pip install sentence_transformers
WORKDIR /src

# download the models/datasets
COPY ./setup.py ./setup.py
RUN python3 setup.py

RUN pip install poetry



