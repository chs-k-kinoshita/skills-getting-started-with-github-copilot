"""Shared pytest fixtures for FastAPI app tests"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def clean_activities():
    """Reset activities to known state before each test"""
    # Save original state
    original_activities = {
        key: {**value, "participants": value["participants"].copy()}
        for key, value in activities.items()
    }
    
    yield  # Run the test
    
    # Restore original state
    for key in activities:
        activities[key]["participants"] = original_activities[key]["participants"].copy()
