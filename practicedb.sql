create database employee;
use employee;
create table emp(emp_id int(10) , emp_name varchar(20), emp_salary int(10));
insert into emp(emp_id , emp_name, emp_salary)
values
       (1, "pratik", 1000000),
       (2, "rohan", 2000000),
       (3, "harish", 3000000);
select * from emp;       

select emp_id, emp_name
from emp
where emp_id > 1 AND emp_name = "harish";



alter table emp
add primary key(emp_id) ;

update emp
set emp_salary = 4000000
where emp_id = 1;

select * from emp;

desc emp;

delete from emp
where emp_id = 1;

select * from emp;

alter table emp
add column dept_id int ;

select * from emp;

create table 
department(dept_id int(10) primary key , dept_name varchar(20));

insert department(dept_id, dept_name)
values (1, 'IT'), 
       (2, 'HR'), 
       (3, 'Finance');
       
       
select emp.emp_id, department.dept_id
from emp   
inner join department
on emp.dept_id = department.dept_id;    
       
UPDATE emp
SET dept_id = 1
WHERE emp_id = 1;

UPDATE emp
SET dept_id = 2
WHERE emp_id = 2;

UPDATE emp
SET dept_id = 1
WHERE emp_id = 3;
       
select emp.emp_id, department.dept_id
from emp   
inner join department
on emp.dept_id = department.dept_id;    


select e.emp_name, d.dept_name
from emp e
left join department d
on e.dept_id = d.dept_id;

select e.emp_name, d.dept_name
from emp e
right join department d
on e.dept_id = d.dept_id;
       

select e.emp_name , d.dept_name
from emp e
left join department d
on e.dept_id = d.dept_id
union 
select e.emp_name, d.dept_name
from emp e
right join department d
on e.dept_id = d.dept_id;
