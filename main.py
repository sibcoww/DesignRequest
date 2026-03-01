"""
GUI module for DesignRequest application.
Implements the Tkinter user interface for managing design project requests.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from database import DatabaseManager
from typing import Optional, List, Tuple, Any
import datetime

# configuration and localization
import config


class DesignRequestApp:
    """Main GUI application class for DesignRequest manager."""

    # Status options for dropdown
    STATUS_OPTIONS = config.STATUS_OPTIONS

    def __init__(self, root: tk.Tk):
        """
        Initialize the application.
        
        Args:
            root (tk.Tk): Root window object.
        """
        self.root = root
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)

        # Initialize database
        self.db = DatabaseManager("design_requests.db")

        # Currently selected request ID
        self.selected_request_id: Optional[int] = None

        # Setup GUI
        self.setup_gui()
        self.load_requests()

    def setup_gui(self) -> None:
        """Setup the main GUI layout."""
        # Create main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text=config.WINDOW_TITLE,
            font=config.FONT_TITLE
        )
        title_label.pack(pady=(0, 10))

        # Create input frame
        self.setup_input_frame(main_frame)

        # Create search and filter frame
        self.setup_search_frame(main_frame)

        # Create table frame
        self.setup_table_frame(main_frame)

        # Create button frame
        self.setup_button_frame(main_frame)

    def setup_input_frame(self, parent: ttk.Frame) -> None:
        """
        Setup input fields frame.
        
        Args:
            parent (ttk.Frame): Parent frame.
        """
        input_frame = ttk.LabelFrame(parent, text="Детали заявки", padding="10")
        input_frame.pack(fill=tk.BOTH, padx=(0, 10), pady=(0, 10))

        # Create two columns for better layout
        left_column = ttk.Frame(input_frame)
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_column = ttk.Frame(input_frame)
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Left column fields
        # Client Name
        ttk.Label(left_column, text="Имя клиента *").pack(anchor=tk.W)
        self.client_name_var = tk.StringVar()
        ttk.Entry(left_column, textvariable=self.client_name_var, width=30).pack(
            anchor=tk.W, pady=(0, 10), fill=tk.X
        )

        # Contact Info
        ttk.Label(left_column, text="Контакт").pack(anchor=tk.W)
        self.contact_info_var = tk.StringVar()
        ttk.Entry(left_column, textvariable=self.contact_info_var, width=30).pack(
            anchor=tk.W, pady=(0, 10), fill=tk.X
        )

        # Project Type
        ttk.Label(left_column, text="Тип проекта *").pack(anchor=tk.W)
        self.project_type_var = tk.StringVar()
        project_types = config.PROJECT_TYPES
        project_combo = ttk.Combobox(
            left_column, 
            textvariable=self.project_type_var, 
            values=project_types, 
            width=28, 
            state="readonly"
        )
        project_combo.pack(anchor=tk.W, pady=(0, 10), fill=tk.X)

        # Right column fields
        # Status
        ttk.Label(right_column, text="Статус").pack(anchor=tk.W)
        self.status_var = tk.StringVar(value=config.STATUS_OPTIONS[0])
        status_combo = ttk.Combobox(
            right_column, 
            textvariable=self.status_var, 
            values=self.STATUS_OPTIONS, 
            width=28, 
            state="readonly"
        )
        status_combo.pack(anchor=tk.W, pady=(0, 10), fill=tk.X)

        # Deadline
        ttk.Label(right_column, text="Срок (ГГГГ-ММ-ДД)").pack(anchor=tk.W)
        self.deadline_var = tk.StringVar()
        ttk.Entry(right_column, textvariable=self.deadline_var, width=30).pack(
            anchor=tk.W, pady=(0, 10), fill=tk.X
        )

        # Description
        ttk.Label(parent, text="Описание").pack(anchor=tk.W, padx=10, pady=(10, 0))
        self.description_var = tk.StringVar()
        description_frame = ttk.Frame(parent)
        description_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=False)
        
        # Use scrolled text for better description handling
        self.description_text = scrolledtext.ScrolledText(
            description_frame,
            height=3,
            width=100,
            wrap=tk.WORD
        )
        self.description_text.pack(fill=tk.BOTH, expand=True)

    def setup_search_frame(self, parent: ttk.Frame) -> None:
        """
        Setup search and filter frame.
        
        Args:
            parent (ttk.Frame): Parent frame.
        """
        search_frame = ttk.Frame(parent)
        search_frame.pack(fill=tk.X, pady=(0, 10))

        # Search by client name
        ttk.Label(search_frame, text="Поиск клиента:").pack(side=tk.LEFT, padx=(0, 5))
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=25)
        search_entry.pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            search_frame, 
            text="Поиск", 
            command=self.search_requests
        ).pack(side=tk.LEFT, padx=(0, 20))

        # Filter by status
        ttk.Label(search_frame, text="Фильтр по статусу:").pack(side=tk.LEFT, padx=(0, 5))
        self.filter_var = tk.StringVar(value="All")
        filter_combo = ttk.Combobox(
            search_frame, 
            textvariable=self.filter_var, 
            values=["All"] + self.STATUS_OPTIONS, 
            width=15, 
            state="readonly"
        )
        filter_combo.pack(side=tk.LEFT, padx=(0, 5))
        filter_combo.bind("<<ComboboxSelected>>", lambda e: self.filter_requests())
        
        ttk.Button(
            search_frame, 
            text="Показать все", 
            command=self.load_requests
        ).pack(side=tk.LEFT, padx=(0, 5))

    def setup_table_frame(self, parent: ttk.Frame) -> None:
        """
        Setup table (Treeview) frame.
        
        Args:
            parent (ttk.Frame): Parent frame.
        """
        table_frame = ttk.LabelFrame(parent, text="Все заявки", padding="10")
        table_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Create Treeview
        columns = tuple(config.TABLE_COLUMNS.keys())
        self.tree = ttk.Treeview(table_frame, columns=columns, height=15, show="headings")

        # Define column headings and widths
        column_widths = config.TABLE_COLUMNS.copy()

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])

        # Add scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Pack table and scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Bind row selection
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def setup_button_frame(self, parent: ttk.Frame) -> None:
        """
        Setup button frame.
        
        Args:
            parent (ttk.Frame): Parent frame.
        """
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X)

        # Add button
        ttk.Button(
            button_frame, 
            text="Добавить заявку", 
            command=self.add_request
        ).pack(side=tk.LEFT, padx=5)

        # Update button
        ttk.Button(
            button_frame, 
            text="Обновить заявку", 
            command=self.update_request
        ).pack(side=tk.LEFT, padx=5)

        # Delete button
        ttk.Button(
            button_frame, 
            text="Удалить заявку", 
            command=self.delete_request
        ).pack(side=tk.LEFT, padx=5)

        # Change Status button
        ttk.Button(
            button_frame, 
            text="Изменить статус", 
            command=self.change_status
        ).pack(side=tk.LEFT, padx=5)

        # Clear button
        ttk.Button(
            button_frame, 
            text="Очистить поля", 
            command=self.clear_fields
        ).pack(side=tk.LEFT, padx=5)

        # Exit button
        ttk.Button(
            button_frame, 
            text="Выход", 
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)

    def load_requests(self) -> None:
        """Load all requests from database and display in table."""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Load requests from database
            requests = self.db.get_all_requests()

            # Insert requests into table
            for request in requests:
                request_id, client_name, contact_info, project_type, description, status, deadline, created_at = request
                self.tree.insert(
                    "",
                    tk.END,
                    values=(request_id, client_name, contact_info, project_type, status, deadline, created_at),
                    tags=(status,)  # Use status as tag for potential coloring
                )

            # Configure tag colors based on status
            for status, color in config.STATUS_COLORS.items():
                self.tree.tag_configure(status, background=color)

        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка загрузки заявок: {str(e)}")

    def on_row_select(self, event) -> None:
        """
        Handle row selection in table.
        
        Args:
            event: Selection event.
        """
        try:
            selection = self.tree.selection()
            if selection:
                item = selection[0]
                values = self.tree.item(item, "values")
                
                if values:
                    self.selected_request_id = int(values[0])
                    
                    # Get full request details from database
                    request = self.db.get_request_by_id(self.selected_request_id)
                    
                    if request:
                        request_id, client_name, contact_info, project_type, description, status, deadline, created_at = request
                        
                        # Populate fields
                        self.client_name_var.set(client_name)
                        self.contact_info_var.set(contact_info)
                        self.project_type_var.set(project_type)
                        self.status_var.set(status)
                        self.deadline_var.set(deadline)
                        self.description_text.delete(1.0, tk.END)
                        self.description_text.insert(1.0, description or "")
        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка при выборе строки: {str(e)}")

    def validate_required_fields(self) -> bool:
        """
        Validate that required fields are filled.
        
        Returns:
            bool: True if validation passes, False otherwise.
        """
        if not self.client_name_var.get().strip():
            messagebox.showwarning(config.MESSAGES["VALIDATION_ERROR"], "Имя клиента обязательно.")
            return False

        if not self.project_type_var.get().strip():
            messagebox.showwarning(config.MESSAGES["VALIDATION_ERROR"], "Тип проекта обязателен.")
            return False

        return True

    def validate_deadline_format(self, deadline: str) -> bool:
        """
        Validate deadline format (YYYY-MM-DD).
        
        Args:
            deadline (str): Deadline string to validate.
            
        Returns:
            bool: True if valid format or empty, False otherwise.
        """
        if not deadline:
            return True  # Deadline is optional

        try:
            datetime.datetime.strptime(deadline, "%Y-%m-%d")
            return True
        except ValueError:
            messagebox.showwarning(
                config.MESSAGES["VALIDATION_ERROR"], 
                config.MESSAGES["INVALID_DATE"]
            )
            return False

    def add_request(self) -> None:
        """Add a new request to the database."""
        try:
            if not self.validate_required_fields():
                return

            deadline = self.deadline_var.get().strip()
            if not self.validate_deadline_format(deadline):
                return

            client_name = self.client_name_var.get().strip()
            contact_info = self.contact_info_var.get().strip()
            project_type = self.project_type_var.get().strip()
            description = self.description_text.get(1.0, tk.END).strip()

            if self.db.add_request(client_name, contact_info, project_type, description, deadline):
                messagebox.showinfo(config.MESSAGES["SUCCESS"], config.MESSAGES["ADD_SUCCESS"])
                self.clear_fields()
                self.load_requests()
            else:
                messagebox.showerror(config.MESSAGES["ERROR"], "Ошибка добавления заявки.")
        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка добавления заявки: {str(e)}")

    def update_request(self) -> None:
        """Update the selected request."""
        try:
            if self.selected_request_id is None:
                messagebox.showwarning(config.MESSAGES["WARNING"], config.MESSAGES["SELECT_REQUEST"])
                return

            if not self.validate_required_fields():
                return

            deadline = self.deadline_var.get().strip()
            if not self.validate_deadline_format(deadline):
                return

            client_name = self.client_name_var.get().strip()
            contact_info = self.contact_info_var.get().strip()
            project_type = self.project_type_var.get().strip()
            status = self.status_var.get().strip()
            description = self.description_text.get(1.0, tk.END).strip()

            if self.db.update_request(
                self.selected_request_id, 
                client_name, 
                contact_info, 
                project_type, 
                description, 
                status, 
                deadline
            ):
                messagebox.showinfo(config.MESSAGES["SUCCESS"], config.MESSAGES["UPDATE_SUCCESS"])
                self.clear_fields()
                self.load_requests()
            else:
                messagebox.showerror(config.MESSAGES["ERROR"], "Ошибка обновления заявки.")
        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка обновления заявки: {str(e)}")

    def delete_request(self) -> None:
        """Delete the selected request."""
        try:
            if self.selected_request_id is None:
                messagebox.showwarning(config.MESSAGES["WARNING"], config.MESSAGES["SELECT_REQUEST"])
                return

            if messagebox.askyesno(
                config.MESSAGES["WARNING"], 
                config.MESSAGES["CONFIRM_DELETE"]
            ):
                if self.db.delete_request(self.selected_request_id):
                    messagebox.showinfo(config.MESSAGES["SUCCESS"], config.MESSAGES["DELETE_SUCCESS"])
                    self.clear_fields()
                    self.load_requests()
                else:
                    messagebox.showerror(config.MESSAGES["ERROR"], "Ошибка удаления заявки.")
        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка удаления заявки: {str(e)}")

    def search_requests(self) -> None:
        """Search requests by client name."""
        try:
            search_term = self.search_var.get().strip()
            # if search field is empty we simply reload the full list
            # this allows the user to clear the search and hit the button again
            # rather than forcing them to click "Show All" separately.
            if not search_term:
                self.load_requests()
                return

            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Search requests
            requests = self.db.search_by_client_name(search_term)

            if not requests:
                # nothing matched; notify and show all so user isn't left with
                # an empty table
                messagebox.showinfo(config.MESSAGES["INFO"], config.MESSAGES["NO_RESULTS"])
                self.load_requests()
                return

            # Insert requests into table
            for request in requests:
                request_id, client_name, contact_info, project_type, description, status, deadline, created_at = request
                self.tree.insert(
                    "",
                    tk.END,
                    values=(request_id, client_name, contact_info, project_type, status, deadline, created_at),
                    tags=(status,)
                )

        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка поиска заявок: {str(e)}")

    def filter_requests(self) -> None:
        """Filter requests by status."""
        try:
            selected_status = self.filter_var.get()

            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            if selected_status == "All":
                requests = self.db.get_all_requests()
            else:
                requests = self.db.filter_by_status(selected_status)

            # Insert requests into table
            for request in requests:
                request_id, client_name, contact_info, project_type, description, status, deadline, created_at = request
                self.tree.insert(
                    "",
                    tk.END,
                    values=(request_id, client_name, contact_info, project_type, status, deadline, created_at),
                    tags=(status,)
                )

        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка фильтрации заявок: {str(e)}")

    def change_status(self) -> None:
        """Change the status of the selected request."""
        try:
            if self.selected_request_id is None:
                messagebox.showwarning(config.MESSAGES["WARNING"], config.MESSAGES["SELECT_REQUEST"])
                return

            new_status = self.status_var.get().strip()
            
            if self.db.update_status(self.selected_request_id, new_status):
                messagebox.showinfo(config.MESSAGES["SUCCESS"], f"Статус изменён на '{new_status}' успешно!")
                self.load_requests()
            else:
                messagebox.showerror(config.MESSAGES["ERROR"], "Ошибка изменения статуса.")
        except Exception as e:
            messagebox.showerror(config.MESSAGES["ERROR"], f"Ошибка изменения статуса: {str(e)}")

    def clear_fields(self) -> None:
        """Clear all input fields."""
        self.client_name_var.set("")
        self.contact_info_var.set("")
        self.project_type_var.set("")
        self.status_var.set("New")
        self.deadline_var.set("")
        self.description_text.delete(1.0, tk.END)
        self.search_var.set("")
        self.selected_request_id = None


def main():
    """Main entry point of the application."""
    root = tk.Tk()
    app = DesignRequestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
