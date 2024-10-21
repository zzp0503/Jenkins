import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
driver = webdriver.Chrome()
driver.get('http://a.com:8022/vul/sqli/sqli_str.php')
driver.maximize_window()

# 等待验证码元素加载完成
wait = WebDriverWait(driver, 10)
slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-class')))
bg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-class')))

# 获取滑块和背景图像
slider_img = slider.screenshot_as_png
bg_img = bg.screenshot_as_png

# 使用PIL打开图像
slider_image = Image.open(BytesIO(slider_img))
bg_image = Image.open(BytesIO(bg_img))

# 转换为OpenCV图像
slider_cv = np.array(slider_image)
bg_cv = np.array(bg_image)

# 使用OpenCV模板匹配找到滑块位置
result = cv2.matchTemplate(bg_cv, slider_cv, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(result)

# 计算滑块需要滑动的距离
slider_distance = max_loc[0] - (bg_cv.shape[1] - slider_cv.shape[1])

# 模拟滑动操作
action = ActionChains(driver)
action.click_and_hold(slider).perform()
action.move_by_offset(slider_distance, 0).perform()
action.release().perform()

# 验证滑块是否滑动成功
# 这里需要根据页面上的反馈来判断，例如检查某个元素是否出现
success_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'success-class')))
if success_element:
    print("滑动验证成功")
else:
    print("滑动验证失败")

# 关闭WebDriver
driver.quit()