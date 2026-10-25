# Sources

1. Attack = SQL typed into input data (lines 2, 4)
   - https://community.owasp.org/attacks/SQL_Injection (opened; owasp.org/www-community/attacks/SQL_Injection redirects here)
   - "A SQL injection attack consists of insertion or “injection” of a SQL query via the input data"

2. Read/change database data (lines 1, 5)
   - same page: "A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete)"

3. Log in without the password (line 5)
   - same page: "it may be possible to connect to a system as another user with no previous knowledge of the password."

4. Careless app glues text into the query (line 3)
   - https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html (opened): injection happens when queries are built "using string concatenation with dynamic untrusted malicious data."

5. Parameterized queries fix it (line 6)
   - same cheat sheet: "Injecting dynamic data through parameterized queries ensure that an attacker is not able to change the intent of a query."
   - Example there: input `tom' or '1'='1` is matched as a literal string, i.e. treated as data, not SQL. "Data, never code" is our paraphrase of that example.
