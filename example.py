from tst_category import CategoryTester
import sys

assert sys.version_info >= (3, 0)

# try to test with mock data rather than fetching data from the server
print("At first, Let's do a mock test without fetching data from the server")            
mock_data = {'Name': 'Test', 'CanRelist': True, 'Promotions': [{'Name': 'Tom', 'Description': 'Well done'}]}
tester = CategoryTester(mock_data=mock_data)
tester.test(key='Name', expected_value=mock_data['Name'])
tester.test(key='CanRelist', expected_value=mock_data['CanRelist'])
tester.test(key='Promotions', expected_value=mock_data['Promotions'])

# do a real test by fetching data from the server    
print("\nLet's do a real test")            
tester = CategoryTester(id=6327)
tester.test(key='Name', expected_value='Carbon credits')
tester.test(key='CanRelist', expected_value=True)
tester.test(key='Promotions', expected_value={'Name': 'Gallery', 'Description': 'Good position in category'})
