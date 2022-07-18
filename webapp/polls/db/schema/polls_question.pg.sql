--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" bigserial NOT NULL PRIMARY KEY, 
    "question_text" varchar(200) NOT NULL, 
    "pub_date" timestamp with time zone NOT NULL);
