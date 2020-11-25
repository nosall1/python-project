DROP TABLE if EXISTS comments;
create table comments(
  id integer PRIMARY key autoincrement,
  comment text not NULL,
  user text not null,
  time text not null
);

DROP TABLE if EXISTS users;
create table users(
  id INTEGER PRIMARY key autoincrement,
  name text not null,
  password text not null
)