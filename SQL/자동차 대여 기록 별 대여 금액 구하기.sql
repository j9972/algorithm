-- 코드를 입력하세요
with value as
(
    select c.DAILY_FEE, c.CAR_TYPE, h.HISTORY_ID, DATEDIFF(END_DATE, START_DATE) + 1 as period,
        case
            when DATEDIFF(END_DATE, START_DATE) +1 >= 90 then '90일 이상'
            when DATEDIFF(END_DATE, START_DATE) +1 >= 30 then '30일 이상'
            when DATEDIFF(END_DATE, START_DATE) +1 >= 7 then '7일 이상'
            else 'NONE'
        end as duration_type
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    join CAR_RENTAL_COMPANY_CAR as c
    on c.CAR_ID = h.CAR_ID
    where c.CAR_TYPE = '트럭'
)


SELECT value.HISTORY_ID, 
    round(value.DAILY_FEE * value.period * (100 - ifnull(p.DISCOUNT_RATE, 0)) / 100) as FEE
    from value
    left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on p.duration_type = value.duration_type
    and p.CAR_TYPE = value.CAR_TYPE
    
    order by FEE desc , HISTORY_ID desc