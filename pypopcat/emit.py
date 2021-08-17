import logging
import time
from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def emit_clicks(
    host: str,
    rate_limit: float,
    limit: Optional[int] = None,
    country: str = 'TW',
):
    '''emit clicks

    Args:
        host (str): hostname
        rate_limit (float): rate limit
        limit (int): total number of clicks. optional
        country (str): country code
    '''
    options = webdriver.ChromeOptions()
    options.add_argument('--mute-audio')
    driver = webdriver.Chrome(options=options)
    driver.get(host)
    driver.add_cookie({
        'name': "country",
        "value": country,
    })
    app = driver.find_element_by_id('app')
    i = 0

    while True:
        actions = ActionChains(driver)
        actions.click(app)
        actions.perform()
        i += 1
        logger.info("Click Stats: %s", i)
        time.sleep(rate_limit)

        if limit and i >= limit:
            break

    driver.close()
