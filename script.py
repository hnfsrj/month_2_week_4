import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
django.setup()


from BlogApp.models import Post
from CommentApp.models import Comment


#create

instance = Post(Title='Title 1', Content='This is content 1.', Category = 'category1')
instance.save()

instance2 = Post(Title='Title 2', Content='This is content 2.', Category = 'category2')
instance2.save()

instance3 = Post(Title='Title 3', Content='This is content 3.', Category = 'category3')
instance3.save()

#query

category = Post.objects.filter(Category ='category1')
print(category)

#update
update = Post.objects.get(Category='category2')

update.content = 'Updated content'
update.save()

#delete

delete = Post.objects.get(Category='category3')

delete.save()


#-------------------Comments------------------------

#create

p_instance1 = Post.objects.filter(Category ='category1')
p_instance2 = Post.objects.filter(Category ='category2')

c_instance = Comment(Content='This is content 1.', Author = 'author1', Post = p_instance1)
c_instance.save()

c_instance2 = Comment(Content='This is content 2.', Author = 'author2', Post = p_instance2)
c_instance2.save()

c_instance3 = Comment(Content='This is content 3.', Author = 'author3', Post = p_instance2)
c_instance3.save()

#query

category = Comment.objects.filter(Post = p_instance2)
print(category)

#update
update = Comment.objects.get(Author='author3')

update.content = 'Updated content'
update.save()


#delete

delete = Comment.objects.get(Author='author3')

delete.save()