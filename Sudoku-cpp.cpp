#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

struct Node{
    int row;
    int col;
    int value = 1;
    Node *next;
    Node *prev;
};

class LinkedList{
    private:
        Node *head;
        Node *tail;
        int size = 0;
        
    public:
        LinkedList(){
            head = NULL;
            tail = NULL;
        }
    
    void addNode(int val, int r, int c){
        Node *tmp = new Node;
        tmp->value = val;
        tmp->row = r;
        tmp->col = c;
        tmp->next = NULL;
        tmp->prev = NULL;
        
        if(head == NULL){
            head = tmp;
            tail = tmp;
            tmp = NULL;
        } else{
            tail->next = tmp;
            tmp->prev = tail;
            tail = tmp;
        }
    }
    
    void printLinkedList(){
        Node *tmp = head;
        while(tmp != NULL){
            cout << "[" << tmp->row << ", " << tmp->col << "]" << endl;
            tmp = tmp->next;
        }
    }
    
    Node* getHead(){
        return head;
    }
};

bool checkRow(int n, vector<int> row){
    for(int i = 0; i < row.size(); i++){
        if(n == row[i]){
//            cout << "Check row failed" << endl;
            return false;
        }
    }
    return true;
}

bool checkCol(int n, vector<vector<int>> board, int col){
    for(int i = 0; i < board.size(); i++){
        if(n == board[i][col]){
//            cout << "Check col failed" << endl;
            return false;
        }
    }
    return true;
}

bool checkSquare(int n, vector<vector<int>> board, int row, int col){
    int rowMin = (row/3)*3;
    int colMin = (col/3)*3;
    for(int i = rowMin; i < rowMin+3; i++){
        for(int j = colMin; j < colMin+3; j++){
            if(board[i][j] == n){
//                cout << "Check square failed" << endl;
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char * argv[])
{

    fstream fs(argv[1], std::fstream::in);

    vector< vector<int> > values;
    int temp = 0;
    LinkedList *empties = new LinkedList();

    for(int i = 0; i < 9; i++)
    {
        vector<int> row;
        values.push_back(row);

        for(int j = 0; j < 9; j++)
        {
            fs >> temp;
            if(temp == 0){
                empties->addNode(temp, i, j);
            }
            values[i].push_back(temp);
        }
    }
    
    fs.close();
//    empties->printLinkedList();

    Node *currentNode = empties->getHead();
    while(currentNode != NULL){
        int row = currentNode->row;
        int col = currentNode->col;
        int tmpVal = currentNode->value;
        if(checkCol(tmpVal, values, col) && checkRow(tmpVal, values[row]) && checkSquare(tmpVal, values, row, col)){
            currentNode = currentNode->next;
//            cout << tmpVal << endl;
            values[row][col] = tmpVal;
        } else{
            if(tmpVal < 9){
                currentNode->value++;
            } else{
                currentNode->value = 1;
                currentNode = currentNode->prev;
                values[row][col] = 0;
            }
        }
    }
    for(int i = 0; i < values.size(); i++){
        for(int j = 0; j < values[0].size(); j++){
            cout << values[i][j];
        }
        cout << endl;
    }
    return 0;
}