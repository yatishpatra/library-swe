# Traceability Matrix
Traceability ensures that each user story is linked to its implementation, unit tests, and release version.
| User Story | Sprint | Code Component | Test Case | Git Tag |
|-----------|--------|----------------|-----------|---------|
| Add a book | Sprint 1 | add_book() | test_add_book_success | v0.1 |
| Prevent duplicate book | Sprint 1 | add_book() | test_add_duplicate_book | v0.1 |
| Borrow a book | Sprint 2 | borrow_book() | test_borrow_book | v0.2 |
| Prevent borrowing unavailable book | Sprint 2 | borrow_book() | test_borrow_unavailable_book | v0.2 |
| Return a book | Sprint 2 | return_book() | test_return_book | v0.2 |
| Generate library report | Sprint 3 | generate_report() | test_report_contains_header | v0.3 |
| Report contains book entries | Sprint 3 | generate_report() | test_report_contains_book | v0.3 |