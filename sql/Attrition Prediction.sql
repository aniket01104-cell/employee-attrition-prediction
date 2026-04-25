-- =====================================================
-- PROJECT: Employee Attrition Analysis
-- DESCRIPTION: SQL analysis to identify key factors 
-- influencing employee attrition.
-- =====================================================

#Creating Database.
create database attrition_db;
use attrition_db;

#Checking if the data is proprly imported
select * from employee_attrition;

#Questions
#Q. What percentage of employees are leaving the company?
select round(sum(case when Attrition="Yes"
then 1 else 0 end)*100.0/count(*),2)
as attrition_rate
from employee_attrition;
-- Insight: The overall attrition rate is approximately 16%, indicating a moderate level of employee turnover.


#Q. Which department has the highest employee turnover?
select Department,count(*) total
,sum(case when Attrition="Yes" then 1
else 0 end) attrition
from employee_attrition
group by Department
order by attrition desc;
-- Insight: Research & Development and Sales departments have the highest attrition, suggesting potential workload or management issues.


#Q. Which job roles are most likely to leave?
select JobRole,count(*) total,
sum(case when Attrition="Yes" then 1
else 0 end) attrition
from employee_attrition
group by JobRole
order by attrition desc;
-- Insight: Roles such as Laboratory Technician and Sales Executive show the highest attrition, indicating higher stress or lower satisfaction in these roles.


#Q. Do employees who leave earn less than those who stay?
select Attrition,avg(MonthlyIncome) avg_salary
from employee_attrition
group by Attrition;
-- Insight: Employees who left earn significantly less than those who stayed, highlighting salary as a major factor in attrition.


#Q. Does overtime increase the likelihood of employees leaving?
select OverTime,count(*) total,
sum(case when Attrition="yes" then 1
else 0 end) attrition
from employee_attrition
group by OverTime;
-- Insight: Employees working overtime have a higher attrition count, indicating workload pressure contributes to employee turnover.


#Q. Are new employees more likely to leave than experienced ones?
select YearsAtCompany,
count(*) total,
sum(case when Attrition="yes" then 1
else 0 end) attrition
from employee_attrition
group by YearsAtCompany
order by YearsAtCompany;
-- Insight: Employees in their early years (0–2 years) show higher attrition, emphasizing the importance of onboarding and early engagement.


#Q. Does job satisfaction affect whether employees leave?
select JobSatisfaction,count(*) total,
sum(case when Attrition="yes" then 1
else 0 end) attrition
from employee_attrition
group by JobSatisfaction
order by JobSatisfaction;
-- Insight: Lower job satisfaction levels are strongly associated with higher attrition rates.


#Q. Which combination of factors defines the highest-risk employees?
select Department,JobRole,OverTime,
count(*) total,
sum(case when Attrition="yes" then 1
else 0 end) attrition
from employee_attrition
group by Department,JobRole,OverTime
order by attrition desc
limit 5;
-- Insight: Employees in Research & Development and Sales roles with overtime form the highest-risk attrition group.