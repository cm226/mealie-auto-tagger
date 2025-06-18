FROM huggingface/transformers-pytorch-gpu


RUN pip install sentence_transformers
WORKDIR /src

COPY ./setup.py ./setup.py
# download the models/datasets
RUN python3 setup.py

COPY ./main.py ./main.py

CMD python /src/main.py
