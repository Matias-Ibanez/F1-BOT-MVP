FROM python:3.13-slim

WORKDIR /app

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#Ya que docker cachea las capas, si no se cambia el pyproject.toml o el uv.lock,
#no se volverán a instalar las dependencias, lo que hace que el proceso de construcción sea más rápido.

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]