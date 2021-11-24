class Person {
    // クラスの下で変数を定義（インスタンス変数）
    String name
    int age
    int height

    // クラス内のメソッドからもアクセスできる（staticメソッドからはアクセスできません。下記参照。）
    public void checkInfo() {
        System.out.print("名前は" + name + "、")
        System.out.print("年齢は" + age + "、")

        if(age < 20) {
            System.out.print("未成年。")
        }

        System.out.println("身長は" + height + " です。")
    }
}


class Main {
    public static void main(String args[]) {
        Person tanaka = new Person()
        // newキーワードでオブジェクトを生成

        tanaka.name = "田中"
        // オブジェクト（インスタンス）を代入した変数名tanakaで、インスタンス変数nameに値を代入している
        tanaka.age = 19
        // // オブジェクトを代入した変数名tanakaで、インスタンス変数ageに値を代入している

        System.out.println(tanaka.name)
        // 田中
        System.out.println(tanaka.age)
        // 19

        // ↓ローカル変数は宣言・初期化を行わなければならなかったが、
        // インスタンス変数は自動で初期化される。
        System.out.println(tanaka.height)
        // 0

        tanaka.checkInfo()
        // 名前は田中、年齢は19、未成年。身長は0 です。


        Person suzuki = new Person()
        // newキーワードでオブジェクトを生成

        suzuki.name = "鈴木"
        // オブジェクトを代入した変数名suzukiで、インスタンス変数nameに値を代入している
        suzuki.age = 51
        // オブジェクトを代入した変数名suzukiで、インスタンス変数ageに値を代入している
        suzuki.height = 146
        // オブジェクトを代入した変数名suzukiで、インスタンス変数heightに値を代入している

        System.out.println(suzuki.name)
        // 鈴木
        System.out.println(suzuki.age)
        // 51
        System.out.println(suzuki.height)
        // 146

        suzuki.checkInfo()
        // 名前は鈴木、年齢は51、身長は146 です。
    }
}

