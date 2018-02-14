class TheMain {
    static void main(String[] args) {
//        获取文件的根目录
        def rootFiles = new File("").listRoots()
        rootFiles.each {
            file -> println file.absolutePath
        }
//        获取用户目录下的所有文件列表
        new File("/home/archermind").eachFile() {
            file->println file.getAbsolutePath()
        }
//        递归获取指定目录下的文件
        new File("/home/archermind/tmp").eachFileRecurse() {
            file -> println file.getAbsolutePath()
        }

//        def sng = new Song(name: "Le Freak", artist: "Chic", genre: "Disco")
//        sng.name = "Funky"
//        sng.setName("Funkytown")
//        println("name:" + sng.name + " artist:" + sng.getArtist() + "  gemre:" + sng.getGenre())
//
//        sng.artist = null
//        println(sng)
//        println(sng.getArtist())
//        sng.artist?.toUpperCase()
//        println(sng.getArtist()?.toUpperCase())
//
//        println(sng)    //如果没有override toString方法那么就输出hashcode, 否则隐示调用toString方法
//        println(sng.toString())
//        assert sng.getArtist() == "Lipps Inc."
//
//      ===========================
//      =          闭包            =
//      ===========================
//        println excite("gabs")  //闭包的调用
//        println excite.call("gabs") //闭包的调用
//        assert "Java!!" == excite.call("Java")    //断言判断
//        acoll.each {  //闭包方法输出list元素
//            println it
//        }
//
//        hash.each { key, value ->
//            println "${key} : ${value}"
//        }
//
//        "ITERATION".each {
//            println it.toLowerCase()
//        }
//
//      ===========================
//      =        方法定义          =
//      ===========================
//        String val = "Hello Worldss"
//        repeat(val, 3)
//        repeat("foo")
//        println val.class
    }

    static def acoll = ["Groovy", "Java", "Ruby"]

    static def hash = [name: "Andy", "VPN-#": 45]

//  名为 excite 的闭包。这个闭包接受一个参数（名为 word），返回的 String 是 word 变量加两个感叹号
    static def excite = { word ->
        return "${word}!!"
    }

    static def repeat(String val, int repeat = 5) {
        for (i in 0..<repeat) {
            println val
        }
    }

    static class Song {
        def name
        def artist
        def genre

        String toString() {
            "${name}, ${artist}, ${genre}"
        }

        String getGenre() {
            genre.toUpperCase()
        }

        String getArtist() {
            artist?.toLowerCase()   //在变量后添加?等同于if(artist != null) {...} else { return null}
        }
    }
}
