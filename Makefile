run:
	docker run --rm -it --name Log-Streaming-Service -p 8000:8000 log-server

generate_logs:
	docker exec Log-Streaming-Service /bin/sh -c "python app/utils/log_generator.py"

build:
	docker build --tag=log-server .

stream:
	curl -N -Lv -H  "Accept:text/event-stream" http://localhost:8000/stream-logs
