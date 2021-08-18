import logging
import time
from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def emit_clicks(
    host: str,
    rate_limit: float,
    limit: Optional[int] = None,
    country: str = 'TW',
    worker_id: int = 0,
    proxy_server: Optional[str] = None,
) -> int:
    '''emit clicks

    Args:
        host (str): hostname
        rate_limit (float): rate limit
        limit (Optional[int]): total number of clicks. optional
        country (str): country code
        worker_id (int): worker id
        proxy_server (Optional[str]):  proxy server

    Returns:
        int: number of clicks
    '''
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument('--mute-audio')
    if proxy_server:
        logger.info(f'Start chrome by proxy: {proxy_server}')
        options.add_argument(
            f'--proxy-server={proxy_server} --user-agent={ua.google}')
    driver = webdriver.Chrome(options=options)
    driver.get(host)
    driver.add_cookie({
        'name': "country",
        "value": country,
    })
    app = driver.find_element(By.ID, 'app')
    i = 0

    try:
        start = time.time()
        while True:
            actions = ActionChains(driver)
            actions.click(app)
            actions.perform()
            i += 1
            logger.info(
                "Worker: %s, Clicks: %s, PPS: %s /s",
                worker_id,
                i,
                round(i / (time.time() - start), 3),
            )
            driver.implicitly_wait(rate_limit)

            if limit and i >= limit:
                driver.close()
                return i

    except KeyboardInterrupt:
        driver.close()
        return i
