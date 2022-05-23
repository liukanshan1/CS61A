CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT adog.name AS name, asize.size AS size
  FROM dogs AS adog, sizes AS asize
  WHERE adog.height > asize.min AND adog.height <= asize.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT dog.name AS name
  FROM dogs AS dog, parents AS parent, dogs AS dogsize
  WHERE dog.name = parent.child AND parent.parent = dogsize.name
  ORDER BY dogsize.height desc;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT firstdog.child AS name1, seconddog.child AS name2
  FROM parents AS firstdog, parents AS seconddog
  WHERE firstdog.parent = seconddog.parent AND firstdog.child < seconddog.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT ("The two siblings, " || sib.name1 || " plus " || sib.name2 || " have the same size: " || dogsize1.size) as sentence
  FROM siblings AS sib, size_of_dogs AS dogsize1, size_of_dogs AS dogsize2
  WHERE sib.name1 = dogsize1.name AND sib.name2 = dogsize2.name AND dogsize1.size = dogsize2.size;

