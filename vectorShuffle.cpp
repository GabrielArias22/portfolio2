#include <iostream>
#include<vector>
using namespace std;
#include <algorithm> // for shuffle
#include <random>    // for the random seed aspects
/**
* Name: Gabriel Arias 
* Program Name:Vector Lab Part 2
* Date: 5/18/26
* Extra: Vector Guessing with Shuffle
*/

int main()
{
     random_device rd; // randomizing seed
     mt19937 e(rd());
    int guess;
    vector<string> pets = {"gizmo","peaches"}; //set up string vector
       pets.insert(pets.begin()+1,"squeaky"); //insert a value into the middle which is +1 cause there's only two elements
    for (auto itr = pets.begin(); itr != pets.end(); ++itr){ //loop through the vector's values and print them one by one
        cout << *itr << endl;
    }
    pets.erase(pets.begin()+1); // remove the middle value with the same type of logic
    cout << "\n";
     for (auto itr = pets.begin(); itr != pets.end(); ++itr){ //another loop 
        cout << *itr << endl;
    }
    shuffle(pets.begin(), pets.end(), e); //goes through the vector and shuffles it according to e which is a randomizer declared at the top
    cout << "guess which one is gizmo 1,2,3" << endl;
    cin >> guess; //user input
    if(pets[guess-1]=="gizmo"){ //puts the user's guess into the index of the vector and has to subtract one since three values are just 0 1 2
        cout << "yay you won" << endl;
    } else{ // else in case you got it wrong
        cout << "better luck next time" << endl;
    }
    return 0;
}