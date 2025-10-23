DROP TABLE IF EXISTS news;

CREATE TABLE news (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  url TEXT NOT NULL
  /*
  We'll figure this out later:

  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
  
  */
);