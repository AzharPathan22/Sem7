//Stud Database
pragma solidity ^0.8.0;

contract StudentDB{

    struct Student{
        string name;
        uint256 rollno;
        string class;
    }

    Student[] private students;

    function addStudent(string memory name, uint256 rollno, string memory class) public {
        students.push(Student(name, rollno, class));
    }

    function getStudById(uint256 id) public view returns(string memory, uint256 , string memory class){
        require(id<=students.length, "Student does not exist in DB");
        return(students[id].name, students[id].rollno, students[id].class);
    }
    function getTotal() public view returns(uint256){
        return students.length;
    }
}