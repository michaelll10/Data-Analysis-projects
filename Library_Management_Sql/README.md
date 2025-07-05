# 📚 Library Management SQL Project

This project demonstrates core SQL operations for managing a library system, including checking out books, returning them, analyzing inventory, and generating reports.

## 🛠 What This Project Covers

### 🔍 Inventory & Availability
- Count total and available copies of a specific book (e.g., *Dracula*)
- Add new books to the library

### 📘 Book Checkout & Returns
- Check out books to a patron by barcode and loan date
- Return a book by updating the `returneddate`

### 📅 Reports & Analytics
- Show books due on a specific date (with patron contact)
- List books from the 1890s that are currently available
- Show how many books were published per year
- Identify the 5 most popular books by total checkouts
- List 10 patrons who have checked out the fewest books

## 🧪 Sample Features Demonstrated

- `JOIN`, `INNER JOIN`, and multi-table queries
- `GROUP BY`, `COUNT`, `ORDER BY`, and `LIMIT`
- Subqueries for real-time availability
- Date filtering (`duedate`, `returneddate`)
- Manual data entry (`INSERT INTO`) for testing

## 📁 Sample Tables Used

- `books` — Book catalog with title, author, published year, barcode
- `loans` — Book loan history with loan/return dates
- `patrons` — Library members with contact info

## 💡 Sample Use Case: Dracula Availability

```sql
-- How many copies of Dracula are available?
SELECT 
    (SELECT COUNT(*) FROM books WHERE title = 'Dracula') - 
    (SELECT COUNT(*) 
     FROM books b 
     JOIN loans l ON b.bookid = l.bookid
     WHERE b.title = 'Dracula' AND l.returneddate IS NULL) 
    AS available_copies;
