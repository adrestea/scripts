package trait

class 特征_Example2 {
    static void main(String[] args) {
        Student st = new Student()
        st.StudentID = 1

        st.DisplayMarks()
        st.DisplayTotal()

    }

    interface Total {
        void DisplayTotal()
    }

    trait Marks implements Total {
        int Marks1

        void DisplayMarks() {
            this.Marks1 = 10
            println(this.Marks1)
        }

        void DisplayTotal() {
            println("Display Total")
        }
    }

    static class Student implements Marks {
        int StudentID
    }
}
