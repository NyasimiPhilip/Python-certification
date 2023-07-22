    <h1>Budget Category Class</h1>
    <h1 style="text-align: center;">Budget Category Class</h1>
    <p>
        The Budget Category Class allows you to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class has an instance variable called ledger that is a list. The class also contains the following methods:
    </p>
    <ul>
        <li>
            <code>deposit(amount, description)</code>: This method accepts an amount and description. If no description is given, it defaults to an empty string. The method appends an object to the ledger list in the form of {"amount": amount, "description": description}.
        </li>
        <li>
            <code>withdraw(amount, description)</code>: This method is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing is added to the ledger. This method returns True if the withdrawal took place, and False otherwise.
        </li>
        <li>
            <code>get_balance()</code>: This method returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        </li>
        <li>
            <code>transfer(amount, destination_category)</code>: This method accepts an amount and another budget category as arguments. The method adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. This method returns True if the transfer took place, and False otherwise.
        </li>
        <li>
            <code>check_funds(amount)</code>: This method accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method is used by both the withdraw method and transfer method.
        </li>
    </ul>
    <p>
        When the budget object is printed it should display:
    </p>
    <p>
        A title line of 30 characters where the name of the category is centered in a line of * characters.
    </p>
    <p>
        A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right-aligned, contain two decimal places, and display a maximum of 7 characters.
    </p>
    <p>
        A line displaying the category total.
    </p>

