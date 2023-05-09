from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from cressive_test.settings.common import BASE_DIR
from scraping.models import BaseScraping, Organic, Sponsored
from threading import Thread
import os, re


class Scraping(object):

    def __init__(self):
        self.driver_path = os.path.join(os.path.dirname(BASE_DIR), 'scraping', 'utils', 'geckodriver')# driver
        self.base_url = 'https://www.amazon.co.uk/'

    def _get_field_text(self, tag, xpath):
        field_text = ""
        try:
            field = tag.find_element('xpath', xpath)
            field_text = field.text.encode('utf-8').decode('utf-8')

            return field_text

        except NoSuchElementException as e:
            print(e)
            return field_text
        
    def _get_link_of_search_keywords(self, driver, keyword):
        number_of_pages = self._get_number_of_pages(driver, keyword)
        link_of_items = []
        for page in range(1, number_of_pages+1):
            driver.get(f'https://www.amazon.co.uk/s?k={keyword}&page={page}')
            driver.implicitly_wait(5)
            search_results = driver.find_elements('xpath', "//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[@data-component-type='s-search-result']")

            for search_result in search_results:
                div_list = search_result.find_elements('xpath', ".//div[@class='a-section a-spacing-base']/div")
                if len(div_list) == 2:
                    a_tag = div_list[1].find_element('xpath', ".//div[@class='a-section a-spacing-none a-spacing-top-small s-title-instructions-style']/h2/a") #self._get_field_text(div_list[1], ".//div[@class='a-section a-spacing-none a-spacing-top-small s-title-instructions-style']/h2/a")
                    link_item = a_tag.get_attribute('href')
                    obj = {
                        "link": link_item,
                        "sponsored": False
                    }
                    sponsored = False #8-21-spons
                    if re.search(r'[0-9]{1,}-[0-9]{1,}-spons', link_item, re.IGNORECASE) != None:
                        sponsored = True
                    obj['sponsored'] = True if sponsored else False
                    link_of_items.append(obj)
        
        return link_of_items
        
    def _get_number_of_pages(self, driver, keyword):
        total_number_of_pages = 0
        try:
            driver.get(f'https://www.amazon.co.uk/s?k={keyword}&page=1')
            driver.implicitly_wait(5)
            number_of_results = driver.find_elements('xpath', "//div[@class='a-section a-spacing-small a-spacing-top-small']")
            number_of_results_str = re.sub(r"results(.)*|\s|over|\,", "", number_of_results[0].text.encode('utf-8').decode('utf-8'))
            split_number_of_results = number_of_results_str.split('of')
            page_number_of_results = re.sub(r"(.)*-", "", split_number_of_results[0])
            total_number_of_results = split_number_of_results[1]
            module_pages = int(total_number_of_results) % int(page_number_of_results)
            total_number_of_pages = int((int(total_number_of_results) / int(page_number_of_results)))
            if module_pages > 0:
                total_number_of_pages += 1
            # Make sure the number of pages won't exceed 5 pages
            if total_number_of_pages > 5:
                total_number_of_pages = 5
            return total_number_of_pages

        except NoSuchElementException as e:
            print(e)
            return total_number_of_pages
        
    def _load_page_item(self, driver, link_of_item):
        try:
            driver.get(link_of_item['link'])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "acrPopover")))
            return True

        except NoSuchElementException as e:
            print(e)
            return False
    
    def _get_info_search_keyword(self, driver, link_of_item):

        try:
            self._load_page_item(driver, link_of_item)
            title = self._get_field_text(driver, "//span[@id='productTitle']")
            price_whole = self._get_field_text(driver, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span/span[@class='a-price-whole']")
            price_fraction = self._get_field_text(driver, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span/span[@class='a-price-fraction']")
            price = f"{price_whole}.{price_fraction}"
            rating = self._get_field_text(driver, "//span[@id='acrPopover']/span/a/span")
            description = ""#self._get_field_text(driver, "//div[@id='productDescription']")
            sponsored = link_of_item['sponsored']
                
            print(f"title: {title}")
            print(f"price: {price}")
            print(f"rating: {rating}")
            print(f"sponsored: {link_of_item['sponsored']}")
            if title:
                if sponsored:
                    Sponsored.objects.create(
                        title=title,
                        price=price,
                        rating=rating,
                        description=description,
                        #sponsored=link_of_item['sponsored'],
                    )
                else:
                    Organic.objects.create(
                        title=title,
                        price=price,
                        rating=rating,
                        description=description,
                        #sponsored=link_of_item['sponsored'],
                    )

        except NoSuchElementException as e:
            print(e)

    def _get_all_info_search_info(self, driver, keyword):
        try:
            keyword_without_spaces = re.sub(r"\s{1,}", "+", keyword)
            link_of_items = self._get_link_of_search_keywords(driver, keyword_without_spaces)
            index = 0
            for link_of_item in link_of_items:
                print(f"---------------- {index} -----------------------")
                self._get_info_search_keyword(driver, link_of_item)
                index += 1
        except NoSuchElementException as e:
            print(e)

    # def _get_all_info_search_info(self, driver, keywords):
    #     try:

    #     except NoSuchElementException as e:
    #         print(e)

    def _get_all_keywords_info(self, driver, keywords):
        for keyword in keywords:
            self._get_all_info_search_info(driver, keyword['name'])
        
    def start_scraping(self, keywords):
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options, executable_path=self.driver_path)
        # This will be executed in background.
        thread = Thread(target=self._get_all_keywords_info, args=[driver, keywords])
        thread.start()
        # Returning the 'response' json without waiting for results of 'tread'.
        response = {'request': {"status": "started!"}}

        return response
        