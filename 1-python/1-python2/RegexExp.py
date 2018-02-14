#!/usr/bin/python
#coding=utf-8
import re

'''
python中正则表达式的使用
reference：http://www.jb51.net/article/15707.htm
'''

'''
提取
'''
def refine_reg():
    p = re.compile('\d+')
    print p.findall(r'12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

'''
匹配
'''
def match():
    p = re.compile("strings*")
    m = p.match( 'string goes here' )
    if m:
        print 'Match found: ', m.group()
    else:
        print 'No match'

if __name__ == '__main__':
    refine_reg()







'''
元字符：. ^ $ * + ? { [ ] \ | ( ) 使用反斜杠"\"取消元字符的意义
[a-c]匹配a-c中任意一个，[^5]：为不匹配5
\d  匹配任何十进制数；它相当于类 [0-9]
\D  匹配任何非数字字符；它相当于类 [^0-9]
\s  匹配任何空白字符；它相当于类  [ "t"n"r"f"v]
\S  匹配任何非空白字符；它相当于类 [^ "t"n"r"f"v]
\w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]
\W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
.   匹配除换行符之外的任何字符
|   可选匹配，优先级很低，Crow|Servo 将匹配"Crow" 或 "Servo"
^   匹配行首。除非设置 MULTILINE 标志，它只是匹配字符串的开始。在 MULTILINE 模式里，它也可以直接匹配字符串中的每个换行。
$   匹配行尾，行尾被定义为要么是字符串尾，要么是一个换行字符後面的任何位置。


重复：
*  匹配零次或多次
+  匹配一或多次
?  匹配一次或零次
{m,n}  重复限定符，至少有 m 个重复，至多到 n 个

RegexObject` 实例有一些方法和属性：
match()	决定 RE 是否在字符串刚开始的位置匹配
search()	扫描字符串，找到这个 RE 匹配的位置
findall()	找到 RE 匹配的所有子串，并把它们作为一个列表返回
finditer()	找到 RE 匹配的所有子串，并把它们作为一个迭代器返回
如果没有匹配到match() 和 search() 将返回None，如果成功会返回`MatchObject` 实例

MatchObject实例也有几个方法和属性，在实际程序中，最常见的作法是将`MatchObject` 保存在一个变量里，然后检查它是否为 None，最重要的那些如下所示：
group()	返回被RE匹配的字符串
start()	返回匹配开始的位置
end()	返回匹配结束的位置
span()	返回一个元组包含匹配 (开始,结束) 的位置


不一定要产生`RegexObject`对象然後再调用它的方法，re模块也提供了顶级函数调用如 match()、search()、sub() 等等。这些函数使用 RE 字符串作为第一个参数，而後面的参数则与相应 `RegexObject` 的方法参数相同，返回则要么是 None 要么就是一个 `MatchObject` 的实例。
>>> print re.match(r'From"s+', 'Fromage amk')
>>> re.match(r'From"s+', 'From amk Thu May 14 19:12:10 1998')

如果一个 RE 在代码中只做用一次的话，那么模块级函数也许更方便。如果程序包含很多的正则表达式，或在多处复用同一个的话，那么将全部定义放在一起，在一段代码中提前编译所有的 REs 更有用：
ref = re.compile("")
entityref = re.compile("")
charref = re.compile("")
starttagopen = re.compile("")

可用标志表:
标志		含义
DOTALL, S	使 . 匹配包括换行在内的所有字符
IGNORECASE, I	使匹配对大小写不敏感
LOCALE, L	做本地化识别（locale-aware）匹配,影响 "w, "W, "b, 和 "B"
MULTILINE, M	多行匹配，影响 ^ 和 $
VERBOSE, X	能够使用 REs 的 verbose 状态，使之被组织得更清晰易懂
locales 是 C 语言库中的一项功能，是用来为需要考虑不同语言的编程提供帮助的。举个例子，如果你正在处理法文文本，你想用 "w+ 来匹配文字，但 "w 只匹配字符类 [A-Za-z]；它并不能匹配 "é" 或 "ç"。如果你的系统配置适当且本地化设置为法语，那么内部的 C 函数将告诉程序 "é" 也应该被认为是一个字母。当在编译正则表达式时使用 LOCALE 标志会得到用这些 C 函数来处理 "w 後的编译对象；这会更慢，但也会象你希望的那样可以用 "w+ 来匹配法文文本。

IGNORECASE
使匹配对大小写不敏感；字符类和字符串匹配字母时忽略大小写。举个例子，[A-Z]也可以匹配小写字母，Spam 可以匹配 "Spam", "spam", 或 "spAM"。这个小写字母并不考虑当前位置。

LOCALE
影响 "w, "W, "b, 和 "B，这取决于当前的本地化设置。
locales 是 C 语言库中的一项功能，是用来为需要考虑不同语言的编程提供帮助的。举个例子，如果你正在处理法文文本，你想用 "w+ 来匹配文字，但 "w 只匹配字符类 [A-Za-z]；它并不能匹配 "é" 或 "ç"。如果你的系统配置适当且本地化设置为法语，那么内部的 C 函数将告诉程序 "é" 也应该被认为是一个字母。当在编译正则表达式时使用 LOCALE 标志会得到用这些 C 函数来处理 "w 後的编译对象；这会更慢，但也会象你希望的那样可以用 "w+ 来匹配法文文本。

MULTILINE
(此时 ^ 和 $ 不会被解释; 它们将在 4.1 节被介绍.)

使用 "^" 只匹配字符串的开始，而 $ 则只匹配字符串的结尾和直接在换行前（如果有的话）的字符串结尾。当本标志指定後， "^" 匹配字符串的开始和字符串中每行的开始。同样的， $ 元字符匹配字符串结尾和字符串中每行的结尾（直接在每个换行之前）。
S
DOTALL
使 "." 特殊字符完全匹配任何字符，包括换行；没有这个标志， "." 匹配除了换行外的任何字符。

VERBOSE
该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。当该标志被指定时，在 RE 字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之後；这可以让你更清晰地组织和缩进 RE。它也可以允许你将注释写入 RE，这些注释会被引擎忽略；注释用 "#"号 来标识，不过该符号不能在字符串或反斜杠之後。


贪婪：
.* 的本质是“贪婪”的
>>> s = '<html><head><title>Title</title>'
>>> print re.match('<.*>', s).span()
(0, 32)
>>> print re.match('<.*>', s).group()
<html><head><title>Title</title>
RE 匹配 在 "<html>" 中的 "<"，.* 消耗掉子符串的剩馀部分。在 RE 中保持更多的左，虽然 > 不能匹配在字符串结尾，因此正则表达式必须一个字符一个字符地回溯，直到它找到 > 的匹配。最终的匹配从 "<html" 中的 "<" 到 "</title>" 中的 ">",这并不是你所想要的结果。


不贪婪：
>>> print re.match('<.*?>', s).group()
解决方案是使用不贪婪的限定符 *?、+?、?? 或 {m,n}?，尽可能匹配小的文本
'''