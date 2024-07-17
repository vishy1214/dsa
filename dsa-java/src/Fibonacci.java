

public class Fibonacci {
    private int fibonacci(int n){
        if(n == 0){
            return 0;
        }else if(n == 1){
            return 1;
        }
        return fibonacci(n-1) + fibonacci(n-1);
    }
    public static void main(String[] args){
        int n = 10;
        Fibonacci fb = new Fibonacci();
        System.out.println(fb.fibonacci(n));
    }
}
