import unittest
import pandas as pd
from utils.transform import DataTransformer

class TestDataTransformer(unittest.TestCase):

    def test_transform_data_with_rupiah(self):
        # Arrange
        products = [
            {'title': 'Product A', 'price': 'Rp10.000', 'rating': '4.2', 'colors': 'Red', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product B', 'price': 'Rp20.500', 'rating': '4.8', 'colors': 'Blue', 'size': 'L', 'gender': 'Women'}
        ]
        
        # Membuat instance dari DataTransformer
        transformer = DataTransformer(products)

        # Act
        df = transformer.transform()
        
        # Assert
        self.assertEqual(len(df), 2)  # Mengharapkan ada dua produk setelah transformasi
        self.assertIn('price', df.columns)  # Memastikan ada kolom 'price'
        self.assertTrue(df['price'].iloc[0] > 0)  # Memastikan harga lebih besar dari 0
        self.assertEqual(df['title'].iloc[0], 'Product A')  # Memastikan nama produk pertama
        self.assertIsInstance(df['price'].iloc[0], (int, float))  # Memastikan harga bertipe numerik
        self.assertIn('timestamp', df.columns)  # Memastikan ada kolom 'timestamp'

    def test_transform_ignores_invalid_rupiah(self):
        # Arrange
        products = [
            {'title': 'Broken Product', 'price': 'RpABC', 'rating': '4.0', 'colors': 'Black', 'size': 'XL', 'gender': 'Unisex'}
        ]
        
        # Membuat instance dari DataTransformer
        transformer = DataTransformer(products)

        # Act
        df = transformer.transform()

        # Assert
        self.assertEqual(len(df), 0)  # Seharusnya tidak ada data yang lolos karena harga tidak valid

if __name__ == '__main__':
    unittest.main()
