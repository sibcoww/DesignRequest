"""
Unit tests for DesignRequest application.
Tests the database module and validates core functionality.
"""

import unittest
import os
import sqlite3
from datetime import datetime, timedelta
from database import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    """Test cases for DatabaseManager class."""

    def setUp(self):
        """Set up test database."""
        self.test_db = "test_design_requests.db"
        # Remove test database if it exists
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.db = DatabaseManager(self.test_db)

    def tearDown(self):
        """Clean up test database."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_database_initialization(self):
        """Test that database is properly initialized."""
        self.assertTrue(os.path.exists(self.test_db))
        
        # Verify table exists
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='design_requests'"
        )
        result = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(result)

    def test_add_request_success(self):
        """Проверка успешного добавления заявки."""
        result = self.db.add_request(
            "Тестовый клиент",
            "test@email.com",
            "Дизайн логотипа",
            "Тестовое описание",
            "2026-03-01"
        )
        self.assertTrue(result)
        
        # Verify request was added
        requests = self.db.get_all_requests()
        self.assertEqual(len(requests), 1)

    def test_add_request_missing_client_name(self):
        """Test that adding request without client name fails."""
        result = self.db.add_request(
            "",  # Empty client name
            "test@email.com",
            "Logo Design",
            "Test description",
            "2026-03-01"
        )
        self.assertFalse(result)

    def test_add_request_missing_project_type(self):
        """Test that adding request without project type fails."""
        result = self.db.add_request(
            "Test Client",
            "test@email.com",
            "",  # Empty project type
            "Test description",
            "2026-03-01"
        )
        self.assertFalse(result)

    def test_get_all_requests(self):
        """Test retrieving all requests."""
        # Add multiple requests
        for i in range(3):
            self.db.add_request(
                f"Клиент {i}",
                f"contact{i}@email.com",
                "Веб-дизайн",
                f"Описание {i}",
                "2026-03-01"
            )
        
        requests = self.db.get_all_requests()
        self.assertEqual(len(requests), 3)

    def test_get_request_by_id(self):
        """Test retrieving a specific request by ID."""
        # Add a request
        self.db.add_request(
            "Тестовый клиент",
            "test@email.com",
            "Дизайн логотипа",
            "Тестовое описание",
            "2026-03-01"
        )
        
        # Retrieve it
        request = self.db.get_request_by_id(1)
        self.assertIsNotNone(request)
        self.assertEqual(request[1], "Тестовый клиент")  # client_name

    def test_update_request(self):
        """Test updating a request."""
        # Add a request
        self.db.add_request(
            "Старое имя",
            "old@email.com",
            "Дизайн логотипа",
            "Старое описание",
            "2026-03-01"
        )
        
        # Update it
        result = self.db.update_request(
            1,
            "Новое имя",
            "new@email.com",
            "Дизайн логотипа",
            "Новое описание",
            "В работе",
            "2026-03-15"
        )
        self.assertTrue(result)
        
        # Verify update
        request = self.db.get_request_by_id(1)
        self.assertEqual(request[1], "Новое имя")
        self.assertEqual(request[5], "В работе")

    def test_delete_request(self):
        """Test deleting a request."""
        # Add a request
        self.db.add_request(
            "Test Client",
            "test@email.com",
            "Logo Design",
            "Test description",
            "2026-03-01"
        )
        
        # Delete it
        result = self.db.delete_request(1)
        self.assertTrue(result)
        
        # Verify deletion
        request = self.db.get_request_by_id(1)
        self.assertIsNone(request)

    def test_search_by_client_name(self):
        """Test searching by client name."""
        # Add requests with different names
        self.db.add_request("Техно Компания", "tech@email.com", "Веб-дизайн", "Desc1", "2026-03-01")
        self.db.add_request("Креативная студия", "creative@email.com", "Дизайн логотипа", "Desc2", "2026-03-01")
        self.db.add_request("Тех Стартап", "startup@email.com", "Мобильное приложение", "Desc3", "2026-03-01")
        
        # Search for "Тех"
        results = self.db.search_by_client_name("Тех")
        self.assertEqual(len(results), 2)

    def test_filter_by_status(self):
        """Test filtering by status."""
        # Add requests with different statuses
        self.db.add_request("Клиент1", "c1@email.com", "Веб-дизайн", "Desc1", "2026-03-01")
        self.db.add_request("Клиент2", "c2@email.com", "Дизайн логотипа", "Desc2", "2026-03-01")
        
        # Change status of second request
        self.db.update_status(2, "В работе")
        
        # Filter by "Новая"
        new_requests = self.db.filter_by_status("Новая")
        self.assertEqual(len(new_requests), 1)
        
        # Filter by "В работе"
        in_progress = self.db.filter_by_status("В работе")
        self.assertEqual(len(in_progress), 1)

    def test_update_status(self):
        """Test updating request status."""
        # Add a request
        self.db.add_request(
            "Test Client",
            "test@email.com",
            "Logo Design",
            "Test description",
            "2026-03-01"
        )
        
        # Update status
        result = self.db.update_status(1, "Завершена")
        self.assertTrue(result)
        
        # Verify status change
        request = self.db.get_request_by_id(1)
        self.assertEqual(request[5], "Завершена")

    def test_get_status_counts(self):
        """Test getting status counts."""
        # Add requests with different statuses
        self.db.add_request("Client1", "c1@email.com", "Web Design", "Desc1", "2026-03-01")
        self.db.add_request("Client2", "c2@email.com", "Logo Design", "Desc2", "2026-03-01")
        self.db.add_request("Client3", "c3@email.com", "Mobile App", "Desc3", "2026-03-01")
        
        # Update statuses
        self.db.update_status(2, "В работе")
        self.db.update_status(3, "Завершена")
        
        # Get counts
        counts = self.db.get_status_counts()
        
        self.assertEqual(counts.get("Новая", 0), 1)
        self.assertEqual(counts.get("В работе", 0), 1)
        self.assertEqual(counts.get("Завершена", 0), 1)

    def test_empty_database_operations(self):
        """Test operations on empty database."""
        # Get all requests
        requests = self.db.get_all_requests()
        self.assertEqual(len(requests), 0)
        
        # Search
        results = self.db.search_by_client_name("NonExistent")
        self.assertEqual(len(results), 0)
        
        # Filter
        filtered = self.db.filter_by_status("New")
        self.assertEqual(len(filtered), 0)


class TestDataValidation(unittest.TestCase):
    """Test data validation."""

    def setUp(self):
        """Set up test database."""
        self.test_db = "test_validation.db"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.db = DatabaseManager(self.test_db)

    def tearDown(self):
        """Clean up test database."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_default_status_is_new(self):
        """Проверка, что статус по умолчанию – 'Новая'."""
        self.db.add_request(
            "Test Client",
            "test@email.com",
            "Logo Design",
            "Test",
            "2026-03-01"
        )
        
        request = self.db.get_request_by_id(1)
        self.assertEqual(request[5], "Новая")

    def test_created_at_timestamp(self):
        """Test that created_at timestamp is set."""
        self.db.add_request(
            "Test Client",
            "test@email.com",
            "Logo Design",
            "Test",
            "2026-03-01"
        )
        
        request = self.db.get_request_by_id(1)
        created_at = request[7]
        
        # Verify it's a valid datetime string
        try:
            datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
            is_valid = True
        except ValueError:
            is_valid = False
        
        self.assertTrue(is_valid)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestDatabaseManager))
    suite.addTests(loader.loadTestsFromTestCase(TestDataValidation))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    sys.exit(run_tests())
