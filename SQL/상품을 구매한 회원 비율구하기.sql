select 
    distinct 
    YEAR(o.SALES_DATE) as YEAR,
    MONTH(o.SALES_DATE) as MONTH,
    count(distinct i.USER_ID) as PUCHASED_USERS,
    round(count(DISTINCT o.USER_ID) / 
            (select count(USER_ID)
            from USER_INFO 
            where YEAR(JOINED) = '2021'), 1) as PUCHASED_RATIO
        
    from ONLINE_SALE as o
    join USER_INFO as i
    on i.USER_ID = o.USER_ID
    where YEAR(i.JOINED) = '2021'
    group by YEAR, MONTH