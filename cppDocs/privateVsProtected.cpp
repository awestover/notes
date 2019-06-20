#include <iostream>
class Animal {
	private:
		int y;
	protected:
		int x;
	public:
		Animal(int x_ = 7, int y_ = 1){
			x= x_;
			y = y_;
		};
		int getY(){
			return y;
		}
};

class Bear : Animal {
	public:
		void pX(){
			std::cout << x << std::endl;
		}
		void pY(){
			// ACTUALLY cout ing y doesn't work cuz y is a private field of Animal
			std::cout << "y"  << std::endl;
			// but we could do
			std::cout << getY() << std::endl;
		}
};

int main(){
	Bear b;
	b.pX();
	b.pY();
	return 0;
}
