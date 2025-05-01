import framework

class TestStub(framework.TestCase):
    def test_success(self):
        self.assert_true(True)

    def test_failure(self):
        self.assert_true(False)

    def test_error(self):
        raise Exception

class TestSpy(framework.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"

class TestCaseTest(framework.TestCase):
    def set_up(self):
        self.result = framework.TestResult()

    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 0 error')

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 1 failed, 0 error')

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 1 error')

    def test_result_multiple_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        stub = TestStub('test_failure')
        stub.run(self.result)
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '3 run, 1 failed, 1 error')

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_set_up)

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_run)

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_tear_down)

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_equal(spy.log, "set_up test_method tear_down")

    def test_assert_true(self):
        self.assert_true(True)

    def test_assert_false(self):
        self.assert_false(False)

    def test_assert_equal(self):
        self.assert_equal("", "")
        self.assert_equal("foo", "foo")
        self.assert_equal([], [])
        self.assert_equal(['foo'], ['foo'])
        self.assert_equal((), ())
        self.assert_equal(('foo',), ('foo',))
        self.assert_equal({}, {})
        self.assert_equal({'foo'}, {'foo'})

    def test_assert_in(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}
        self.assert_in('a', 'abc')
        self.assert_in('foo', ['foo'])
        self.assert_in(1, [1, 2, 3])
        self.assert_in('monkey', animals)

class TestSuiteTest(framework.TestCase):
    def test_suite_size(self):
        suite = framework.TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        self.assert_equal(len(suite.tests), 3)

    def test_suite_success_run(self):
        result = framework.TestResult()
        suite = framework.TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        self.assert_equal(result.summary(), '1 run, 0 failed, 0 error')

    def test_suite_multiple_run(self):
        result = framework.TestResult()
        suite = framework.TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        suite.run(result)
        self.assert_equal(result.summary(), '3 run, 1 failed, 1 error')

class TestLoaderTest(framework.TestCase):
    def test_create_suite(self):
        loader = framework.TestLoader()
        suite = loader.make_suite(TestStub)
        self.assert_equal(len(suite.tests), 3)

    def test_create_suite_of_suites(self):
        loader = framework.TestLoader()
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)
        suite = framework.TestSuite()
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)
        self.assert_equal(len(suite.tests), 2)

    def test_get_multiple_test_case_names(self):
        loader = framework.TestLoader()
        names = loader.get_test_case_names(TestStub)
        self.assert_equal(sorted(names), ['test_error', 'test_failure', 'test_success'])

    def test_get_no_test_case_names(self):
        class Test(framework.TestCase):
            def foobar(self):
                pass
        loader = framework.TestLoader()
        names = loader.get_test_case_names(Test)
        self.assert_equal(names, [])

if __name__ == "__main__":
    loader = framework.TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = framework.TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = framework.TestRunner()
    runner.run(suite)
