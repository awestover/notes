#include <limits.h>
#include <queue>
#include <iostream>

void pQ(std::priority_queue<int> q){
	while(!q.empty()){
		std::cout << q.top() << " ";
		q.pop();
	}
	std::cout << std::endl;
}

int main(){
	std::cout << INT_MAX << std::endl;
	std::priority_queue<int> q;

	int n = 7;
	int nums[] = {1,2,3,4,10,9,INT_MAX};

	for (int i = 0; i < n; i++) {
		q.push(nums[i]);
	}

	pQ(q);
	pQ(q);

	return 0;
}
