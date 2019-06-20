
#include <iostream>
#include <string>

class Animal {
	private: 
		int x;
		void pX();
	protected:
		int y;
		void pY();
	public:
		int z;
		Animal(int x, int y, int z);
		void pZ();
		void speak(std::string s);
};

Animal::Animal(int x, int y, int z){
	this->x = x;
	this->y = y;
	this->z = z;
}
void Animal::pX(){
	std::cout << x << std::endl;
}
void Animal::pY(){
	std::cout << y << std::endl;
}
void Animal::pZ(){
	std::cout << z << std::endl;
	pX();
	pY();
}
void Animal::speak(std::string s){
	std::cout << "absolutely not! Animals don't say " << s << std::endl;
}


// this is a subclass of Animal
class Giraffe : public Animal {

};
// throws an error
// void Giraffe::speak(std::string s){
//     std::cout << "ima giraffee so im not gonna say "  << s << std::endl;
// }

class Bear : public Animal {
	public:
		void speak();
};
void Bear::speak(){
	std::cout << "growl growl growl"  << std::endl;
}


int main() {
	// Animal a; // throws an error you need arguments!
	// a.pX(); a.speak("yo");
	Animal aa(1,2,3);
	aa.pZ(); aa.speak("yo");

	// Bear b;
	// b.pZ(); b.speak();
	Bear *bb = (Bear*)(new Animal(3,4,5));
	bb->pZ(); bb->speak();

	Giraffe *g = (Giraffe*)(new Animal(1,2,3));
	g->speak("test");

	return 0;
}

