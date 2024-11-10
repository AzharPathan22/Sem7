//Bank Solidity
pragma solidity >=0.8.2 <0.9;

contract Bank{
    uint256 Balance;

    function Deposit(uint256 value) public {
        Balance= Balance+ value;
    }

    function Withdraw(uint256 value) public {
        Balance= Balance- value;
    }

    function Show() public view returns(uint256) {
        return (Balance);
    }
}

------------------------------------

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) balances;
    
    function depositMoney(uint256 amount) public {
        require(amount >= 0, "Amount must be greater than 0");
        balances[msg.sender] = balances[msg.sender] + amount;
    }
    
    function withdrawMoney(uint256 amount) public {
        require(amount <= balances[msg.sender], "Insufficient Balance");
        balances[msg.sender] = balances[msg.sender] - amount;
    }
    function showBalance() public view returns(uint256)
    { 
        return balances[msg.sender];
    }
}