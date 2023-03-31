# NAME, PASSWORD, TYPE
# types: 'Admin', 'Chair', 'Author', 'Reviewer'
USERS: list[tuple[int, str, str, str]] = [
    (0, "Admin", "test", "Admin"),
    (1, "Chair", "test", "Chair"),
    (2, "Author", "test", "Author"),
    (3, "Reviewer", "test", "Reviewer"),
]

db_userlogins = {x[1]: (x[2], x[0]) for x in USERS}
db_userdata = {x[0]: x[1:] for x in USERS}


