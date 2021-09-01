class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author


    def get_post_message (self):
        print(f"Post: {self.message} {self.author}")

