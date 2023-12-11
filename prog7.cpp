/*Assignment 7, Student Records
Kien Le - KL23A
COP 3363 - Section 1
*/

#include <iostream>
#include <iomanip>
#include <fstream>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

//structure declaration
struct Student{
    string lastName;
    string firstName;
    char course;
    int test1;
    int test2;
    int final;
    double average;
};
//function prototypes
void readRecords(int &noOfRecords, Student *&students, const string infilename);
void calculateAverage(Student *students, int noOfRecords);
char scoreToGrade(double average);
void sortStudents(Student *students, int noOfRecords);
void outputReport(Student *students, int noOfRecords, ofstream &outp);


int main(){
    string infilename, outfilename;

    ifstream inp;
    ofstream outp;
    do{
        inp.clear();
        cout << "Please enter the name of the input file.\n";
        cout << "Filename: ";
        cin >> infilename;
        inp.open(infilename.c_str());
        if(!inp){
            cout << "Invalid file. Try again!\n";
        }
    }
    while(!inp);
    //dynamically allocate memory for students array
    Student* students;
    int noOfRecords = 0;
    students = new Student[noOfRecords];

    readRecords(noOfRecords, students, infilename);

    calculateAverage(students, noOfRecords);

    do{
        outp.clear();	
        cout << "Please enter the name of the output file.\n";
        cout << "Filename: ";
        cin >> outfilename;
        outp.open(outfilename.c_str());
        if(!outp){
            cout << "Invalid file. Try again!\n";
        }
    } 
    while(!outp);
    //print the grade summary to the output file    
    outputReport(students, noOfRecords, outp);

    delete[] students; //clean up dynamically allocated memory

    inp.close();
    outp.close();

    return 0;    
}

//function declaration
void readRecords(int &noOfRecords, Student *&students, const string infilename){
    ifstream inp;
    inp.open(infilename.c_str());
    char c;
    inp >> noOfRecords; //read the number of records
    
    students = new Student[noOfRecords];
    for(int i = 0; i < noOfRecords; i++){
        getline(inp, students[i].lastName, ',');
        getline(inp, students[i].firstName, ',');
        inp >> students[i].course >> c >> students[i].test1 >> c >>students[i].test2 >> c 
        >> students[i].final;
        
    }
    inp.close();
}
void calculateAverage(Student *students, int noOfRecords){
    for(int i = 0; i < noOfRecords; i++){
        students[i].average = 0.3 * students[i].test1
        + 0.3 * students[i].test2 + 0.4 * students[i].final;
    }
}
char scoreToGrade(double average){
    if(average >= 90)
        return 'A';
    else if(average >= 80) 
        return 'B';
    else if(average >= 70) 
        return 'C';
    else if(average >= 60) 
        return 'D';
    else 
        return 'F';
}
void sortStudents(Student *students, int noOfRecords){
    for(int i = 0; i < noOfRecords - 1; i++){
        for(int j = 0; j < noOfRecords - i - 1; j++){
            if(students[j].course > students[j + 1].course){
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}
void outputReport(Student *students, int noOfRecords, ofstream &outp){
    sortStudents(students, noOfRecords);    //sort students by course
    //initialize variables for class averages
    double eng_total = 0.0, his_total = 0.0, math_total = 0.0;
    int eng_count = 0, his_count = 0, math_count = 0;

    //iterate through sorted students and print the summary
    outp << "Student Grade Summary\n";
    outp << "---------------------\n";

    for(int i = 0; i < noOfRecords; i++){
        //determine the class of the student
        string className;
        switch(students[i].course){
            case 'E':
                className = "ENGLISH CLASS";
                eng_total += students[i].average;
                eng_count++;
                break;
            case 'H':
                className = "HISTORY CLASS";
                his_total += students[i].average;
                his_count++;
                break;
            case 'M':
                className = "MATH CLASS";
                math_total += students[i].average;
                math_count++;
                break;
            default:
                className = "UNKNOWN CLASS";
        }

        //print class header if it's the first student of the class
        if(i == 0 || students[i].course != students[i - 1].course){
            outp << "\n" << className << "\n\n";
            outp << "Student Name                             Test Avg\n";
            outp << "----------------------------------------------------------------\n";
        }
        
        //print student info
        outp << students[i].firstName << " " << students[i].lastName
             << setw(34) << fixed << setprecision(2) << students[i].average
             << "\t" << scoreToGrade(students[i].average) << "\n";

        //if it's the last student in the class then print that class average
        if(i == noOfRecords - 1 || students[i].course != students[i + 1].course){
            double classTotal, classAverage;
            int classCount;

            //calculate class-specific totals and averages
            switch(students[i].course){
                case 'E':
                    classTotal = eng_total;
                    classCount = eng_count;
                    break;
                case 'H':
                    classTotal = his_total;
                    classCount = his_count;
                    break;
                case 'M':
                    classTotal = math_total;
                    classCount = math_count;
                    break;
                default:
                    classTotal = 0.0;
                    classCount = 0;
            }

            //calculate and print the class average
            if(classCount > 0){
                classAverage = classTotal / classCount;
                outp << "\n\t\t\t\tClass Average" << setw(20) << classAverage;
            }

            outp << "\n" << "----------------------------------------------------------------\n";
        }
    }

}