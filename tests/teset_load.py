import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets

class TestDataSaving(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_should_save_dataframe_to_csv(self, mock_to_csv):
        # Simulasi DataFrame sebagai input
        dummy_df = pd.DataFrame({
            'title': ['Kaos Polos', 'Jaket Hoodie'],
            'price': [15000, 35000],
            'rating': [4.0, 4.8]
        })

        # Pemanggilan fungsi
        save_to_csv(dummy_df, 'dummy_output.csv')

        # Validasi bahwa .to_csv dipanggil dengan benar
        mock_to_csv.assert_called_once_with('dummy_output.csv', index=False)

    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_should_push_data_to_google_sheets(self, mock_creds_loader, mock_google_build):
        # Dummy dataframe
        df = pd.DataFrame({
            'title': ['Celana Jeans', 'Kemeja Batik'],
            'price': [50000, 60000],
            'rating': [4.2, 4.7]
        })

        # Setup mock kredensial dan service
        mock_creds_loader.return_value = MagicMock()
        mock_service = MagicMock()
        mock_google_build.return_value = mock_service

        # Jalankan fungsi penyimpanan
        save_to_google_sheets(df, 'fake_spreadsheet_id', 'Sheet1!A2')

        # Pastikan method update pada API Google Sheets dipanggil sekali
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

if __name__ == '__main__':
    unittest.main()
