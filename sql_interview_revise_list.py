# 1. SQL fundamentals and tricky concepts
# 1. What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?
# 2. What is the default join when we write JOIN without specifying a type?
# 3. What is the difference between WHERE and HAVING?
# 4. What is the logical execution order of a SQL query?
# 5. What is the difference between UNION and UNION ALL?
# 6. What is the difference between COUNT(*), COUNT(column), and COUNT(DISTINCT column)?
# 7. How does SQL handle NULL? Why does NULL = NULL not evaluate to true?
# 8. What is the difference between IN, EXISTS, and NOT EXISTS?
# 9. What is the difference between a subquery and a CTE (WITH clause)?
# 10. What is the difference between DELETE, TRUNCATE, and DROP?
# 2. Query-writing problems
# Assume these tables:
# - employees(employee_id, name, department_id, salary, email)
# - customers(customer_id, name)
# - policies(policy_id, customer_id, status, premium)
# - claims(claim_id, policy_id, customer_id, status, claim_amount, created_at)
# 11. Write a query to find the second-highest distinct salary.
# 12. Find duplicate email addresses in the employees table.
# 13. Find employees earning more than the average salary of their department.
# 14. Find the top three highest-paid employees in each department.
# 15. Find the latest claim for each policy.
# 16. Find customers who have never submitted a claim.
# 17. Find policies that have no claims.
# 18. Find customers who have more than three claims.
# 19. Calculate the total claim amount for each customer.
# 20. Find the highest-paid employee in each department, including ties.
# 21. Find employees whose salary is greater than their manager's salary.
# 22. Find records created in the last 30 days.
# 23. Find the third-highest salary without using LIMIT or OFFSET.
# 24. Delete duplicate rows while keeping one record per email.
# 25. Find consecutive days on which a customer submitted claims.
# 3. Window functions
# 26. What is the difference between ROW_NUMBER(), RANK(), and DENSE_RANK()?
# 27. How do you find the second-highest salary using DENSE_RANK()?
# 28. What is the difference between GROUP BY and window functions?
# 29. How do you calculate a running total using SUM() OVER()?
# 30. How do you compare each employee's salary with the previous employee's salary using LAG()?
# 31. How do you retrieve the first and last record in each group?
# 32. What is the purpose of PARTITION BY?
# 4. Indexing and query optimization
# 33. What is an index, and how does it improve query performance?
# 34. What is the difference between a B-tree index and a hash index in PostgreSQL?
# 35. What is a composite index? How does column order affect it?
# 36. Why might PostgreSQL ignore an existing index?
# 37. Why can applying LOWER(), DATE(), or EXTRACT() to an indexed column make a query slower?
# 38. What is the difference between EXPLAIN and EXPLAIN ANALYZE?
# 39. How would you troubleshoot a query that takes 10 seconds to execute?
# 40. What is an N+1 query problem, and how would you fix it in Django or SQLAlchemy?
# 41. What is a partial index? When would you use one?
# 42. What is table partitioning, and how is it different from indexing?
# 5. Transactions and concurrency
# 43. What are ACID properties?
# 44. What are transaction isolation levels?
# 45. What is the difference between optimistic and pessimistic locking?
# 46. What does SELECT ... FOR UPDATE do?
# 47. What is a deadlock, and how do you handle one?
# 48. What is a lost update, and how can you prevent it?
# 49. What is the difference between COMMIT and ROLLBACK?
# 50. How would you prevent two requests from approving the same insurance claim simultaneously?
# 51. What happens when a transaction fails before COMMIT?
# 52. What is the difference between a unique constraint and a unique index in PostgreSQL?
# 6. PostgreSQL-specific questions
# 53. What are CTEs, and when would you use recursive CTEs?
# 54. What is the difference between JSON and JSONB?
# 55. What are COALESCE() and NULLIF()?
# 56. How do DATE_TRUNC(), EXTRACT(), AGE(), and INTERVAL work?
# 57. What is an upsert, and how does INSERT ... ON CONFLICT work?
# 58. What is a materialized view, and how is it different from a normal view?
# 59. What is RETURNING used for in PostgreSQL?
# 60. How do connection pooling and too many database connections affect a FastAPI application?
# 7. Real-world backend scenarios
# 61. An API endpoint is slow because it retrieves 100,000 rows. How would you optimize it?
# 62. Two API requests attempt to deduct money from the same account. How would you prevent incorrect balances?
# 63. A report joins five tables and takes 15 seconds. How would you investigate and optimize it?
# 64. How would you implement pagination for millions of records: offset or keyset pagination?
# 65. How would you safely update millions of rows without holding a large transaction for too long?
# 66. A query works locally but is slow in production. What would you check?
# 67. How would you design indexes for a frequently used filtering and sorting query?
# 68. How would you handle database connection failures and transaction retries in Python?
# 69. When would you choose a database constraint instead of validating only in Python?
# 70. How would you implement idempotency to prevent duplicate records when an API request is retried?