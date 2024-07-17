import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QuickSort {

    /**
     * Create 3 arraylist
     * take the mid value as the pivot
     * break the incoming list into 3 array by comparing the array value with the pivot
     * add the left & right array recursively.
     */
    private List<Integer> quickSort(List<Integer> list){
        ArrayList<Integer> sorted = new ArrayList<>();

        if(list.size() == 0){
            return sorted;
        }
        int pivot = list.get(list.size() / 2);  // THIS IS THE KEY STEP - very similar to binary search, we need to pick the mid value.
        List<Integer> left = new ArrayList<>();
        List<Integer> mid = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for(Integer x : list){
            if(x < pivot) left.add(x);
            if(x > pivot) right.add(x);
            if(x == pivot) mid.add(x);
        }

        sorted.addAll(quickSort(left));
        sorted.addAll(mid);
        sorted.addAll(quickSort(right));

        return sorted;
    }

    public static void main(String[] args){
        List<Integer> inputList = Arrays.asList(3,5,1,6,2,9,4,7,10);
        QuickSort qs = new QuickSort();
        for (Integer i : qs.quickSort(inputList)) {
            System.out.print(" "+i);
        }
    }
}
