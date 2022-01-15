**网站架构已基本设计完成，已经在线部署（10.17）**

#网站基本结构
##界面结构（10.20更新）

- [x] /:主界面 开始按钮，进行测试
- [x] /basic:用户信息采集表
- [x] /test:标注测试页面
- [x] /welcome:welcome to our lab.
- [x] /forms:用户表单填写页面
    基本完成表单填写、提交、表单验证、数字转字符串并存储数据库的功能
- [x] /model:重定向到test页面

```
###########目录结构描述
├── Readme.md                   // help
├── app.py                      // 应用
├── requirements                // 环境依赖
├── 城市感知实验策划书            // 网站设计规章
├── utils                     	// 各种辅助方法类
│   ├── UserForm.py				      // 用户表单类
│   ├── SaveDateBase.py         // 数据存储方法，包括表单数据与评估数据
│   └── ProcessData.py        	// 对于数据格式转换以及数据保存读取等操作
│   └── ImagesSetTools.py       // 随机化备选图片夹工具
│   └── init_db.py              // 数据库图片信息初始化
├── templates                   // 提供给前端的配置，html文件
│   ├── index.html				      // welcome，网站门户
│   ├── welcome.html 			      // 一次评估结束之后的再选择页面
│   ├── page_form.html			    // 用户表单forms
│   └── image_test.html			    //图片评估测试界面       			
├── static                      // web静态资源加载
│   └── css						// 提供给前端的配置，CSS样式表
│       └── pagestytle1.css     // /welcome页面
│       └── pagestytle2.css     // 图片/test页面（预览）
│       └── pagestytle-3.css    // 提示奖励页面（暂时未涉及）
│       └── form.css     		// *forms页面
│       └── test_style.css      //  测试界面使用的css
│   └── images		            //其他界面的图片
│   └─data_set_test             //数据集目录，图片放此处
│	└─js	                    //js脚本放此目录下




