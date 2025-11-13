#include <iostream>
#include <string>

class DoublyLinkedList{
    private:

        struct LinkedNode{                                                          // defines node structure
            std::string arbitraryData;
            LinkedNode* next;
            LinkedNode* prev;
        };

        LinkedNode* head;                                                           // defines the head & tail pointers
        LinkedNode* tail;

    public:

        DoublyLinkedList(){                                                         // initialises head & tail to nullptr to avoid undefined behaviour
            head = nullptr;
            tail = nullptr;
        };

        void Prepend(std::string inputData){                                        // class method to prepend a node to the start of the LL
            LinkedNode* tempPointer = new LinkedNode;                               // creates new node and temporarily points to its memory address
            tempPointer -> arbitraryData = inputData;                               // takes the data input and writes it to the new node
            tempPointer -> next = head;                                             // points the new node's 'next' pointer to the old head node
            tempPointer -> prev = nullptr;                                          // this node will be the new head so there's no previous node to point to

            if (head != nullptr){                                                   // checks if the LL is empty 
                head -> prev = tempPointer;                                         // if the LL already has entries this points the old head node's prev pointer to the new node
            }
            else{
                tail = tempPointer;                                                 // if the LL is empty then the new node becomes both head & tail of the LL
            };

            head = tempPointer;                                                     // points the head pointer at the new node
        };

        void Append(std::string inputData){                                         // class method to append a node to the end of the LL
            LinkedNode* tempPointer = new LinkedNode;                               
            tempPointer -> arbitraryData = inputData;                               
            tempPointer -> next = nullptr;                                          // this node will be the new tail so there's no next node to point to
            tempPointer -> prev = tail;                                             // points the new node's 'prev' pointer to the old tail node

            if (tail != nullptr){                                                   // checks if the LL is empty 
                tail -> next = tempPointer;                                         // if the LL already has entries this points the old tail node's next pointer to the new node
            }
            else{
                head = tempPointer;                                                 // if the LL is empty then the new node becomes both head & tail of the LL
            };

            tail = tempPointer;                                                     // points the tail pointer to the new node
        };

        void Insert(std::string inputData, int tempIndex, bool forwardBackward){    // method to insert a node at a specific position in the LL
            LinkedNode* tempPointer = new LinkedNode;                               
            tempPointer -> arbitraryData = inputData; 

            switch(forwardBackward){
                case 1:

                case 0:

                default:
                std::cout << "debug - invalid input";
                break;
            }
        };

        void Search(std::string inputData, bool forwardBackward){

        };
};

int main(){

};