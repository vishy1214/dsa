package designguru.array;

public class FindingHighestAltitude {
    /*
    Given an array of integers representing a journey on a bike,
    wherein each number indicates a climb or descent in altitude,
    measured as a gain or loss of height.

    The rider starts at altitude 0 and determines the highest altitude
    the biker reaches at any point during the journey.
     */
    public int largestAltitude(int[] gain) {
        int maxAltitude = 0; // To store the maximum altitude encountered
        int sumOfLastTwo = 0;

        for(int i =0 ; i<gain.length;i++){
            if(i == 0){
                sumOfLastTwo = gain[i];
                maxAltitude = sumOfLastTwo;
            }else{
                //System.out.println(sumOfLastTwo+" + "+gain[i]+ "  < " +maxAltitude);
                sumOfLastTwo = sumOfLastTwo + gain[i];
                if(sumOfLastTwo > maxAltitude){
                    maxAltitude = sumOfLastTwo;
                }
            }
        }
        // System.out.println("~~~~~~~~~~");
        return maxAltitude>0?maxAltitude:0;
    }

    public static void main(String[] args){
        FindingHighestAltitude s = new FindingHighestAltitude();
        int[] case1 = {-5, 1, 5, 0, -7};
        int[] case2 = {4, -3, 2, -1, -2};
        int[] case3 = {2, 2, -3, -1, 2, 1, -5};
        int[] case4 = {-838, -981, 750, 232, -960};
        System.out.println("MaxAltitude: "+s.largestAltitude(case1));
        System.out.println("MaxAltitude: "+s.largestAltitude(case2));
        System.out.println("MaxAltitude: "+s.largestAltitude(case3));
        System.out.println("MaxAltitude: "+s.largestAltitude(case4));
    }
}
