"""
Database module for DesignRequest application.
Handles SQLite database connection, initialization, and CRUD operations.
"""

import sqlite3
from datetime import datetime
from typing import List, Tuple, Optional, Dict, Any


class DatabaseManager:
    """Manages all database operations for the DesignRequest application."""

    def __init__(self, db_file: str = "design_requests.db"):
        """
        Initialize database manager.
        
        Args:
            db_file (str): Path to the SQLite database file.
        """
        self.db_file = db_file
        self.init_database()

    def init_database(self) -> None:
        """Initialize database and create table if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Create table with specified fields
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS design_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    contact_info TEXT,
                    project_type TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'Новая',
                    deadline TEXT,
                    created_at TEXT NOT NULL
                )
            ''')
            
            conn.commit()
            conn.close()
            print("Database initialized successfully.")
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def add_request(self, client_name: str, contact_info: str, 
                   project_type: str, description: str, 
                   deadline: str) -> bool:
        """
        Add a new design request to the database.
        
        Args:
            client_name (str): Name of the client.
            contact_info (str): Contact information.
            project_type (str): Type of the project.
            description (str): Project description.
            deadline (str): Project deadline.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Validate required fields
            if not client_name or not project_type:
                print("Ошибка: требуются имя клиента и тип проекта.")
                return False
            
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor.execute('''
                INSERT INTO design_requests 
                (client_name, contact_info, project_type, description, status, deadline, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (client_name, contact_info, project_type, description, 'Новая', deadline, created_at))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error adding request: {e}")
            return False

    def get_all_requests(self) -> List[Tuple[Any, ...]]:
        """
        Retrieve all design requests from the database.
        
        Returns:
            List[Tuple]: List of all requests.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM design_requests ORDER BY created_at DESC')
            requests = cursor.fetchall()
            conn.close()
            return requests
        except sqlite3.Error as e:
            print(f"Error retrieving requests: {e}")
            return []

    def get_request_by_id(self, request_id: int) -> Optional[Tuple[Any, ...]]:
        """
        Retrieve a specific request by ID.
        
        Args:
            request_id (int): ID of the request.
            
        Returns:
            Optional[Tuple]: Request data if found, None otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM design_requests WHERE id = ?', (request_id,))
            request = cursor.fetchone()
            conn.close()
            return request
        except sqlite3.Error as e:
            print(f"Error retrieving request: {e}")
            return None

    def update_request(self, request_id: int, client_name: str, 
                      contact_info: str, project_type: str, 
                      description: str, status: str, deadline: str) -> bool:
        """
        Update an existing design request.
        
        Args:
            request_id (int): ID of the request to update.
            client_name (str): Updated client name.
            contact_info (str): Updated contact info.
            project_type (str): Updated project type.
            description (str): Updated description.
            status (str): Updated status.
            deadline (str): Updated deadline.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Validate required fields
            if not client_name or not project_type:
                print("Error: Client name and project type are required.")
                return False
            
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE design_requests 
                SET client_name = ?, contact_info = ?, project_type = ?, 
                    description = ?, status = ?, deadline = ?
                WHERE id = ?
            ''', (client_name, contact_info, project_type, description, status, deadline, request_id))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error updating request: {e}")
            return False

    def delete_request(self, request_id: int) -> bool:
        """
        Delete a design request by ID.
        
        Args:
            request_id (int): ID of the request to delete.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM design_requests WHERE id = ?', (request_id,))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error deleting request: {e}")
            return False

    def search_by_client_name(self, client_name: str) -> List[Tuple[Any, ...]]:
        """
        Search for requests by client name (case-insensitive).
        
        Args:
            client_name (str): Client name to search for.
            
        Returns:
            List[Tuple]: List of matching requests.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM design_requests WHERE client_name LIKE ? ORDER BY created_at DESC',
                (f"%{client_name}%",)
            )
            requests = cursor.fetchall()
            conn.close()
            return requests
        except sqlite3.Error as e:
            print(f"Error searching requests: {e}")
            return []

    def filter_by_status(self, status: str) -> List[Tuple[Any, ...]]:
        """
        Filter requests by status.
        
        Args:
            status (str): Status to filter by.
            
        Returns:
            List[Tuple]: List of requests with the specified status.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM design_requests WHERE status = ? ORDER BY created_at DESC',
                (status,)
            )
            requests = cursor.fetchall()
            conn.close()
            return requests
        except sqlite3.Error as e:
            print(f"Error filtering requests: {e}")
            return []

    def update_status(self, request_id: int, new_status: str) -> bool:
        """
        Update the status of a specific request.
        
        Args:
            request_id (int): ID of the request.
            new_status (str): New status value.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE design_requests SET status = ? WHERE id = ?',
                (new_status, request_id)
            )
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error updating status: {e}")
            return False

    def get_status_counts(self) -> Dict[str, int]:
        """
        Get count of requests for each status.
        
        Returns:
            Dict[str, int]: Dictionary with status as key and count as value.
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(
                'SELECT status, COUNT(*) FROM design_requests GROUP BY status'
            )
            counts = dict(cursor.fetchall())
            conn.close()
            return counts
        except sqlite3.Error as e:
            print(f"Error getting status counts: {e}")
            return {}
