# Rule-to-Constraint Matrix

| # | Business Rule | Enforcement Mechanism |
|---|---|---|
| 1 | Student email must be unique | UNIQUE constraint on student.s_email |
| 2 | Student can have only one active internship at a time | Application-level validation |
| 3 | Student cannot repeat a completed internship | student_internship history + application validation |
| 4 | Every internship has exactly one supervisor | Foreign Key internship.t_id + UNIQUE(t_id) |
| 5 | A supervisor can supervise only one internship | UNIQUE constraint on internship.t_id |