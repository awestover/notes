import java.util.*;

public class A {
  public static void main(String[] args){
    HashSet<B> bs = new HashSet<B>();
    bs.add(new B(10,5));
    bs.add(new B(10,50));
    bs.add(new B(10,5));
    System.out.println(bs.contains(new B(10,5)));

    for (B boi : bs) {
      boi.print();
    }

    HashSet<Integer> z = new HashSet<Integer>();
    z.add(100);
    z.add(100);
    z.remove(0);
    for (int zz : z) {
     System.out.println(zz);
    }

    Vector<Integer> v = new Vector<Integer>();
    v.add(100);
    v.remove(0);

    System.out.println(v.size());
  }
}

