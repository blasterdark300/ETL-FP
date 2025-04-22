import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_main

class TestExtract(unittest.TestCase):
    
    @patch('utils.extract.requests.get')
    def test_scrape_main_returns_expected_product(self, mock_get):
        """
        Test sukses: memastikan scrape_main mengembalikan data produk yang benar
        ketika HTML valid dan respons berhasil.
        """
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Cool Jacket</h3>
                    <div class="price-container">$45</div>
                    <p>Rating: 4.5 stars</p>
                    <p>Colors: Black, White</p>
                    <p>Size: XL</p>
                    <p>Gender: Male</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        result = scrape_main(url)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        product = result[0]
        self.assertEqual(product['title'], 'Cool Jacket')
        self.assertEqual(product['price'], '$45')
        self.assertIn('Black', product['colors'])
        self.assertIn('XL', product['size'])

    @patch('utils.extract.requests.get')
    def test_scrape_main_raises_exception_on_http_error(self, mock_get):
        """
        Test gagal: memastikan scrape_main melempar error ketika HTTP gagal (misalnya 404).
        """
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as err:
            scrape_main(url)

        self.assertIn("404", str(err.exception))

if __name__ == '__main__':
    unittest.main()
