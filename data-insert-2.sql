-- Inserting book information
insert into mysite_books(book_name, isbn, pub_year, pub_name_id)
values
('The 48 Laws of Power', '9780670881468', 1998, (select id from mysite_publisher where pub_name='Viking Press')),
('The Art of Seduction', '9780142001196', 2001, (select id from mysite_publisher where pub_name='Penguin Books')),
('The 33 Strategies of War', '9780670033921', 2006, (select id from mysite_publisher where pub_name='Viking Press')),
('Mastery', '9780143123756', 2012, (select id from mysite_publisher where pub_name='Penguin Books')),
('The Laws of Human Nature', '9780143129018', 2018, (select id from mysite_publisher where pub_name='Penguin Books'));

-- inserting book and author information
insert into mysite_author_books(author_id, books_id)
values(1, 1),(1,2),(1,3),(1,4),(1,5);