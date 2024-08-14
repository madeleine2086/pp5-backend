from django.contrib.auth.models import User
from .models import Review
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_review(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_review(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        response = self.client.post(
            '/reviews/',
            {'post': 1,
             'product_name': 'product_name',
             'content': 'content'
             })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_review(self):
        response = self.client.post(
            '/reviews/',
            {'product_name': 'product_name',
             'content': 'content'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReviewViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        colm = User.objects.create_user(username='colm', password='pass')
        Post.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Post.objects.create(
            owner=adam, title='colms title', content='colms content'
        )
        Review.objects.create(
            post_id=1,
            owner=adam, product_name='product_name', content='content'
        )
        Review.objects.create(
            post_id=2,
            owner=colm, product_name='product_name', content='content'
        )

    def test_can_retrieve_review_using_valid_id(self):
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.data['product_name'], 'product_name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_review_using_invalid_id(self):
        response = self.client.get('/reviews/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_review(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/reviews/1/',
            {'product_name':
             'a product',
             'content': 'content'
             })
        review = Review.objects.filter(pk=1).first()
        self.assertEqual(review.product_name, 'a product')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_review(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/reviews/2/',
            {'product_name':
             'a new product',
             'content': 'content'
             })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)