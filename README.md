# sast2023 word game

## 环境配置

```

langdetect~=1.0.9

```

## 使用设置

约定以下参数：

```
--choose    -c  接所选文章的标题，必选
--file      -f  接文章的路径，默认为随机抽取
--language  -l  无后缀，控制是否限制输入语言与文章语言相同，默认为无限制
--save      -s  接输出路径，默认为输出到屏幕

```

文章使用 JSON 存储，格式如下：

```

{
    "language": "language",
    "articles": [
        {
            "title": "title",
            "article": "我们都爱{{1}}这门课程。这门课程是多么的{{2}}，以至于...",
            "hints": ["hint1", "hint2", ...]
        },
        { ... },
        ...
    ]
}

```

## 游戏功能

基础功能：启动、读取、输入、替换、显示。\
拓展功能：\
&emsp;1. todo:图形化\
&emsp;2. 鲁棒性\
&emsp;3. 语言限制\
&emsp;4. 输出到txt

