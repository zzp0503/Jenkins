# 登录模块
class Login_element:
    username = '//*[@id="app"]/div/div[1]/div/div[3]/form/div[1]/div/div/input'
    password = '//*[@id="app"]/div/div[1]/div/div[3]/form/div[2]/div/div/input'
    login_button = '//*[@id="app"]/div/div[1]/div/div[3]/form/div[3]/div/button'


# 弱口令模块
class Weak_pwd:
    # 应用高级防御设置模块
    defense = '/html/body/div[1]/section/div/div[2]/div[1]/div/ul/li[4]/i'
    # 弱口令模块
    weak = '//*[@id="tab-weak-password"]'
    # 添加按钮
    add = '/html/body/div[1]/section/section/main/div[1]/div[2]/div[2]/div/div[1]/div/div/button/span'
    # 编辑按钮，索引0
    update = '//td/div/button[@class="el-button el-button--text el-button--mini"]'
    # 删除按钮 索引1
    delete = '//td/div/button[@class="el-button el-button--text el-button--mini"]'
    '''
        新增、编辑页面元素
    '''
    # 用户名
    username = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # 密码
    password = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # 响应码
    status_code = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # 特征字符
    identify_key_word = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # URL
    url = '//div[@class="el-textarea"]/textarea'
    # 密码长度
    len = '//body//div[@class="el-input-number el-input-number--mini"]/div/input'

    # 加密方式  _1代表未加密 , _2 代表base64加密  ， _3代表md5加密
    #
    encrypt_type = '//body//section[@class="el-container is-vertical"]//div[@class="el-select"]/div[@class="el-input el-input--suffix"]'
    encrypt_type_1 = '//body/div[@class="el-select-dropdown el-popper"]//li[@class="el-select-dropdown__item"]/span[text()="未加密"]'
    encrypt_type_2 = '//body/div[@class="el-select-dropdown el-popper"]//li[@class="el-select-dropdown__item"]/span[text()="Base64"]'
    encrypt_type_3 = '//body/div[@class="el-select-dropdown el-popper"]//li[@class="el-select-dropdown__item"]/span[text()="MD5"]'
    update_encrypt_type_3 = '//body/div[@class="el-select-dropdown el-popper"]//li[@class="el-select-dropdown__item selected hover" or @class="el-select-dropdown__item selected" or @class="el-select-dropdown__item"]/span[text()="MD5"]'
    # 字母
    letter = '//span[@class="el-checkbox__input is-checked"]'
    # 大写字母
    upper = '//span[@class="el-checkbox__input is-checked"]'
    # 小写字母
    lower = '//span[@class="el-checkbox__input is-checked"]'
    # 数字
    num = '//span[@class="el-checkbox__input is-checked"]'
    # 特殊符号
    punctuation = '//span[@class="el-checkbox__input is-checked"]'
    # 其他情形——账号与密码相同
    name_pwd_equal = '//body//div[@class="el-form-item"]/div[@class="el-form-item__content"]//div/div[@class="el-switch is-checked"]'
    # 其他情形——连续字符检测
    continuous_char = '//body//div[@class="el-form-item"]/div[@class="el-form-item__content"]//div/div[@class="el-switch is-checked"]'
    # 名称
    name = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # 确定
    confirm = '//div[@class="el-form-item__content"]/button/span[text()="确认"]'
    # 取消
    close = '//div[@class="el-form-item__content"]/button/span[text()="取消"]'
    # 错误结果
    fail = "//body/div[@class='el-message el-message--error']/p"
    # 正确结果
    success = "//body/div[@class='el-message el-message--success']/p"
    '''
        列表页面元素
    '''
    search = '//div[@class="el-card__body"]/div//div[@class="vapp-input"]'
    # 索引值为0
    search_url = '//div[@class="el-scrollbar el-cascader-menu"]/div/ul/li"]'
    search_url_equal = '//li[@id="cascader-menu-3188-0-0"]'
    search_url_fuzzy = '//li[@id="cascader-menu-3188-0-1"]'
    # 索引值为1
    search_name = '//div[@class="el-scrollbar el-cascader-menu"]/div/ul/li"]'
    search_name_fuzzy = '//li[@id="cascader-menu-7591-0-0"]'
    # 输入框
    search_content = '//div[@class="el-input el-input--mini"]/input[@class="el-input__inner"]'
    # 确认按钮
    search_confirm = '//span[text()="保存"]'