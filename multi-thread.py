import threading
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time, sleep
import os

# 创建保存图片的目录
os.makedirs('downloads', exist_ok=True)

# 模拟需要下载的图片URL列表
IMAGE_URLS = [
    f'https://picsum.photos/200/300?random={i}' for i in range(10)
]

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

def single_thread_download():
    """单线程下载示例"""
    print("开始单线程下载...")
    start_time = time()
    
    for url in IMAGE_URLS:
        download_image(url)
    
    print(f"单线程下载完成，耗时: {time() - start_time:.2f}秒")

def multi_thread_download():
    """多线程下载示例"""
    print("\n开始多线程下载...")
    start_time = time()
    
    # 创建线程池，最大线程数为5
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 提交所有下载任务
        futures = [executor.submit(download_image, url) for url in IMAGE_URLS]
        
        # 获取所有任务的结果
        results = [future.result() for future in futures]
    
    print(f"多线程下载完成，耗时: {time() - start_time:.2f}秒")

def thread_safety_demo():
    """线程安全问题演示"""
    print("\n线程安全问题演示...")
    
    class Counter:
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()  # 创建锁对象
        
        def increment_unsafe(self):
            """非线程安全的自增方法"""
            self.value += 1
        
        def increment_safe(self):
            """线程安全的自增方法"""
            with self.lock:  # 使用锁保护共享资源
                self.value += 1
    
    def worker(counter, method):
        for _ in range(1000000):
            method()
    
    # 测试非线程安全的计数器
    unsafe_counter = Counter()
    threads = [
        threading.Thread(target=worker, args=(unsafe_counter, unsafe_counter.increment_unsafe))
        for _ in range(10)
    ]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"非线程安全计数器预期结果: 100000，实际结果: {unsafe_counter.value}")
    
    # 测试线程安全的计数器
    safe_counter = Counter()
    threads = [
        threading.Thread(target=worker, args=(safe_counter, safe_counter.increment_safe))
        for _ in range(10)
    ]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"线程安全计数器预期结果: 100000，实际结果: {safe_counter.value}")

if __name__ == "__main__":
    # 1. 单线程下载
    single_thread_download()
    
    # 2. 多线程下载
    multi_thread_download()
    
    # 3. 线程安全演示
    thread_safety_demo()