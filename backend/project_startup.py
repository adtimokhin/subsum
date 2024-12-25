from app.core.db import create_db_and_tables

def initialize_database():
    """
    Initializes the database by creating all necessary tables.
    """
    print("Initializing database...")
    create_db_and_tables()
    print("Database initialized successfully.")

def pre_start_tasks():
    """
    Run all pre-startup tasks for the project.
    """
    print("Running pre-startup tasks...")
    initialize_database()
    # Add additional startup tasks here if needed
    print("All pre-startup tasks completed.")
