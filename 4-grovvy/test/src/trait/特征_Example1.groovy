package trait

class 特征_Example1 {
    static void main(String[] args) {
        Student st = new Student()
        st.StudentID = 1
        st.Marks1 = 10

        st.DisplayMarks()
        st.DisplayTotal()
    }

    interface Total {
        void DisplayTotal()
    }

    trait Marks implements Total {
        void DisplayMarks() {
            println("Display Marks")
        }

        void DisplayTotal() {
            println("Display Total")
        }
    }

    static class Student implements Marks {
        int StudentID
        int Marks1
    }
}
