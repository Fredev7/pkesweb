from django.test import TestCase

from gallery_app.models import Gallery


class TestGalleriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Gallery.objects.create(title='djangoGallery', description='djangoGallery', image='image')
    
    def test_gallery_model_entry(self):
        """
        Test Gallery model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Gallery))
        self.assertEqual(str(data), 'djangoGallery')

    
