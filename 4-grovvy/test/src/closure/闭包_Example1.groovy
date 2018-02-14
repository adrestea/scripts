package closure

class 闭包_Example1 {
    static void main(String[] args) {
        new closure_use5().doMain()
        new closure_use4().doMain()
        new closure_use3().doMain()
        new closure_use2().doMain()
        new closure_use1().doMain()
        closure1.call()
        closure2.call()
        closure3.call()
    }

    static class closure_use5 { //遍历集合的成员，并且仅当元素满足一些标准时应用一些逻辑
        def doMain() {
            def lst = [1, 2, 3, 4];
            lst.each { println it }
            println("The list will only display those numbers which are divisible by 2")
            lst.each { num -> if (num % 2 == 0) println num }
        }
    }

    static class closure_use4 { //集合和字符串中的闭包:使用映射闭包
        def doMain() {
            def mp = ["TopicName": "Maps", "TopicDescription": "Methods in Maps"]
            mp.each { println it }
            mp.each { println "${it.key} -----maps to ---->: ${it.value}" }
        }
    }

    static class closure_use3 { //集合和字符串中的闭包:使用闭包和列表
        def doMain() {

            def lst = [11, 12, 13, 14]
            lst.each {
                println it
            }
        }
    }

//    在方法中使用闭包
    static class closure_use2 {
        def Display(clo) {
            // This time the $param parameter gets replaced by the string "Inner"
            clo.call("Inner")
        }

        def doMain() {
            def str1 = "Hello"
            def clos = { param -> println "${str1} ${param}" }
            clos.call("World")

            // We are now changing the value of the String str1 which is referenced in the closure
            str1 = "Welcome"
            clos.call("World")

            // Passing our closure to a method
            this.Display(clos)
        }
    }

//    闭包和变量
    static class closure_use1 {
        def doMain() {

            def str1 = "Hello"
            def clos = { param -> println "${str1} ${param}" }
            clos.call("World")

            // We are now changing the value of the String str1 which is referenced in the closure
            str1 = "Welcome"
            clos.call("World")

        }
    }

    static def closure3 = {
//        下一个图重复了前面的例子并产生相同的结果，但显示可以使用被称为它的隐式单个参数。这里的'it'是Groovy中的关键字。
        def clos = { println "Hello ${it}" }
        clos.call("World")
    }

    static def closure2 = {
//        注意使用$ {param}，这导致closure接受一个参数。当通过clos.call语句调用闭包时，我们现在可以选择将一个参数传递给闭包
        def clos = { param -> println "Hello ${param}" }
        clos.call("World")
    }

    static def closure1 = {
        def clos = { println "Hello World" }
        clos.call()
    }
}