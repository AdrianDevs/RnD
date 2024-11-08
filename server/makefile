# Variables
APP_NAME := Tracking-Suits
VERSION := 0.0.1
# SERVER_DIR := ./server
# CLIENT_DIR := ./client

# Settings
# COMPOSE_UP := docker compose up --detach
COMPOSE_UP := docker compose up --detach
COMPOSE_DOWN := docker compose down
PY_DEPENCIES := poetry install
PY_MIGRATE_CREATE := python manage.py makemigrations
PY_MIGRATE := python manage.py migrate
PY_RUN := python manage.py runserver

# Default rule to build the binary
all: start

# Start running containers
up:
	@echo "Start running containers..."
	$(COMPOSE_UP)
	@echo "Start containers complete!"

# Stop running containers
down:
	@echo "Stopping running containers..."
	$(COMPOSE_DOWN)
	@echo "Stopping containers complete!"

# Run the application
start: up
	@echo "Running $(APP_NAME)..."
	$(PY_RUN)

# Stop running containers and clean the build
stop:
	@echo "Stopping..."
	# TODO stop the server
	make down

# Run tests
test:
	@echo "Running tests..."
	# TODO: Add test command

# Install dependencies
deps:
	@echo "Installing dependencies..."
	$(PY_DEPENCIES)

# Add a rule for versioning
version:
	@echo "$(APP_NAME) version $(VERSION)"

# Create migrations
migrate-create:
	@echo "Creating migrations..."
	${PY_MIGRATE_CREATE}

# Apply migrations
migrate-apply:
	@echo "Applying migrations..."
	${PY_MIGRATE}

# Help command to display usage of the Makefile
help:
	@echo "Usage:"
	@echo "  make          				- Start containers and start the server"
	@echo "  make start    				- Start containers and start the server"
	@echo "  make stop     				- Stop containers and stop the server"
	@echo "  make up       				- Start running containers"
	@echo "  make down     				- Stop running containers"
	@echo "  make test     				- Run tests"
	@echo "  make deps     				- Install dependencies"
	@echo "  make version  				- Show application version"
	@echo "  make migrate-create	- Create migrations"
	@echo "  make migrate-apply  	- Apply migrations"
	@echo "  make help     				- Show this help message"