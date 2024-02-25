select case
when SKILL_CODE&(select CODE
    from SKILLCODES
    where NAME = 'Python') and
    
    SKILL_CODE&(select sum(CODE)
    from SKILLCODES
    where CATEGORY = 'Front End') then 'A'
    
when SKILL_CODE&(select CODE
    from SKILLCODES
    where NAME = 'C#') then 'B'

when SKILL_CODE&(select sum(CODE)
    from SKILLCODES
    where CATEGORY = 'Front End') then 'C' 

end GRADE,
ID, EMAIL
from DEVELOPERS
having GRADE is not null
order by GRADE, ID