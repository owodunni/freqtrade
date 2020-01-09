import logging

from tests.conftest import get_patched_exchange, log_has, log_has_re

def test_init(default_conf, mocker, caplog):
    caplog.set_level(logging.INFO)
    exchange = get_patched_exchange(mocker, default_conf, id="uniswap")
    assert log_has('I am Uniswap!', caplog)