package trait

class 特征_Example4 {
    static void main(String[] args) {
        Student st = new Student()
        st.StudentID = 1
        (st.DisplayMarks())
    }

    trait Marks {
        void DisplayMarks() {
            println("Marks1")
        }
    }

    trait Total extends Marks {
        void DisplayMarks() {
            println("Total")
        }
    }

    static class Student implements Total {
        int StudentID
    }
}
