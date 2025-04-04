"""
test.py - Example Python file to test Sphinx documentation generation.

This module includes a sample function and class to demonstrate how
Sphinx can generate documentation from docstrings.
"""

def add(a, b):
    """
    Adds two numbers together.

    Parameters
    ----------
    a : int or float
        First number to add.
    b : int or float
        Second number to add.

    Returns
    -------
    int or float
        The sum of the two numbers.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(10.5, 5)
    15.5
    """
    return a + b


class Calculator:
    """
    A simple calculator class to demonstrate Sphinx autodoc functionality.

    Methods
    -------
    add(a, b)
        Adds two numbers.
    subtract(a, b)
        Subtracts the second number from the first.
    """

    def add(self, a, b):
        """
        Adds two numbers.

        Parameters
        ----------
        a : int or float
            First number to add.
        b : int or float
            Second number to add.

        Returns
        -------
        int or float
            The sum of the two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Parameters
        ----------
        a : int or float
            First number.
        b : int or float
            Second number to subtract.

        Returns
        -------
        int or float
            The result of subtraction.
        
        Examples
        --------
        >>> calc = Calculator()
        >>> calc.subtract(10, 4)
        6
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Parameters
        ----------
        a : int or float
            First number.
        b : int or float
            Second number to multiply.

        Returns
        -------
        int or float
            The result of multiplication.
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divides the first number by the second.

        Parameters
        ----------
        a : int or float
            First number.
        b : int or float
            Second number to divide by.

        Returns
        -------
        int or float
            The result of division.
        """
        return a / b
    
    def power(self, a, b):
        """
        Raises the first number to the power of the second.

        Parameters
        ----------
        a : int or float
            Base number.
        b : int or float
            Exponent.

        Returns
        -------
        int or float
            The result of exponentiation.
        """
        return a ** b
    
