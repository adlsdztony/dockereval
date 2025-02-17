FROM runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04

WORKDIR /app

COPY ./MixEval .

COPY ./.env /app/

COPY ./llamacpp.py /app/mix_eval/models/llamacpp.py

# edit /app/mix_eval/models/__init__.py
# add at second line:
# "llamacpp": "LLAMACPP",
RUN sed -i '2i\    "llamacpp": "LLAMACPP",\n' /app/mix_eval/models/__init__.py

RUN pip install -e . && \
    pip install flash-attn --no-build-isolation && \
    rm -rf /root/.cache/pip

ENTRYPOINT ["python3"]