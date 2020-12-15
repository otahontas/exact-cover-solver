### === Build frontend ===
FROM node:14.15.1-alpine3.12 as build

WORKDIR /app

# Copy dependencies and install them first
COPY web/ui/package.json ./
COPY web/ui/yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy code after installing dependencies for better caching
COPY web/ui/src/ ./src
COPY web/ui/public/ ./public

# Build production version
RUN yarn run build

### === Install server and add other settings ===
FROM pypy:3.6-7.3.1

# Install poetry
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry && poetry config virtualenvs.create false

# Copy exact-cover-solver library files to correct place
COPY pyproject.toml .
COPY poetry.lock .
COPY exact_cover_solver/ ./exact_cover_solver/

# Install server dependencies
WORKDIR /app/web/server
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY web/server/poetry.lock .
COPY web/server/pyproject.toml .
RUN poetry install --no-dev

# Copy server files, setup variables
COPY web/server/server.py .
ENV SERVER_ENV_MODE=production
ENV SERVER_SPA_LOCATION=/app/web/server/build
COPY --from=build /app/build /app/web/server/build

# Run the image as a non-root user
RUN useradd -m app
USER app

EXPOSE 8000
  
# Run the app with:
# - two pypy-compatible uvicorn workers
# - 180 second timeout for each worker
# CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn server:app --bind 0.0.0.0:$PORT -w 2 -k uvicorn.workers.UvicornH11Worker -t 180
