# User Guide for the Application

Welcome to the application! This guide will help you run and use the application smoothly. Follow the steps below:

## Prerequisites:

- Make sure you have Docker and Docker Compose installed on your machine. You can download them from [Docker Hub](https://hub.docker.com/).

## Step 1: Clone the Repository from GitHub

1. Open your terminal.
2. Run the following command to clone the repository from GitHub:

   ```bash
   git clone https://github.com/4ndr3steban/Second_quiz_submission.git
	```

## Step 2: Navigate to the Project Directory

Change to the project directory:

  

```bash
cd your-repository
```

## Step 3: Run the Application with Docker Compose

Run the following command to start the application with Docker Compose:

```bash
docker-compose up --build
```

This command will build and start the necessary containers for the application.

## Step 4: Access the Graphical Interface

Once the containers are up and running, open your web browser and go to:

```plaintext
http://localhost:9000
```

This will take you to the graphical interface of the application.

## Step 5: Use the Application

1. Fill out the form provided in the graphical interface with the required information.
2. Click the corresponding button to process the information.

That's it! The application should process the data and display the results based on the form you completed.

  ### Additional Notes:

If you need to stop the application, go to the terminal where you ran docker-compose up and press Ctrl + C. Then, run:

```bash
docker-compose down
```
If you encounter any issues or have questions, check the documentation in the GitHub repository or contact the developer.