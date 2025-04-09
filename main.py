
import asyncio
from pydoll.browser.chrome import Chrome
from pydoll.constants import By

async def main():
    async with Chrome() as browser:
        await browser.start()
        page = await browser.get_page()
        
        await page.go_to('https://google.com')
        search_box = await page.find_element(By.CSS_SELECTOR, '[name="q"]')
        await search_box.click()
        await search_box.type_keys("MTN Store - Sandton City", interval=0.2)
        search_button = await page.find_element(
            By.CSS_SELECTOR, '[value="Google Search"]'
        )
        await search_button.click()
        await asyncio.sleep(3)
        reviews_link = await page.find_element(
            By.CSS_SELECTOR,
            '[data-async-trigger="reviewDialog"]'
        )
        await reviews_link.click()
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
