
CREATE FUNCTION pres_full_name(term int) RETURNS text AS
$$
BEGIN
    DECLARE fullname text;

    SELECT concat(fname, ' ', lname) 
    INTO fullname 
    FROM presidents
    WHERE num = term;

    RETURN fullname;
END
$$
LANGUAGE PLPGSQL
