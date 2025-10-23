#include <iostream>
#include <string>

class DoublyLinkedList{
    private:

        struct LinkedNode{                              // Defines node structure
            std::string arbitraryData;
            LinkedNode* next;
            LinkedNode* prev;
        };

        LinkedNode* head;                               // Defines the head & tail pointers
        LinkedNode* tail;

    public:

        DoublyLinkedList(){                             // Initialises head & tail to nullptr to avoid undefined behaviour
            head = nullptr;
            tail = nullptr;
        };

        void Prepend(std::string inputData){            // class method to prepend a node to the start of the LL
            LinkedNode* temp = new LinkedNode;          // creates new node and points temp to its memory address
            temp -> arbitraryData = inputData;          // takes the data input and writes it to the new node
            temp -> next = head;                        // points the new node's 'next' pointer to the old head node
            temp -> prev = nullptr;                     // this node will be the new head so there's no previous node to point to

            if (head != nullptr){                       // checks if the LL is empty 
                head -> prev = temp;                    // if the LL already has entries this points the old head node's prev pointer to the new node
            }
            else{
                tail = temp;                            // if the LL is empty then the new node becomes both head & tail of the LL
            };

            head = temp;                                // points the head pointer at the new node
        };

        void append(std::string inputData){             // class method to append a node to the end of the LL
            LinkedNode* temp = new LinkedNode;          // creates new node and points temp to its memory address
            temp -> arbitraryData = inputData;          // takes the data input and writes it to the new node
            temp -> next = nullptr;                     // this node will be the new tail so there's no next node to point to
            temp -> prev = tail;                        // points the new node's 'prev' pointer to the old tail node

            if (tail != nullptr){                       // checks if the LL is empty 
                tail -> next = temp;                    // if the LL already has entries this points the old tail node's next pointer to the new node
            }
            else{
                head = temp;                            // if the LL is empty then the new node becomes both head & tail of the LL
            };

            tail = temp;                                // points the tail pointer to the new node
        };
};

int main(){

};