USE sample_database;


SET SESSION FOREIGN_KEY_CHECKS=0;


/* ============================== */
/* drop tables */
/* ============================== */
DROP TABLE IF EXISTS SCHOOL;
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS REPORT_CARD;
DROP TABLE IF EXISTS SUBJECT;
DROP TABLE IF EXISTS EVALUATION;


/* ============================== */
/* create tables */
/* ============================== */
CREATE TABLE ROLE
(
  role_id varchar(36) NOT NULL,
  role_name varchar(36) NOT NULL,
  PRIMARY KEY (role_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE USER_ROLE
(
  user_id varchar(36) NOT NULL,
  role_id varchar(36) NOT NULL,
  PRIMARY KEY (user_id, role_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE SCHOOL
(
  school_id varchar(36) NOT NULL,
  school_name varchar(36) NOT NULL,
  PRIMARY KEY (school_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE USER
(
  user_id varchar(36) NOT NULL,
  user_name varchar(36) NOT NULL,
  email varchar(128) NOT NULL,
  school_id varchar(36) NOT NULL,
  teacher_id varchar(36),
  PRIMARY KEY (user_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE REPORT_CARD
(
  report_card_id varchar(36) NOT NULL,
  user_id varchar(36) NOT NULL,
  first_evaluator_id varchar(36) NOT NULL,
  second_evaluator_id varchar(36) NOT NULL,
  content text NOT NULL,
  PRIMARY KEY (report_card_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE SUBJECT
(
  subject_id varchar(36) NOT NULL,
  report_card_id varchar(36) NOT NULL,
  content text NOT NULL,
  PRIMARY KEY (subject_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


CREATE TABLE EVALUATION
(
  subject_id varchar(36) NOT NULL,
  evaluated_by_id varchar(36) NOT NULL,
  evaluation varchar(36) NOT NULL,
  PRIMARY KEY (subject_id, evaluated_by_id)
) ENGINE = InnoDB DEFAULT CHARACTER SET utf8mb4;


/* ============================== */
/* create foreign keys */
/* ============================== */
ALTER TABLE USER_ROLE
  ADD FOREIGN KEY (user_id)
  REFERENCES USER (user_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE USER_ROLE
  ADD FOREIGN KEY (role_id)
  REFERENCES ROLE (role_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE USER
  ADD FOREIGN KEY (school_id)
  REFERENCES SCHOOL (school_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE REPORT_CARD
  ADD FOREIGN KEY (user_id)
  REFERENCES USER (user_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE REPORT_CARD
  ADD FOREIGN KEY (first_evaluator_id)
  REFERENCES USER (user_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE REPORT_CARD
  ADD FOREIGN KEY (second_evaluator_id)
  REFERENCES USER (user_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE SUBJECT
  ADD FOREIGN KEY (report_card_id)
  REFERENCES REPORT_CARD (report_card_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE EVALUATION
  ADD FOREIGN KEY (subject_id)
  REFERENCES SUBJECT (subject_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;


ALTER TABLE EVALUATION
  ADD FOREIGN KEY (evaluated_by_id)
  REFERENCES USER (user_id)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT
;
