package arrays;

public class MyArray {
    private int[] nArray;
    private int nSize;
    public MyArray(int initialSize){
        this.nArray =  new int[initialSize];
    }

    public int get(int index){
        return this.nArray[index];
    }

    public void insert(int item){
        this.nArray[this.nSize] = item;
        this.nSize +=1;
    }

    public boolean delete(int item){
        for(int x=0;x < this.nSize;x++){
            if(this.nArray[x] == item){
                for(int y=x;y<this.nSize;y++){
                    this.nArray[y] = this.nArray[y+1];
                }
                this.nSize -= 1;
                return true;
            }
        }
        return false;
    }

    public void traverse(){
        for(int x : this.nArray){
            if(x!=0) {
                System.out.print(x);
            }
        }
    }
}
