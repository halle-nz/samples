# Description
This is a simple demostration for showing an API test.

class CategoryTester is used to handle all things to do the test:
1) fetch data from the server
2) check the value or the existance in a dict object

# How to use it?

## try to test with mock data rather than fetching data from the server
mock_data = {'Name': 'Test', 'CanRelist': True, 'Promotions': [{'Name': 'Tom', 'Description': 'Well done'}]}
tester = CategoryTester(mock_data=mock_data)
tester.test(key='Name', expected_value=mock_data['Name'])
tester.test(key='CanRelist', expected_value=mock_data['CanRelist'])
tester.test(key='Promotions', expected_value=mock_data['Promotions'])

## do a real test by fetching data from the server    
tester = CategoryTester(id=6327)
tester.test(key='Name', expected_value='Carbon credits')
tester.test(key='CanRelist', expected_value=True)
tester.test(key='Promotions', expected_value={'Name': 'Gallery', 'Description': 'Good position in category'})

The running result of example.py:
```
At first, Let's do a mock test without fetching data from the server

Test passed: Name == Test

Test passed: CanRelist == True

Test passed: Promotions == [{'Name': 'Tom', 'Description': 'Well done'}]

Let's do a real test

Try to fetch data from remote host..

Test passed: Name == Carbon credits

Test passed: CanRelist == True

Test passed: Promotions == {'Name': 'Gallery', 'Description': 'Good position in category'}
```