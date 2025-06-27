DROP TABLE IF EXISTS recipe;
CREATE TABLE recipe (
    id int PRIMARY KEY,
    title text,
    instructions text,
    ingredients text
);