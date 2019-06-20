// friend functions and classes have the ability to access privaate and protected fields of the class that they are a friend to


class Node 
{ 
private: 
  int key; 
  Node *next; 
  /* Other members of Node Class */
  
  friend class LinkedList; // Now class  LinkedList can  
                           // access private members of Node 
}; 

//*******************************************************************************************************************
// partial friend function example

class NodeP
{ 
private: 
  int key; 
  NodeP *next; 
  
  /* Other members of NodeP Class */
  friend int LinkedList::search(); // Only search() of linkedList  
                                  // can access internal members 
}; 



//*******************************************************************************************************************
// friend class example
#include <iostream> 
class A { 
private: 
    int a; 
public: 
    A() { a=0; } 
    friend class B;     // Friend Class 
}; 
  
class B { 
private: 
    int b; 
public: 
    void showA(A& x) { 
        // Since B is friend of A, it can access 
        // private members of A 
        std::cout << "A::a=" << x.a; 
    } 
}; 
  
int main() { 
   A a; 
   B b; 
   b.showA(a); 
   return 0; 
} 



//*******************************************************************************************************************
// global friend function
#include <iostream> 
class A 
{ 
    int a; 
public: 
    A() {a = 0;} 
    friend void showA(A&); // global friend function 
}; 
  
void showA(A& x) { 
    // Since showA() is a friend, it can access 
    // private members of A 
    std::cout << "A::a=" << x.a; 
} 
  
int main() 
{ 
    A a; 
    showA(a); 
    return 0; 
}
