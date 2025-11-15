FROM python:3.10-slim
# add your stuff here
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" ./
RUN uv sync --locked

COPY "/Scripts/predict.py" "/Scripts/streamlit_app.py" "/Scripts/model.bin" ./

EXPOSE 9696
EXPOSE 8501


ENTRYPOINT ["bash", "-c", "uvicorn predict:app --host 0.0.0.0 --port 9696 & streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0"]
