# Gunicorn config variables

workers = 1  # Number of worker processes
timeout = 120  # Timeout for worker processes
keepalive = 100  # Maximum number of requests a worker will process before restarting

# Logging config
accesslog = "-"  # Log requests to stdout
errorlog = "-"  # Log errors to stdout
loglevel = "info"  # Log level (debug, info, warning, error, critical)

# Worker class and type
worker_class = "sync"  # Use synchronous workers
worker_connections = 1000  # Maximum number of simultaneous clients

# Set the maximum number of requests a worker will process before restarting
max_requests = 1000
max_requests_jitter = 100

# Enable preloading the application code before the worker processes are forked
preload_app = True
