all: start
	@echo "Starting..."

docker-all: docker-build docker-start
	@echo "Done..."

docker-build:
	@echo "Building image from docker file..."
	docker build --no-cache --pull -t zwlevy/tetris:latest .
	@echo "Image done..."

docker-start:
	@echo "Starting new service in container..."
	docker run -v /home/:/home/ -p 8080:8080 zwlevy/tetris

service:
	@echo "Creating service..."
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	@echo "Starting new service..."
	pip install --upgrade pip
	pip install -r requirements.txt
	python server.py

docker-stop:
	@echo "Stopping service..."
	docker stop $$(docker ps -alq)
	@echo "Service has been stopped."

docker-remove:
	@echo "Removing image..."
	docker rmi -f zwlevy/tetris
	@echo "Image has been removed."

docker-clean: docker-stop docker-remove
	@echo "DONE"

clean:
	@echo "Removing service files created..."
	rm -rf $(CREATED)
