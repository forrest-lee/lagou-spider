SELECT city, search_keyword, count(search_keyword) total FROM lagou.position
GROUP BY search_keyword,city order by city;

SELECT search_keyword,count(search_keyword) total FROM lagou.position
GROUP BY search_keyword order by search_keyword;

SELECT city,count(*) total FROM lagou.position
GROUP BY city order by city;

SELECT count(*) total FROM lagou.position;

select * from position
where company like '%腾讯%';


select distinct position_id,company from lagou.position;

