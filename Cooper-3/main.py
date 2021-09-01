from user import User
from post import Post

app_user_one = User("cooper@cc.com", "Cooper", "passwd", "DevOps")

app_user_one.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)

new_post.get_post_message()