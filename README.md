Library Management API

Building a Django Rest Framework API for a library management system. The API will cover the following features:

1. Book Model:
Model for a book with the following fields:
    Title
    Author
    Publication Date
    ISBN (International Standard Book Number)
    Genre
    Number of Pages


3. API Endpoints:
  API endpoints for the following operations:
    List all books
    Retrieve a single book by its ID
    Create a new book
    Update an existing book
    Delete a book


5. Serializers:
  Serializers for the Book model to convert data to and from JSON.

6. Authentication:
  Token-based authentication for the API.

8. Permissions:
  Custom permissions to allow only authenticated users to create, update, or delete books.

9. Pagination:
  Pagination for the list of all books API endpoint.

7.Filtering:
  Filtering capabilities to the list of all books API endpoint based on:
    Title
    Author
    Genre
    Publication Date


8. Testing:
  Unit tests for your views and serializers to ensure that the API behaves as expected.

9. Documentation:
  Django Rest Framework's built-in tools to generate API documentation. Ensure that the documentation is clear and includes examples.

10. Versioning:
  Versioning for the API to handle changes in the future.

11. Rate Limiting:
  Rate limiting for the API to prevent abuse.

12. Dockerization:
  Dockerizing application for easy deployment.
