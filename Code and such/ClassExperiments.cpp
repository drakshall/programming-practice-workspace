#include <iostream>
#include <string>

class User{
    public:
        std::string firstName;
        std::string lastName;
        int age;

        User(std::string f, std::string l, int a): firstName(f), lastName(l), age(a){
        };

        void sayHello(){
            std::cout << "Hello, ",firstName;
        };
}; 

int main(){
    std::cout << "Hello World!" << std::endl;
};