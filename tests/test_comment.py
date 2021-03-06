from app.models import User,Comment
from app import db
import unittest

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.user_Venus = User(username = 'venus',password = 'test', email = 'venus@gg.com')
        self.new_comment = Comment("Nice blog",blog_id = 123, user_id=self.user_Venus)
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"Nice blog")
        self.assertEquals(self.new_comment.blog_id,123)
        self.assertEquals(self.new_comment.user,self.user_Venus)
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
    