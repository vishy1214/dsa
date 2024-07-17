package arrays;


public class MyArrayUsage {
    public static void main(String[] args){
        MyArray myArray = new MyArray(20);
        myArray.get(1);
        myArray.insert(1234);
        myArray.insert(345);
        myArray.insert(44444);
        System.out.println(myArray.delete(1234));
        myArray.traverse();

    }
}
