pragma solidity ^0.5.0;

contract Class {
    struct Student {
        string name;
        uint id;
        string email;
        uint[4] assignments;
        uint finalExam;
    }
    Student[] public students;
    //initialized student with all grades
    function AddStudentWithGrades(string memory name, uint id,string memory email, uint assignment1,uint assignment2, uint assignment3,uint assignment4, uint finalExam) public {
        if(checkGrade(assignment1)&&checkGrade(assignment2)&&checkGrade(assignment3)&&checkGrade(assignment4)&&checkGrade(finalExam)){
            students.push(Student(name,id,email,[assignment1,assignment2,assignment3,assignment4],finalExam));    
        }
        else{
            revert('Wrong input for the grades! Each assignment or exam grade should be between 0 and 100');
        }
    }

    //adds a student without initializing their grades
    function AddStudentWithoutGrades(string memory name, uint id,string memory email) public{
        students.push(Student(name,id,email,[uint(0),0,0,0],0));
    }
    
    //assume user enters assignment number starting from 1
    function addAssignmentGrades(uint id, uint assignmentNumber, uint grade) public{
        uint i = find(id);
        if(checkGrade(grade) && assignmentNumber<=4 && assignmentNumber>=1){
            students[i].assignments[assignmentNumber-1]=grade;
        }
        else{
            revert('Wrong input!');
        }
    }
    
    function addExamGrade(uint id, uint grade) public{
        uint i = find(id);
        if(checkGrade(grade)){
            students[i].finalExam = grade;
        }
        else{
            revert('Wrong input for the grades! Each assignment or exam grade should be between 0 and 100');
        }
    }
    
    
    function read(uint id) view public returns(string memory, uint,string memory, uint256[4] memory,uint) {
        uint i = find(id);
        return(students[i].name, students[i].id,students[i].email,students[i].assignments,students[i].finalExam);
    }


    function updateAssignmentGrade(uint id, uint assignmentNumber, uint grade) public {
        uint i = find(id);
        students[i].assignments[assignmentNumber] = grade;
    }
    function updateExamGrade(uint id, uint grade) public {
        uint i = find(id);
        students[i].finalExam = grade;
    }

    function destroy(uint id) public {
        uint i = find(id);
        delete students[i];
    }
    
    function calculateWightedSum(uint id) view public returns(uint){
        uint i = find(id);
        uint sum =uint(0);
        for(uint j=0;j<4;j++){
            sum =sum + students[i].assignments[j];
        }
        sum =sum * uint(15);
        sum+= uint(40)*(students[i].finalExam);
        return sum/100;
    }
    function calculateLetterGrade(uint id) view public returns(string memory){
        uint numericGrade = calculateWightedSum(id);
        if(numericGrade>=90 && numericGrade<=100){
            return 'A';
        }
        else if(numericGrade>=80 ){
            return 'B';
        }
        else if(numericGrade>=70){
            return 'C';
        }
        else if(numericGrade>=60 ){
            return 'D';
        }
        else if(numericGrade <60){
            return 'F';
        }
        else{
            revert('Invalid Grade!');
        }
    }
    
    

    function find(uint id) view internal returns(uint) {
        for(uint i = 0; i < students.length; i++) {
            if(students[i].id == id) {
                return i;
            }
        }
        revert('User does not exist!');
    }
    
    function checkGrade(uint grade) pure internal returns(bool){
        if(grade>=0 && grade<=100){
            return true;
        }
        return false;
    }

}
