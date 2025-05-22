10年毕业，直到18年基本都在一线研发，18~21年做团队管理，参与各个角色的工作，21年开始带PM团队直到现在；

也不知道是code血脉开始翻腾，还是最近对AI的兴趣导致技术无法回避，突然感觉还是喜欢Coding；

遂决定：

花两个月的时间复习编程技能，学习新的AI技术，成为一个合格的AI研发。在这里整理我的学习计划和进展，鞭策自己！！！8月见！！！

## 学习计划
### 第一阶段：基础夯实（第1-4周）
1. Python快速上手（第1周）
- 重点：语法差异、数据科学库、函数式编程  
- 任务：  
  - 用Python实现Java项目中的常用功能（如多线程、文件操作）  
  - 掌握NumPy（数组操作）、Pandas（数据处理）、Matplotlib（可视化）  
  - 学习装饰器、生成器、lambda表达式等Python特性  

2. 数学基础补全（第2周）
- 重点：线性代数（矩阵运算）、概率论（贝叶斯定理）、微积分（梯度）  
- 资源：  
  - 《机器学习数学基础》（简明版）  
  - 3Blue1Brown《线性代数的本质》视频  

3. 机器学习核心（第3-4周）
- 算法学习：  
  - 监督学习：线性回归、逻辑回归、决策树、随机森林  
  - 无监督学习：K-means、PCA降维  
  - 评估指标：准确率、召回率、F1-score、AUC-ROC  
- 实战项目：  
  - 使用Scikit-learn完成一个完整的分类项目（如鸢尾花分类）  
  - Kaggle入门赛：泰坦尼克号生存预测  


### 第二阶段：深度学习与实战（第5-8周）
1. 深度学习框架（第5-6周）
- 框架选择：PyTorch（入门友好）或TensorFlow  
- 学习路径：  
  - 神经网络基础（激活函数、反向传播）  
  - 卷积神经网络（CNN，图像任务）  
  - 循环神经网络（RNN/LSTM，序列任务）  
- 实战项目：  
  - 用PyTorch实现手写数字识别（MNIST数据集）  
  - 搭建简单的图像分类模型（CIFAR-10）  

2. 自然语言处理（NLP）或计算机视觉（CV）方向（第7周）
- 根据兴趣选择：  
  - NLP：词向量（Word2Vec）、Transformer架构、文本分类  
  - CV：目标检测（YOLO）、图像分割（U-Net）  
- 项目实践：  
  - 情感分析（IMDB影评数据集）  
  - 人脸识别（FaceNet）  

3. 特定Topic强化（第8周）
- 过拟合/欠拟合的解决方法  
- 梯度下降与优化器（SGD、Adam）  
- 模型评估与交叉验证  

## 学习进展
### 2025-05-21
####
1. 多线程、文件操作（multi-thread.py）
- with关键字：
  - 代码更清晰简洁，避免手动写`try...finally`。
  - 简化资源管理的操作，确保资源在使用后能够被正常释放（即便是代码块发生异常，资源也会被释放），
  - 可应用的场景比较多，比如：多线程、文件操作、数据库操作、锁操作等等；
  - 工作原理：依赖对象的`__enter__()`和`__exit__()`方法：
    - 在进入with代码块时，enter方法被调用，返回资源对象；
    - 在离开with代码块时，exit方法被调用，释放资源对象；
  - 举例：
  ```python
   # 写入文件
  with open(filename, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
  ```
  ```python
  # 创建线程池，最大线程数为5
  with ThreadPoolExecutor(max_workers=5) as executor:
    # 提交所有下载任务
    futures = [executor.submit(download_image, url) for url in IMAGE_URLS]
        
    # 获取所有任务的结果
    results = [future.result() for future in futures]
  ```
2. 列表推导式（List Comprehension）
- 说明
  ```python
  # expression：对每个元素执行的操作，如item * 2
  # item：迭代变量，表示可迭代对象中的每个元素
  # iterable：可迭代对象，如列表、元组、字符串等
  [expression for item in iterable]
  ```
- 示例
  ```python
  # 传统写法
  square = []
  for x in [1,2,3,4]
    squares.append(x**2)
  print(squares) # 输出：[1,4,9,16]

  # 列表推导式
  squares = [x**2 for x in [1,2,3,4]]
  print(squares) # 输出：[1,4,9,16]
  ```
3. f-string，格式化字符串字面量（Formatted String Literal）
- 说明

  Python 3.6及以上版本引入的语法糖，支持嵌入表达式，包括变量、函数、数学运算、格式化、对齐填充等；
- 示例
  ```python
  name = "Zhangsan"
  age = 30
  height = 187.237
  print(f"Name:{name},Age:{30+1},Height:{height:.2f}")
  ```
4.流式下载文件，并存储到本地
- 代码
  ```python
  def download_image(url):
    """下载单个图片的函数"""
    try:
        # 获取图片文件名
        filename = f'downloads/image_{url.split("=")[-1]}.jpg'
        
        # 发送HTTP请求
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        # 写入文件
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        print(f"下载完成: {filename}")
        return filename
        
    except Exception as e:
        print(f"下载失败 {url}: {e}")
        return None
  ```
- 解析
  - `url.split("=")[-1]`：根据字符串`=`分割成列表，取最后一个元素
  - `request.get(url, stream=True)`：代表流式获取文件，降低内存消耗，尤其是读取大文件时
  - `response.raise_for_status`：安全检查机制，检查http响应的状态码，如果是200~299，则会继续执行，否则会抛出异常
  - `for chunk in response.iter_content(chunk_size=8192)`：在流式读取文件时，以8192字节（8k）的数据库大小进行读取下载
5. 多线程
- 代码
  ```python
    # 创建线程池，最大线程数为5
    with ThreadPoolExecutor(max_workers=5) as executor:
      # 提交所有下载任务
      futures = [executor.submit(download_image, url) for url in IMAGE_URLS]
          
      # 获取所有任务的结果
      results = [future.result() for future in futures]
  ```
- 解释  
  `with`：确保线程池在使用完后被正确关闭，避免代码块发生异常时线程池未正确关闭；
  `ThreadPoolExecutor(max_workers=5) as executor`：创建最大线程数为5的线程池
  `futures = [executor.submit(download_image, url) for url in IMAGE_URLS]`：列表推导式，生成5个Future对象
  `future.result()`：线程的执行是`executor.submit()`方法触发的，`future.result()`方法只是阻塞在这里等待结果返回

