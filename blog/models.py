from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ----------------------------
# Tag Model
# ----------------------------
# This model represents tags that can be associated with multiple blog posts.
# Many-to-Many relationship with Blog model:
# - A blog can have multiple tags.
# - A tag can belong to multiple blogs.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)  # Each tag must be unique

    def __str__(self):
        return self.tag_name


# ----------------------------
# Blog Model
# ----------------------------
# Represents the main blog post.
# Includes a Many-to-Many relationship with Tag model,
# and a One-to-Many relationship with BlogComment (via related_name).
class Blog(models.Model):
    # Choices for blog visibility or status
    BLOG_TYPE = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Draft', 'Draft'),
    ]

    title = models.CharField(max_length=200)  # Blog title
    pub_date = models.DateTimeField()         # Publication date
    image = models.ImageField(upload_to='images/')  # Image uploaded to 'images/' directory
    date = models.DateTimeField(default=timezone.now)  # Created date (default: now)
    draft = models.BooleanField(default=False)         # Flag to mark blog as draft
    blog_type = models.CharField(max_length=7, choices=BLOG_TYPE, default='Public')  # Type of blog
    description = models.TextField(default='', blank=True)  # Optional description/content

    # Many-to-Many relation with Tag model 
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

    def __str__(self):
        return self.title


# ----------------------------
# BlogComment Model
# ----------------------------
# Represents comments made on blog posts.
# One-to-Many relationship:
# - A blog can have many comments.
# - A comment belongs to one blog.
# Also links each comment to a specific User.
class BlogComment(models.Model):
    # ForeignKey to Blog model:
    # on_delete=models.CASCADE: if the blog is deleted, all related comments are also deleted.
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    # ForeignKey to built-in User model:
    # on_delete=models.CASCADE: if the user is deleted, their comments are also removed.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.TextField()  # Content of the comment
    date = models.DateTimeField(default=timezone.now)  # Date the comment was created

    def __str__(self): # Returns a string representation of the comment when not customizing the admin interface
        return f"{self.user.username}: {self.comment}"
