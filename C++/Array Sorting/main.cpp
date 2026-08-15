#include <iostream>

using namespace std;

void print_array(int arr[], int arr_size){
    for (int i = 0; i < arr_size; i++){
        if (i == 0){
            cout << "{" << arr[i];
        }
        else if (i == arr_size - 1){
            cout << ", " << arr[i] << "}\n";
        }
        else{
            cout << ", " << arr[i];
        }
    }   
}
void sort(int arr[], int arr_size){
    for (int x = 0; x < arr_size; x++){
        int min_number = arr[x];
        int min_number_index = x;
        for (int y = x + 1; y < arr_size; y++){
            if (arr[y] < min_number){
                min_number = arr[y]; 
                min_number_index = y;
            }
        }
        arr[min_number_index] = arr[x];
        arr[x] = min_number;
        
    }  
}
int main(){
    const int arr_size = 5;
    int arr[arr_size] = {5, 2, 8, 1, 4};

    sort(arr, arr_size);
    
    print_array(arr, arr_size);

}