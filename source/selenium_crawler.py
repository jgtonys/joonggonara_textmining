from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs


def main(location, link, filename, driver):
    # Get to web page (url)
    driver.get('http://cafe.naver.com/joonggonara')

    # Wait until driver load resources
    wait = WebDriverWait(driver, 30)

    # Wait until specific css resource is loaded
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.gm-tcol-c")))


    location_group = driver.find_element_by_css_selector("a[title*='" + location + "']")
    driver.execute_script("arguments[0].scrollIntoView();", location_group)
    location_group.click();

    elm = driver.find_element_by_id(link)
    driver.execute_script("arguments[0].scrollIntoView();", elm)
    elm.click()

    iframe_element = driver.find_element_by_css_selector("iframe#cafe_main")
    driver.switch_to.frame(iframe_element)

    first = 0
    end = 11
    page_10th = 99

    f = codecs.open(filename+"(2019).txt", 'w', encoding='utf-8')
    fo = codecs.open(filename + "(~2019).txt", 'w', encoding='utf-8')

    file_switch_flag = False

    notice_hidden = driver.find_element_by_css_selector("label[for*='notice_hidden']")
    driver.execute_script("arguments[0].scrollIntoView();", notice_hidden)
    notice_hidden.click()


    for ten in range(page_10th):
        for i in range(first, end):
            page_button = driver.find_element_by_class_name("prev-next")
            driver.execute_script("arguments[0].scrollIntoView();", page_button)
            page_buttons = driver.find_elements_by_css_selector("div.prev-next a")

            if (ten is not 0) and (len(page_buttons) <= 11) and (i is len(page_buttons)):
                debug_last_date = driver.find_elements_by_css_selector("td.td_date")
                if file_switch_flag:
                    fo.write("-----last date : " + debug_last_date[0].text)
                else:
                    f.write("-----last date : " + debug_last_date[0].text)

                print("-----last date : " + debug_last_date[0].text)
                print("DEBUG TERMINATION")
                return 0;

            page_buttons[i].click()

            #print("number of pages : " + str(len(page_buttons)))

            if i is end-1:
                first = 1
                end = 12
            else:
                print("------------" + filename + " " + str(10 * ten + i) + "page---------------")

                articles = driver.find_elements_by_css_selector("td.td_article")
                date = driver.find_elements_by_css_selector("td.td_date")[0].text

                if date[:4] == "2018":
                    print("FLAG-------------------------")
                    file_switch_flag = True

                for article in articles:
                    title_text = article.find_element_by_css_selector('a.article').text
                    if file_switch_flag:
                        fo.write(title_text+"\n")
                    else:
                        f.write(title_text+"\n")


        # DEBUG MODE
        if ten is page_10th-1:
            debug_last_date= driver.find_elements_by_css_selector("td.td_date")
            f.write("-----last date : " + debug_last_date[0].text)
            print("-----last date : " + debug_last_date[0].text)

