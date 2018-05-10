# Introduction
#### 社会信息检索作业，实现了以下三个小功能：

(1)计算文档TF-IDF值

(2)计算句子相似度 (內积、向量夹角余弦值、Jaccard值)

(3)简易搜索引擎

使用了python Flask框架，前端语言为HTML和JavaScript

## Operation method

#### 工程文件在Windows下和Linux下都可以运行

#### 需要安装的有：

(1) python 2.7

(2) python库 (jieba, numpy, scipy, scikit-learn)

#### 可以通过两种方式运行工程文件：

(1) 使用 Pycharm 打开social information工程，运行\_\_init\_\_.py 文件

(2) 使用命令行进入social information文件夹,输入

```bash
$python __init__.py runserver
```

#### 运行成功后，输入127.0.0.1:5000即可访问

## Function description

### 1 TF-IDF

使用python库：结巴分词对文档进行分词后，统计词语在现有语料库中的TF值和IDF值

则词语(A)的TF-IDF值为：

$$ TF(A)=词语在文章中的出现次数 $$

$$ IDF(A)=\frac{词语在文章中出现次数}{文章总词数 } $$

$$ TFIDF(A)=TF(A)*IDF(A) $$

### 2 SIM

对输入的句子进行分词，构建向量空间，向量空间的维数为两个句子中的词语的种类数。求出两个句子对应的向量$$ V_a $$和$$ V_b $$

#### 向量点积: 

$$ product=V_a*V_b $$

#### 夹角余弦值:

 $$ cos =\frac{product}{|V_a|*|V_b|} $$

#### Jaccard: 

$$ jac = \frac{V_a\bigcap V_b}{V_a \bigcup V_b} $$

