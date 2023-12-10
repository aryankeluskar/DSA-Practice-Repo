import java.util.*;

public class hashmaps {
   public static void main(String[] args) {
      HashMap<String, String[]> city_maps = new HashMap<>();
      // java craves knowing which data type is being reffered, classic java typed
      // hashmaps vs maps: Map is interface but HashMap is class

      city_maps.put("Canada", new String[] { "Vancouver", "Toronto", "Ottawa" });
      city_maps.put("Canada", new String[] { "Vancouver", "Toronto" });
      city_maps.put("America", new String[] { "DC", "NYC" });
      city_maps.put("Bhutan", new String[] { "Thimphu" });
      city_maps.put("Bangladesh", new String[] { "Dhaka" });

      System.out.println(Arrays.toString(city_maps.get("Canada")));
      System.out.println(city_maps.containsKey("Canada"));

   }
}