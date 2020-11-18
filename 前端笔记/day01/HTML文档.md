## 什么是HTML(Hyper Text Markup Language)
- 用来描述网页的一种语言
    - 超文本标记语言
    - HTML不是一种编程语言,而是一种标记语言,类似json
    - 标记语言是一套标记标签(markup tag)
    - HTML文档包含了HTML标签及文本内容
    - HTML文档也叫做web页面
    
## HTML 是干嘛的
- 可以用HTML来建立自己的WEB站点, HTML运行在浏览器上, 由浏览器来解析

## 建立HTML文件
- .html
- .htm

## HTML注释
- 见范例01

## HTML基本结构
- 见范例01

## 通用声明
- <!DOCTYPE html>

## HTML标签结构
- HTML标记通常被称为HTML标签(HTMLtag)
    - 通常是尖括号包围的关键词
    - 通常是成对出现
    - <开始标签>内容</结束标签>
    
## HTML元素
- HTML标签和HTML元素通常都是描述同样的意思, 一个HTML元素包含了开始标签和结束标签

## HTML 属性
- HTML可以设置属性
- 一般添加在开始标签
- 一般是键值对的形式,
- 注意:
    - 属性值必须用双引号
    - 标签都用小写字母
    - 双标签必须又结束标签

## HTML常用标签
### 一 HTML常用的块级标签(块级元素)

> 独占一行

#### 有语义的html块级元素
> 有默认样式

#### 标题(Heading)
> 通过h1~h6来定义的

#### 段落
> 通过标签p来定义

#### 列表
- 无序列表ul,li
> 是一个项目的列表, 列项目使用粗体圆点进行标记

- 有序列表 ol,li
> 也是一个项目的列表, 列表项目使用数字进行标记

- 自定义列表dl,dt,dd(了解)
- 注意:列表内部可以使用段落, 换行符, 图片, 链接以及其他列表等

#### 表格 table tr td
- table 常用属性
    - border 边框
    - cellpadding 内容距离表框的距离
    - cellspacing 单元格和单元格之间的距离
    - rowspan 垂直合并(跨行显示)
    - colspan 水平和并(跨列显示)
    - align 内容水平对齐方式
    - valign 内容垂直对齐方式
    
    
### 无语义的块级元素 div
`
<div>元素没有特定的含义.除此之外,由于他属于块级元素,浏览器会在他前后显示换行.
一般和CSS一同使用
<div>元素的另一个常见的用途是文档布局.它取代了使用表格定义布局的老式方法.
`

## HTML的常用行级标签(行内元素)
- 不独占一行

###有语义的行内元素

#### HTML链接 a标签
`<a href="链接地址">链接文本</a>`
- target属性,定义被链接的文档在哪里显示_blank新窗口打开

#### HTML图像
`<img src="图片地址" alt="">`

#### 文本标签
- b 标签 i strong em

### 无语义的行内元素
- span标签 配合CSS使用

## 常用的实体字符
- gt;lt;copy

## 表单标签
- 表单是一个包含表单元素的区域.通过form来定义表单区域
> 通过type属性定义不同类型的表单控件    
- text 
- password 
- radio 
- checked 
- select 
- file 
- textarea 
- submit 
- reset  
- hidden 
































































