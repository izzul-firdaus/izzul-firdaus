import backend.backend as back


class Controller:
    def __init__(self):
        pass


class User(Controller):
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def select_user_type():
        ...

    def login(self):
        result = back.login(self.name, self.password)
        if result == -1:
            return None
        return back.get_user_data(result)

    def logout(self):
        return True


class Author(User):
    def __init__(self, author_id: int, author_name: str):
        self.author_id = author_id
        self.author_name = author_name

    def create_paper():
        ...

    def submit_paper():
        ...

    def edit_paper():
        ...

    def search_paper():
        ...

    def view_paper_status():
        ...

    def view_paper_ratings():
        ...

    def view_notifications():
        ...


class Admin(User):
    def __init__(
        self,
    ):
        ...

    def create_user():
        ...

    def view_user():
        ...

    def suspend_user():
        ...

    def update_user():
        ...

    def create_user_profile():
        ...

    def suspend_user_profile():
        ...

    def update_user_profile():
        ...

    def view_user_profile():
        ...


class Reviewer(User):
    def __init__(
        self,
    ):
        ...

    def submit_bid():
        ...

    def view_bid():
        ...

    def update_bid():
        ...

    def delete_bid():
        ...

    def set_maximum_paper():
        ...

    def create_reviews():
        ...

    def submit_reviews():
        ...

    def submit_ratings():
        ...

    def update_reviews():
        ...

    def update_ratings():
        ...

    def delete_reviews():
        ...

    def delete_ratings():
        ...

    def view_reviews():
        ...

    def view_ratings():
        ...

    def add_comments():
        ...


class Chair(User):
    def __init__(
        self,
    ):
        ...


class ReviewRating(Controller):
    def __init__(
        self,
    ):
        ...


class Paper(Controller):
    def __init__(
        self,
    ):
        ...


class Bid(Controller):
    def __init__(
        self,
    ):
        ...


class Comment(Controller):
    def __init__(
        self,
    ):
        ...
