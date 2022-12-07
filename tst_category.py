import requests

class Tester(object):
    """Base class for tester objects"""

    COLOR_OK = '\033[94m'
    COLOR_INFO = '\033[93m'
    COLOR_FAIL = '\033[91m'
    COLOR_ENDC = '\033[0m'
    COLOR_BOLD = '\033[1m'

    def __init__(self, verbose=True):
        self.verbose = verbose

    def print_pass(self, str):
        print(self.COLOR_BOLD + self.COLOR_OK + '\n{0}'.format(str) + self.COLOR_ENDC)

    def print_fail(self, str):
        print(self.COLOR_BOLD + self.COLOR_FAIL + '\n{0}'.format(str) + self.COLOR_ENDC)

    def print_info(self, str):
        if self.verbose:
            print(self.COLOR_BOLD + self.COLOR_INFO + '\n{0}'.format(str) + self.COLOR_ENDC)

class CategoryTester(Tester):
    """Fetch Category information from api.tmsandbox.co.nz, and check some attributes in the resposne"""

    def __init__(self, 
                 id=None, 
                 catalogue=False, 
                 base_url='https://api.tmsandbox.co.nz/v1/Categories', 
                 verbose=True, 
                 mock_data = None):
        Tester.__init__(self, verbose=verbose)
        self.id = id
        self.catalogue = catalogue
        self.base_url = base_url
        self.data = mock_data

    def _fetch_category_info(self) -> dict:
        url = '{0}/{1}/Details.json?catalogue={2}'.format(self.base_url, self.id, self.catalogue)
        self.print_info('Try to fetch data from remote host..')
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.data = resp.json()

    def _check_atribute(self, key, expected_value) -> bool:
        if self.data is None:
            self._fetch_category_info()

        if key not in self.data.keys():
            self.print_info('Could not find key:{0}'.format(key))
            return False

        if self.data[key] == expected_value:
            return True

        return False

    def _check_array(self, key, expected_value):
        if self.data is None:
            self._fetch_category_info()

        if key not in self.data:            
            self.print_info('Could not get {0} from response'.format(key))
            return False

        values = self.data[key]
        if not isinstance(values, list):
            self.print_info('{0} is not a instance of list'.format(key))
            return False

        for value in values:
            ret = True
            for key in expected_value.keys():
                if value[key] != expected_value[key]:
                    ret = False
                    break

            if ret:
                return True

        self.print_info('Not all items have been matched.')
        return False

    def test(self, key, expected_value):
        if isinstance(expected_value, dict):
            result = self._check_array(key, expected_value)
        else:
            result = self._check_atribute(key, expected_value)

        if result:
            self.print_pass('Test passed: {0} == {1}'.format(key, expected_value))
        else:
            self.print_fail('Test failed: {0} != {1}'.format(key, expected_value))
