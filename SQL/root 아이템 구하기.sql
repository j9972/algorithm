-- 코드를 작성해주세요
select 
t.ITEM_ID, i.ITEM_NAME
from ITEM_INFO as i
join ITEM_TREE as t
on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID is NULL