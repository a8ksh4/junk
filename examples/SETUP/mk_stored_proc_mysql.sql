
delimiter //
drop procedure if exists pres_full_name;
create procedure pres_full_name(term int)
begin
    select concat(fname, ' ', lname) from presidents
    where num = term;
end//
