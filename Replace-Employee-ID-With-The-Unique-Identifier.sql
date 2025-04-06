# Write your MySQL query statement below
select y.unique_id, x.name from Employees x left join EmployeeUNI y on y.id = x.id