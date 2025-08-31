compose = docker compose -f docker-compose.dev.yml

.PHONY: dev up down logs migrate
dev: up
up:
	$(compose) up -d --build
down:
	$(compose) down -v
logs:
	$(compose) logs -f --tail=200
migrate:
	$(compose) run --rm api bash -lc "alembic upgrade head"
