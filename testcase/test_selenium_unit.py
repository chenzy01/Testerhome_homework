import pytest
from selenium.webdriver.ie.options import Options


@pytest.fixture
def opts():
    yield Options()


@pytest.mark.parametrize("TIMEOUT", (0.6, 5))
def test_browser_attach_timeout(opts, TIMEOUT):
    opts.browser_attach_timeout = TIMEOUT
    assert opts.browser_attach_timeout == TIMEOUT






