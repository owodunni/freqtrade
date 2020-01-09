""" Binance exchange subclass """
import logging
from typing import Dict

import ccxt

from freqtrade.exceptions import (DependencyException, InvalidOrderException,
                                  OperationalException, TemporaryError)
from freqtrade.exchange import Exchange

logger = logging.getLogger(__name__)


class Uniswap(Exchange):

    _ft_has: Dict = {
        "stoploss_on_exchange": True,
        "order_time_in_force": ['gtc', 'fok', 'ioc'],
        "trades_pagination": "id",
        "trades_pagination_arg": "fromId",
    }

    def __init__(self, config: dict, validate: bool = True) -> None:
        if config['dry_run']:
            logger.info('Instance is running with dry_run enabled')