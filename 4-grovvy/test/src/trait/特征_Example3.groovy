package trait

class 特征_Example3 {
    static void main(String[] args) {
        Student st = new Student()
        st.StudentID = 1

        (st.DisplayMarks())
        (st.DisplayTotal())
    }

    trait Marks {
        void DisplayMarks() {
            println("Marks1")
        }
    }

    trait Total {
        void DisplayTotal() {
            println("Total")
        }
    }

    static class Student implements Marks, Total {
        int StudentID
    }
}
