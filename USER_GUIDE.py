"""
Complete User Guide for DesignRequest Application
"""

# ================================================================================
# DESIGNREQUEST - COMPLETE USER GUIDE
# ================================================================================

# PROJECT OVERVIEW
# ================================================================================
# DesignRequest is a desktop application for managing design project requests.
# It provides a user-friendly interface for tracking client requests, project types,
# deadlines, and project status throughout the lifecycle.

# REQUIREMENTS
# ================================================================================
# - Python 3.7 or higher
# - Windows, macOS, or Linux operating system
# - No internet connection required (all data stored locally)
# - 50 MB free disk space

# INSTALLATION & STARTUP
# ================================================================================

# Option 1: Direct Python Execution
# -----------------------------------
# 1. Navigate to the project directory
# 2. Run: python main.py

# Option 2: Using Launch Script (Windows)
# ----------------------------------------
# 1. Double-click run.bat
# 2. Application window will open

# Option 3: Using Launch Script (Linux/macOS)
# ------------------------------------
# 1. Make script executable: chmod +x run.sh
# 2. Run: ./run.sh

# FILE STRUCTURE
# ================================================================================
# DesignRequest/
# ├── main.py                  # Main GUI application
# ├── database.py              # Database operations module
# ├── config.py                # Configuration settings
# ├── examples.py              # Usage examples
# ├── test_database.py         # Unit tests
# ├── design_requests.db       # SQLite database (created automatically)
# ├── run.bat                  # Windows launcher
# ├── run.sh                   # Linux/macOS launcher
# ├── README.md                # Project documentation
# └── requirements.txt         # Dependencies (Python standard library only)

# GETTING STARTED
# ================================================================================

# 1. MAIN INTERFACE
#    The application window consists of several sections:
#    - Request Details Panel: Input fields for entering request information
#    - Search & Filter Panel: Tools for finding and filtering requests
#    - Request Table: Displays all requests with their details
#    - Action Buttons: Add, Update, Delete, Change Status, Clear, Show All

# 2. ADDING A NEW REQUEST
#    Steps:
#    a) Fill in the required fields:
#       - Client Name: Name of the client (required)
#       - Project Type: Select from dropdown (required)
#    
#    b) Optionally fill in:
#       - Contact Info: Phone, email, or other contact details
#       - Description: Detailed project description (can be multi-line)
#       - Deadline: In format YYYY-MM-DD (e.g., 2026-03-15)
#    
#    c) Click "Add Request" button
#    d) Success message confirms the request was added
#    e) Request appears in the table with status "New"

# 3. SELECTING AND EDITING A REQUEST
#    Steps:
#    a) Click on any row in the request table to select it
#    b) Selected request details automatically populate the input fields
#    c) Modify any fields as needed
#    d) Click "Update Request" to save changes
#    e) Table updates to show new values

# 4. CHANGING REQUEST STATUS
#    Quick Method:
#    a) Click on a request in the table
#    b) Select new status from dropdown (New, In Progress, On Review, Completed)
#    c) Click "Change Status" button
#    
#    Status meanings:
#    - New: Newly received request
#    - In Progress: Currently being worked on
#    - On Review: Awaiting client review or approval
#    - Completed: Finished and delivered to client

# 5. DELETING A REQUEST
#    Steps:
#    a) Click on the request to select it
#    b) Click "Delete Request" button
#    c) Confirmation dialog appears
#    d) Click "Yes" to confirm deletion
#    e) Request is permanently removed from database

# 6. SEARCHING FOR REQUESTS
#    Steps:
#    a) Enter client name (or part of it) in search field
#    b) Click "Search" button
#    c) Table shows only matching requests
#    d) Click "Show All" to see all requests again
#    
#    Note: Search is case-insensitive and matches partial names

# 7. FILTERING BY STATUS
#    Steps:
#    a) Select a status from the "Filter by Status" dropdown
#    b) Table automatically updates to show only requests with that status
#    c) Select "All" to show all requests regardless of status

# 8. CLEARING INPUT FIELDS
#    - Click "Clear Fields" button to reset all input fields to default values
#    - Useful when starting to add a new request

# DATA FIELD DESCRIPTIONS
# ================================================================================

# ID: Unique request identifier (auto-generated)
# Client Name: Name of the client requesting the design work
# Contact Info: Phone number, email, or other contact information
# Project Type: Category of design work (Logo, Web, Mobile, UI/UX, Other)
# Status: Current state of the request (New, In Progress, On Review, Completed)
# Deadline: Target completion date in YYYY-MM-DD format
# Description: Detailed project requirements and specifications
# Created At: Automatic timestamp when request was added

# PROJECT TYPES
# ================================================================================
# • Logo Design: Creating or redesigning company logos
# • Web Design: Designing websites and web interfaces
# • Mobile App: Designing mobile application interfaces
# • UI/UX Design: User interface and user experience design
# • Other: Custom project types not listed above

# TIPS & BEST PRACTICES
# ================================================================================

# 1. DATA ENTRY TIPS
#    - Always fill in Client Name and Project Type (required fields)
#    - Use consistent formatting for contact information
#    - Keep descriptions concise but informative
#    - Use YYYY-MM-DD format for deadlines (example: 2026-03-15)

# 2. STATUS WORKFLOW
#    Recommended workflow:
#    New → In Progress → On Review → Completed
#    
#    This helps track project lifecycle:
#    - New: Initial receipt of request
#    - In Progress: Designer actively working
#    - On Review: Waiting for client feedback
#    - Completed: Project finalized and delivered

# 3. REGULAR BACKUPS
#    The database file (design_requests.db) contains all your data.
#    Regular backups recommended:
#    - Copy design_requests.db to external drive
#    - Backup weekly or after major updates

# 4. SEARCH STRATEGIES
#    - Search by first name or last name
#    - Search by company name
#    - Partial matches work (e.g., "Tech" finds "TechStart Inc")

# 5. BULK OPERATIONS
#    Current limitations:
#    - Delete: One request at a time
#    - Export: Use sqlite3 command line for advanced exports
#    - Bulk update: Not available via GUI

# KEYBOARD SHORTCUTS
# ================================================================================
# Tab: Move to next field
# Shift+Tab: Move to previous field
# Enter: In some fields, submits the form
# Ctrl+A: Select all text in a field

# TROUBLESHOOTING
# ================================================================================

# Issue: "Python not found" error
# Solution: Install Python 3.7+ from python.org

# Issue: "No module named tkinter"
# Windows: Usually installed with Python
# Linux (Ubuntu/Debian): sudo apt-get install python3-tk
# macOS: Usually included with Python installation

# Issue: Application window won't open
# Solution: Check Windows/macOS firewall settings

# Issue: "Database error" message
# Solution: 
# - Check disk space
# - Verify file permissions
# - Restart the application
# - If persists, delete design_requests.db to start fresh

# Issue: Slow performance with many records
# Solution: Archive old completed requests to separate database

# Issue: Date format error
# Solution: Ensure deadline format is YYYY-MM-DD (example: 2026-03-15)

# ADVANCED USAGE
# ================================================================================

# Accessing Database from Command Line:
# sqlite3 design_requests.db
# 
# Useful SQL queries:
# SELECT * FROM design_requests;
# SELECT COUNT(*) FROM design_requests WHERE status='Completed';
# SELECT * FROM design_requests ORDER BY deadline;

# Exporting Data to CSV:
# sqlite3 -header -csv design_requests.db \
#   "SELECT * FROM design_requests;" > export.csv

# PERFORMANCE TIPS
# ================================================================================
# - Application handles 1000+ requests smoothly
# - Large descriptions (>10,000 characters) may slow down display
# - Regular cleanup of old completed requests improves performance

# SECURITY & DATA PROTECTION
# ================================================================================
# - Database file is plain SQLite (not encrypted)
# - Keep design_requests.db in secure location
# - No network transmission of data (all local)
# - Regular backups recommended

# UNINSTALLATION
# ================================================================================
# Simply delete the entire DesignRequest folder.
# All application data is stored in design_requests.db within that folder.

# SUPPORT & FEEDBACK
# ================================================================================
# For issues or feature requests, refer to README.md documentation.

# VERSION HISTORY
# ================================================================================
# v1.0 - Initial release with full CRUD functionality
# Features: Add, Edit, Delete, Search, Filter, Status management

# ================================================================================
# END OF USER GUIDE
# ================================================================================
