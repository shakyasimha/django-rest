-- Inserting book information
insert into mysite_books(book_name, author_name_id, isbn, pub_year, pub_name_id)
values
('The Communist Manifesto', (select id from));