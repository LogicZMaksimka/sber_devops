create database cacti;

-- create schema cacti;

create table if not exists cacti_table (
   family text,
   subtype text,
   spines_length integer
);

insert into cacti_table values ('rebutia', 'senilis', 3);
insert into cacti_table values ('rebutia', 'albiflora', 3);
insert into cacti_table values ('rebutia', 'miniscula', 1);
insert into cacti_table values ('echinopsis', 'amblayensis', 3);
insert into cacti_table values ('echinopsis', 'albispinosa', 4);
insert into cacti_table values ('mammillaria', 'bocasana', 4);


select * from cacti_table;