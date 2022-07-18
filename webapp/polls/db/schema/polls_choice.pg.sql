--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" bigserial NOT NULL PRIMARY KEY, "choice_text" varchar(200) NOT NULL, 
    "votes" integer NOT NULL, 
    "question_id" bigint NOT NULL);

ALTER TABLE "polls_choice" 
    ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id" 
        FOREIGN KEY ("question_id") 
        REFERENCES "polls_question" ("id") 
        DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
