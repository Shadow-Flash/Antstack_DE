1. For user count create a tabe with dates. (replace nth day with a particular date).
   
   Answer: 
~~~~sql
create table user_count_modify as 
select ('2021-01-01'::timestamp + ("Nth day" || ' days')::interval) as nth_day, "Users" from public.user_count
~~~~



2.  New table showing total users, new users, old users and engagement time on website.
Answer:
~~~~sql
-- nth day as bigint
select aet."Nth day", uc."Users", ns."New users", (uc."Users"+ns."New users") as total_users from public.average_engagement_time aet
inner join public.new_users ns
on aet."Nth day" = ns."Nth day"
inner join public.user_count uc
on aet."Nth day" = uc."Nth day"

-- converting nth day as date
select ('2021-01-01'::date + (aet."Nth day" || ' days')::interval)::date as nth_day, 
uc."Users", ns."New users", (uc."Users"+ns."New users") as total_users from public.average_engagement_time aet
inner join public.new_users ns
on aet."Nth day" = ns."Nth day"
inner join public.user_count uc
on aet."Nth day" = uc."Nth day"
~~~~

3. Show new users count per month.

Answer:
~~~~sql
select
to_char(('2021-01-01'::timestamp + ("Nth day" || ' days')::interval), 'YYYY-MM') as nth_year_month, sum("New users") from new_users
group by nth_year_month
order by nth_year_month
~~~~

4. 4. Show monthly avg and yearly ,old users revisting the website.

Answer:
~~~~sql
-- Didn't understand the question
~~~~

5. Show the max, avg and minimun user count for each year, next to the each months. (window)
   
Answer:
~~~~sql
-- Used only new user data as nothing is mentioned
-- Each month with year
select
to_char(('2021-01-01'::timestamp + ("Nth day" || ' days')::interval), 'YYYY-MM') as nth_year_month, 
min("New users") as minimum_user_count,
max("New users") as maximum_user_count,
avg("New users")::numeric(10,2) as average_user_count from new_users
group by nth_year_month
order by nth_year_month

-- Each year
select
to_char(('2021-01-01'::timestamp + ("Nth day" || ' days')::interval), 'YYYY') as nth_year, 
min("New users") as minimum_user_count,
max("New users") as maximum_user_count,
avg("New users")::numeric(10,2) as average_user_count from new_users
group by nth_year
order by nth_year
~~~~

6. Total number of users per month. Each month shouls be a column and each row representing a different year. (pivot)

Answer:
~~~~sql
select Extract('Year' from ('2021-01-01'::date + (aet."Nth day" || 'days')::interval)::date) as nth_year,
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '01') AS "Jan",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '02') AS "Feb",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '03') AS "Mar",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '04') AS "Apr",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '05') AS "May",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '06') AS "Jun",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '07') AS "Jul",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '08') AS "Aug",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '09') AS "Sep",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '10') AS "Oct",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '11') AS "Nov",
SUM("New users") FILTER (WHERE TO_CHAR(('2021-01-01'::timestamp + (aet."Nth day" || ' days')::interval), 'MM') = '12') AS "Dec"
from public.average_engagement_time aet
inner join public.new_users ns
on aet."Nth day" = ns."Nth day"
inner join public.user_count uc
on aet."Nth day" = uc."Nth day"
group by nth_year
order by nth_year
~~~~

7. Read the by country table, and sort the whole thing by number of users in decending order. replace country code with country name.

Answer:
~~~~sql
-- country_lookup has all the country code and names in it.
UPDATE country u
SET "Country ID" = cl.country_name
FROM country_lookup cl
WHERE u."Country ID" = cl.country_code;

SELECT * FROM public.country
order by "Users" desc
~~~~