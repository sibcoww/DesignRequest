"""
Example usage and testing of the DesignRequest application components.
This file demonstrates how to use the database module independently.
"""

from database import DatabaseManager
from datetime import datetime, timedelta


def example_usage():
    """
    Demonstrate basic usage of the DatabaseManager.
    """
    
    # Initialize database manager
    db = DatabaseManager("design_requests.db")
    
    print("=" * 60)
    print("Пример использования DesignRequest")
    print("=" * 60)
    
    # Example 1: Add some sample requests
    print("\n1. Добавление примеров заявок...")
    requests_data = [
        {
            "client_name": "ООО "Акме",
            "contact_info": "john@acme.com, +1-555-0001",
            "project_type": "Дизайн логотипа",
            "description": "Разработка современного логотипа для нашей техкомпании",
            "deadline": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        },
        {
            "client_name": "TechStart Inc",
            "contact_info": "contact@techstart.io",
            "project_type": "Веб-дизайн",
            "description": "Полный редизайн сайта с адаптивной версткой",
            "deadline": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        },
        {
            "client_name": "Креативное агентство",
            "contact_info": "hello@creative.com, +1-555-0002",
            "project_type": "UI/UX дизайн",
            "description": "Дизайн интерфейса мобильного приложения, 15 экранов",
            "deadline": (datetime.now() + timedelta(days=21)).strftime("%Y-%m-%d")
        },
        {
            "client_name": "Global Solutions",
            "contact_info": "info@global.solutions.com",
            "project_type": "Мобильное приложение",
            "description": "Дизайн для iOS и Android приложения",
            "deadline": (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d")
        }
    ]
    
    for req in requests_data:
        success = db.add_request(
            req["client_name"],
            req["contact_info"],
            req["project_type"],
            req["description"],
            req["deadline"]
        )
        if success:
            print(f"✓ Added: {req['client_name']} - {req['project_type']}")
    
    # Example 2: Get all requests
    print("\n2. Получение всех заявок...")
    all_requests = db.get_all_requests()
    print(f"Total requests: {len(all_requests)}")
    for req in all_requests:
        print(f"  - {req[1]} ({req[3]}) - Status: {req[5]}")
    
    # Example 3: Search by client name
    print("\n3. Поиск заявок по имени клиента...")
    search_results = db.search_by_client_name("Tech")
    print(f"Найдено {len(search_results)} заявок, соответствующих 'Tech':")
    for req in search_results:
        print(f"  - {req[1]} ({req[3]})")
    
    # Example 4: Filter by status
    print("\n4. Фильтрация заявок по статусу...")
    for status in ["Новая", "В работе", "На проверке", "Завершена"]:
        filtered = db.filter_by_status(status)
        print(f"  {status}: {len(filtered)} заявок")
    
    # Example 5: Update a request
    if all_requests:
        print("\n5. Обновление первой заявки...")
        first_request = all_requests[0]
        request_id = first_request[0]
        
        success = db.update_status(request_id, "В работе")
        if success:
            print(f"✓ Статус заявки {request_id} изменён на 'В работе'")
    
    # Example 6: Get status statistics
    print("\n6. Статистика заявок по статусам...")
    stats = db.get_status_counts()
    for status, count in stats.items():
        print(f"  {status}: {count}")
    
    # Example 7: Update request details
    if all_requests:
        print("\n7. Обновление данных заявки...")
        first_request = all_requests[0]
        request_id = first_request[0]
        
        success = db.update_request(
            request_id,
            "Updated " + first_request[1],
            "updated@email.com",
            first_request[3],
            "Updated description text",
            "На проверке",
            (datetime.now() + timedelta(days=20)).strftime("%Y-%m-%d")
        )
        if success:
            print(f"✓ Updated request {request_id} details")
    
    # Example 8: Retrieve specific request
    if all_requests:
        print("\n8. Получение конкретной заявки...")
        first_request = all_requests[0]
        request_id = first_request[0]
        
        specific = db.get_request_by_id(request_id)
        if specific:
            print(f"Request ID: {specific[0]}")
            print(f"  Client: {specific[1]}")
            print(f"  Contact: {specific[2]}")
            print(f"  Type: {specific[3]}")
            print(f"  Description: {specific[4]}")
            print(f"  Status: {specific[5]}")
            print(f"  Deadline: {specific[6]}")
            print(f"  Created: {specific[7]}")
    
    # Example 9: Delete a request (commented out to preserve data)
    # if len(all_requests) > 3:
    #     print("\n9. Deleting a request...")
    #     request_to_delete = all_requests[-1]
    #     success = db.delete_request(request_to_delete[0])
    #     if success:
    #         print(f"✓ Deleted request {request_to_delete[0]}")
    
    print("\n" + "=" * 60)
    print("Примеры успешно выполнены!")
    print("=" * 60)


def test_validation():
    """
    Test data validation.
    """
    print("\n" + "=" * 60)
    print("Testing Data Validation")
    print("=" * 60)
    
    db = DatabaseManager("design_requests.db")
    
    print("\n1. Тест с пустым именем клиента (ожидается неудача)...")
    result = db.add_request("", "contact@email.com", "Logo Design", "Description", "2026-03-01")
    print(f"Result: {result}")
    
    print("\n2. Тест с пустым типом проекта (ожидается неудача)...")
    result = db.add_request("Client Name", "contact@email.com", "", "Description", "2026-03-01")
    print(f"Result: {result}")
    
    print("\n3. Тест с корректными данными (ожидается успех)...")
    result = db.add_request(
        "Test Client",
        "test@email.com",
        "Web Design",
        "Test description",
        "2026-03-01"
    )
    print(f"Result: {result}")
    
    print("\nТесты валидации завершены!")
    print("=" * 60)


if __name__ == "__main__":
    # Run examples
    example_usage()
    
    # Test validation
    test_validation()
