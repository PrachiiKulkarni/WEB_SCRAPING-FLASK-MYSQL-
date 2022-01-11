use flask;

drop table if exists internshala3;
create table internshala3 (
    id INT NOT NULL auto_increment,
    Internship_title VARCHAR(300) NOT NULL,
    Company VARCHAR(200) NOT NULL,
    Location VARCHAR(200) NOT NULL,
    Location_1 varchar(500) NOT NULL,
    Duration_in_months INT NOT NULL,
    Stipend_per_month VARCHAR(200) NOT NULL,
    Skills_required varchar(5000) NOT NULL,
    Skills_required_1 varchar(500) NOT NULL,
    PRIMARY KEY (id)
);
show tables;
describe internshala3;
set sql_safe_updates=0;
SELECT @@secure_file_priv;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/internshala_df1NF_final.csv' 
INTO TABLE internshala3
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from internshala3;
