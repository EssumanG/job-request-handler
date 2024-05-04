# Job Request Handler

## Overview
    The Job Request Handler is a microservice responsible for handling GET requests from users, processing the requests, and pushing them to a queue for further processing. This service acts as the entry point for job requests and ensures that incoming requests are validated and formatted correctly before being sent to the job processing queue.

## Features

- **Handles POST requests from users**
- **Validates and processes incoming requests**
- **Pushes requests to a queue for further processing**
- **Returns a response to the user indicating the status of their request**


## Technical Details
- **Programming Language**: Python
- **Framework**: FastAPI
- **Queueing System**: RabbitMQ

## Setup and Installation

1. **Clone the repository** : https://github.com/EssumanG/job-request-handler.git
2. **Install dependencies**: pip install -r requirements.txt 
3. **Configure environment** variables (e.g., queue connection settings)
4. **Start the service**: 
        
     ```bash
            uvicorn main:app --reload

## Endpoints
- **/job**: Handles POST requests from users, processes the requests, and pushes them to the queue.
    ### Request Body"

    - **email**: The email address of the user making the request
    - **"search_term**: The type of job the user is requestin
    - **location**: The location of the job