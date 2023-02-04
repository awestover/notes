import java.util.*;

public class B extends HashSet {
  int[] loc = new int[2];
  public B(int x, int y){
    loc[0] = x; loc[1] = y;
  }
  public int getX(){return loc[0]; }
  public int getY(){return loc[1]; }

  // public boolean equals(B other){
  //   return (other.getX() == loc[0] && other.getY() == loc[1]);
  // }

  public int hashCode() {
    return 60*loc[0] + loc[1];
  }

  public void print(){
    System.out.println(loc[0] + "; " +loc[1]);
  }
}

