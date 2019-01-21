pragma solidity ^0.4.24;
import "./SafeMath.sol";


/**
 * The contractName contract does this and that...
 */
contract Token {
    using SafeMath for uint256;
	event Transfer(
		address indexed _form,
		address indexed _to,
		uint256 _value
		);

	event Approval(
			address indexed _owner,
			address indexed _spender,
			uint256 _value
		);


	mapping(address => uint256) public balanceOf;
	mapping(address => mapping (address => uint256)) public allowance;


//	function DappToken (uint256 _intialSupply) public {
//		balanceOf[msg.sender] = _intialSupply;
//		totalSupply = _intialSupply;
//		//allocate the intial supply
//
//	}

	//Transfar
	function transfer(address _to,uint256 _value) public returns (bool success){
    // Exception if account does not enough

    require(balanceOf[msg.sender] >= _value);
    // Transfar the balance
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;

	// Transfar Event
	emit Transfer(msg.sender,_to,_value);

	// Return a boolean
	return true;
	}

	// approve
	function approve(address _spender,uint256 _value) public returns (bool success){
		//allowence
		allowance[msg.sender][_spender] = _value;

		// Approve event
		emit Approval(msg.sender,_spender,_value);
             return true;

	}

    // transfer form
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= balanceOf[_from]);
        require(_value <= allowance[_from][msg.sender]);
        // change the balance
        balanceOf[_from] -= _value;

        //update the balance
       balanceOf[_to] += _value;

       allowance[_from][msg.sender] -= _value;

       emit Transfer(_from,_to,_value);


        return true;
    }

     function increaseApproval(address _spender, uint256 _addedValue) public returns (bool) {
        allowance[msg.sender][_spender] = (allowance[msg.sender][_spender].add(_addedValue));
        emit Approval(msg.sender, _spender, allowance[msg.sender][_spender]);
        return true;
    }

    function decreaseApproval(address _spender, uint256 _subtractedValue) public returns (bool) {
        uint256 oldValue = allowance[msg.sender][_spender];
        if (_subtractedValue >= oldValue) {
          allowance[msg.sender][_spender] = 0;
        } else {
          allowance[msg.sender][_spender] = oldValue.sub(_subtractedValue);
        }
        emit Approval(msg.sender, _spender, allowance[msg.sender][_spender]);
        return true;
    }

}

