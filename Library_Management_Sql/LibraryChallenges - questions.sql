/******************* In the Library *********************/

/*******************************************************/
/* find the number of availalbe copies of the book (Dracula)      */
/*******************************************************/

/* check total copies of the book */
SELECT COUNT(*) as total_copies FROM books
 WHERE title = 'Dracula';
/* current total loans of the book */
SELECT COUNT(*) as total_current_loans FROM books AS b 
INNER JOIN loans AS l ON b.bookid = l.bookid
WHERE b.title = 'Dracula' AND l.returneddate IS NULL;

/* total available books of dracula */
SELECT 
    (SELECT COUNT(*) FROM books WHERE title = 'Dracula') - 
    (SELECT COUNT(*) 
     FROM books AS b 
     INNER JOIN loans AS l ON b.bookid = l.bookid
     WHERE b.title = 'Dracula' AND l.returneddate IS NULL) 
    AS available_copies_of_book;

/*******************************************************/
/* Add new books to the library                        */
/*******************************************************/
select * from books
order by bookid desc;

insert into books values(
201, "It’s Only the Himalayas" ,'MariaAbroad',1990,9586004121
);

select * from books
order by bookid desc;

/*******************************************************/
/* Check out Books: books(4043822646, 2855934983) whose patron_email(jvaan@wisdompets.com), loandate=2020-08-25, duedate=2020-09-08, loanid=by_your_choice*/
/*******************************************************/
select * from patrons
where email = 'jvaan@wisdompets.com';

select * from books 
where  barcode = '2855934983';
# fisrt book id 93 , second 11 

select * from loans
order by loanid desc;

insert into loans 
values (2001, 93, 50, '2020-08-25', '2020-09-08', null 
);
insert into loans 
values (2002, 11, 50, '2020-08-25', '2020-09-08', null 
);
/********************************************************/
/* Check books for Due back                             */
/* generate a report of books due back on July 13, 2020 */
/* with patron contact information                      */
/********************************************************/
select * from patrons as p 
inner join loans as l on l.PatronID = p.PatronID 
where duedate = '2020-07-13';
/*******************************************************/
/* Return books to the library (which have barcode=6435968624) and return this book at this date(2020-07-05)                    */
/*******************************************************/
UPDATE loans as l
inner JOIN books as b ON l.bookid = b.bookid
SET l.returneddate = '2020-07-05'
WHERE b.barcode = '6435968624'
AND l.returneddate IS NULL; 

select * from loans
where returneddate = '2020-07-05';

select * from books
where bookid = 105;

/*******************************************************/
/* Encourage Patrons to check out books                */
/* generate a report of showing 10 patrons who have
checked out the fewest books.                          */
/*******************************************************/
select p.PatronID, p.FirstName, p.LastName,count(*) as num_of_checkout from patrons as p
inner join loans as l on l.PatronID = p.PatronID
group by p.PatronID,p.FirstName,p.LastName
order by  num_of_checkout asc 
limit 10;


/*******************************************************/
/* Find books to feature for an event                  
 create a list of books from 1890s that are
 currently available                                    */
/*******************************************************/
select * from books as b 
inner join loans as l on l.BookID = b.bookid
where l.ReturnedDate is not null and b.Published >1890 and b.Published < 1900 ;

/*******************************************************/
/* Book Statistics 
/* create a report to show how many books were 
published each year.                                    */
/*******************************************************/
SELECT Published, COUNT(DISTINCT(Title)) AS TotalNumberOfPublishedBooks FROM Books
GROUP BY Published
ORDER BY TotalNumberOfPublishedBooks DESC;


/*************************************************************/
/* Book Statistics                                           */
/* create a report to show 5 most popular Books to check out */
/*************************************************************/
SELECT b.Title, b.Author, b.Published, COUNT(b.Title) AS TotalTimesOfLoans FROM Books b
JOIN Loans l ON b.BookID = l.BookID
GROUP BY b.Title, b.Author, b.Published
ORDER BY 4 DESC
LIMIT 5;
