--building a docker container for postgres with exposed(!) port 5432
-- docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:alpine
 
 drop schema if exists school cascade;

 create schema school;
 set schema 'school';
 

CREATE TYPE class_enum AS ENUM ('ט','י','יא','יב');
CREATE TYPE sub_class_enum AS ENUM ('1','2','3','4','5','6','7');

 create table classes (
    id uuid DEFAULT gen_random_uuid(),
    class class_enum, -- 9\10\11\12
    sub_class sub_class_enum,
    educator_name text, 
    PRIMARY KEY(id),
    unique(class, sub_class,educator_name)
);

CREATE TYPE unit_enum as ENUM ('3','4','5');

create table unit_groups(
    id uuid DEFAULT gen_random_uuid(),
    teacher_name text,
    unit unit_enum,
    unit_group text,
    room text,
    PRIMARY KEY(id)
);


create table students (
    id INT,
    lname text,
    fname text,
    class_id uuid,
    unit_group_id uuid,
    module_1 text,
    module_2 text,
    literature text,
    oral text,
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP DEFAULT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_class_id
    FOREIGN KEY(class_id) 
        REFERENCES classes(id),
    CONSTRAINT fk_unit_group_id
    FOREIGN KEY(unit_group_id) 
        REFERENCES unit_groups(id)
);





-- <<<<INSERTS

insert into classes (
    class,
    sub_class,
    educator_name
) values (
    'ט',
    '1',
    'אריאל בצלאל'
),
(
    'ט',
    '2',
    'לוסטיג זכריה'
),
(
    'ט',
    '3',
    'פלהיימר שלומי'
),
(
    'י',
    '1',
    'גואטה נועם'
);


-- ט1
-- 55e733e8-c1cb-4213-a878-63ef4abfe213
-- ט2
-- 82fddd15-d8e6-4ccf-bd21-b3881a285547
-- ט3
-- b2bc7388-be22-4331-a3e7-0c20a274e5f8
-- י1
-- 5db51073-503c-4008-8726-450f52ac0169


  
insert into unit_groups(
teacher_name,
unit,
unit_group
-- room,
 
) VALUES (
    'הראל',
    '3',
    'א'
    -- (select class from classes where class=9 limit 1),
    -- (select id from teachers where fname='Tamir')
),
(
    'שי',
    '3',
    'ב'
);

INSERT INTO students (
    id ,
    lname,
    fname,
    class_id,
    unit_group_id
) VALUES (
    308358209,
    'Kelman',
    'shai',
    (select id from classes where id='55e733e8-c1cb-4213-a878-63ef4abfe213'),
    (select id from unit_groups where id = '343a9c82-d425-4f18-8086-073a38cefa6b')
),
(
    312560626,
    'Kelman',
    'Cherut',
    (select id from classes where id='55e733e8-c1cb-4213-a878-63ef4abfe213'),
    (select id from unit_groups where id = '343a9c82-d425-4f18-8086-073a38cefa6b')
),
( 
    1232123,
    'תלמיד כיתה',
    'י',
    (select id from classes where id='5db51073-503c-4008-8726-450f52ac0169'),
    (select id from unit_groups where id = '7b86a654-61f6-4703-90f0-4ba0bbab4c13')
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


-- update  students set class_id = 'f84ba710-40e3-4273-b77e-63660ee541f5';

-- join creates a temporary veiw that I can later use in my app.
-- Exporting data from the database to the app.
-- If the output of the query is too big it is optional to write the
-- data onto a file so the RAM would not be overload. 
-- The second option is simplt limit the result. 
-- for REST API use page_size() 


-- select lname,fname, classes.class from students left join classes on class_id = classes.id;