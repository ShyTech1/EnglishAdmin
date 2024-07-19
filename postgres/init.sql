--building a docker container for postgres with exposed(!) port 5432
-- docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:alpine
 
 drop schema if exists school cascade;

 create schema school;
 set schema 'school';
 
 create table classes (
    id uuid DEFAULT gen_random_uuid(),
    class INT, -- 9\10\11\12
    sub_class int,  -- 1\2\3\4\5\6\7 
    educator_name CHAR(255), 
    PRIMARY KEY(id)
);
create table teachers(
    id  INT,
    lname CHAR(255) ,
    fname CHAR(255),
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP DEFAULT NULL,
    PRIMARY KEY (id)
);
create table unit_groups (
    id char(255),
    unit int, -- 3|4|5
    unit_group char(255), -- |a|b|c|d|e,
    class INT,
    teacher_id INT,
    PRIMARY key (id),
    CONSTRAINT fk_unit_group_teacher_id
      FOREIGN KEY(teacher_id) 
        REFERENCES teachers(id),
    CONSTRAINT check_class  CHECK (class>=9 AND class<=12)
);
create table students (
    id INT,
    lname CHAR(255),
    fname CHAR(255),
    teacher_id INT,
    class_id uuid ,
    unit_group_id char(255), 
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP DEFAULT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_teacher_id
      FOREIGN KEY(teacher_id) 
        REFERENCES teachers(id),
    CONSTRAINT fk_students_class_id
      FOREIGN KEY(class_id) 
        REFERENCES classes(id),
    CONSTRAINT fk_unit_group_id
      FOREIGN KEY(unit_group_id) 
        REFERENCES unit_groups(id)
);
create table exams (
    id uuid DEFAULT gen_random_uuid(), 
    student_id INT, 
    season CHAR(255) , --winter|summer|summer_b
    year int,
    module CHAR(255), --A,B,C,D,E,F,G,O3,O4,O5,O07
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP DEFAULT NULL,
    PRIMARY KEY(year,season,module),
    unique (id),
     CONSTRAINT fk_exams_student_id
      FOREIGN KEY(student_id) 
        REFERENCES students(id)
);
create table scores (
    student_id INT,
    exam_id uuid,
    score INT,
    teacher_id INT, 
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP DEFAULT NULL,
     CONSTRAINT fk_scores_student_id
      FOREIGN KEY(student_id) 
        REFERENCES students(id),
    CONSTRAINT fk_exam_id
      FOREIGN KEY(exam_id) 
        REFERENCES exams(id),
    CONSTRAINT fk_score_teacher_id
      FOREIGN KEY(teacher_id) 
        REFERENCES teachers(id)
);


-- <<<<INSERTS

insert into classes (
    class,
    sub_class,
    educator_name
) values (
    9,
    1,
    'harav mazliach'
),
(
    9,
    2,
    'harav moshe'
);
    insert into teachers (
        id,
        lname,
        fname
    ) values (
        301220422,
        'Admon',
        'Tamir'
    );
insert into unit_groups(
id,
unit,
unit_group,
class,
teacher_id 
) VALUES (
    '3-a',
    3,
    'a',
    (select class from classes where class=9 limit 1),
    (select id from teachers where fname='Tamir')
);

INSERT INTO students (
    id ,
    lname,
    fname,
    teacher_id,
    unit_group_id
) VALUES (
    308358209,
    'Kelman',
    'shai',
    (select id from teachers where fname='Tamir'),
    '3-a'
);

insert into exams (
    student_id,
    season,
    year,
    module
) values   (
    (select id from students limit 1),
    'winter',
    '2024',
    'A'
);
insert into scores (
    student_id,
    exam_id,
    teacher_id,
    score
) values (
    (select id from students limit 1),
    (select id from exams limit 1),
    (select id from teachers limit 1),
    80
);