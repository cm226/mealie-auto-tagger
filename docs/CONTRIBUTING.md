# Contributing Guide

Thank you for your interest in contributing!

## Development Setup

To get started with development, follow these steps:

1. **Use VS Code Dev Container**  
   This project is configured to use a Visual Studio Code Dev Container. Make sure you have the dev container extension installed in VS Code.

2. **Set Up Environment Variables**  
   Before running the project, you will need to create a Mealie API token.

   - Obtain your token from your Mealie instance.
   - Create the file ../mealie-auto-tagger/src/.env.dev file and paste in your token:

     ```env
     mealie_api_token=your_token_here
     ```
3. **Run the Project**  
   You can run the project using `F5` inside the Dev Container environment.


That’s it! You should now be ready to start developing.
