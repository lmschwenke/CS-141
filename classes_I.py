{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"http://www.cs.wm.edu/~rml/images/wm_horizontal_single_line_full_color.png\">\n",
    "\n",
    "# CSCI 141, Fall 2016"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The <code>import</code> statement\n",
    "\n",
    "You have seen the <code>import</code> statement in a recent assignment, where you imported the pseudo-random number generator function <code>randint()</code> from the <code>random</code> module."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from random import randint\n",
    "\n",
    "print(randint(42, 54))\n",
    "print(randint(0, 7))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We must import modules before we can use them.\n",
    "\n",
    "The <code>import</code> statement gives us a way of accessing Python code in other files.  For instance, the <code>math</code> module (standard in Python) contains a function named <code>log2()</code> that computes the base-2 logarithm of its input.\n",
    "\n",
    "If we try to call <code>log2</code> before we have imported the <code>math</code> module, we get an error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "print(log2(32))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Observe the syntax for accessing the function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "print(math.log2(32))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that we need to indicate that <code>log2()</code> comes from the <code>math</code> module.  The following doesn't work, even though <code>math</code> has been imported."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "print(log2(32))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Anaconda software collection includes [a lot of modules](https://docs.continuum.io/anaconda/pkg-docs) (sometimes called packages).\n",
    "\n",
    "Later we will look at variations on <code>import</code>, but for now we have the syntax we need to start using modules."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The main program\n",
    "\n",
    "In a Python file, all the commands that are not in functions are implicitly in the **main program**.\n",
    "\n",
    "Statements in the main program are automatically executed, as illustrated by the following example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def funyun():\n",
    "    print('boo!')\n",
    "\n",
    "def bunyun():\n",
    "    print('foo!')\n",
    "\n",
    "# The stuff that follows is the main program.\n",
    "print('Hello from the main program!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Interaction between main and import\n",
    "\n",
    "When we import a Python module, if there are statements in the main program then they will be executed.\n",
    "\n",
    "Let's take a look at the file <code>bar.py</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# The following is a Jupyter notebook magic command,\n",
    "# not a Python statement.\n",
    "%pycat bar.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's import the contents of the file as a module.  To do so, we use the name of the file without the suffix \".py\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import bar"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Observe that the statements in the main program in bar.py were executed as part of the importation.\n",
    "\n",
    "In general, this is anti-social behavior in a module that is imported, especially if the commands are <code>print</code> statements or debugging code."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Safeguarding the main program\n",
    "\n",
    "There are two approaches you can use to avoid this behavior.\n",
    "\n",
    "1. You can encapsulate your main program as a function named, say, <code>main</code>.  This means that an explicit call to the function is needed to execute the main program.\n",
    "2. The second approach (which you still need to fully implement the first), is more fun because it introduces a cryptic <code>if</code> statement to test whether you are in the main program at the time of execution.\n",
    "\n",
    "This is illustrated in foo.py."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%pycat foo.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note the test\n",
    "\n",
    "<pre>\n",
    "if (__name__ == \"__main__\"):\n",
    "</pre>\n",
    "\n",
    "This checks at runtime whether we are in the main program.\n",
    "\n",
    "With this test foo.py will be silent when we import it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import foo"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Safeguard your main programs in your code!\n",
    "\n",
    "We will use <code>import</code> to import your code our test programs.  If you do not safeguard your main program, this may break our test programs and cause them to report your code failed!\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# More on modules\n",
    "\n",
    "We can look at the contents of a module using the <code>dir()</code> and <code>help()</code> functions. <code>dir()</code> simply returns a list of the items contained in the module. <code>help()</code> prints information about the module similar to what you would find in the [Python3 documentation](https://docs.python.org/3/library/math.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "dir(math)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "help(math)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Object-oriented programming and classes\n",
    "\n",
    "Object-oriented programming (OOP) is a common approach to software development.\n",
    "\n",
    "The idea is to create objects that encapsulate both *data* (variables), and *methods*, which are functions that act on the object's variables.\n",
    "\n",
    "Together a class' variables and methods are call the *class attributes*."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python is inherently object-oriented\n",
    "\n",
    "Python strings are a good example of object-oriented programming.\n",
    "\n",
    "The data of a string are the characters that make up the string.\n",
    "\n",
    "The methods of a string are the various functions that can act on the string's characters.  [A complete list](https://docs.python.org/3/library/stdtypes.html#string-methods) string methods can be found in the Python documentation.  Here we illustrate two string methods."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "poem = 'THE WOMBAT\\n' +\\\n",
    "       'by Ogden Nash\\n' +\\\n",
    "       'The wombat lives across the seas,\\n'+\\\n",
    "       'Among the far Antipodes.\\n'+\\\n",
    "       'He may exist on nuts and berries,\\n'+\\\n",
    "       'Or then again, on missionaries;\\n'+\\\n",
    "       'His distant habitat precludes\\n'+\\\n",
    "       'Conclusive knowledge of his moods,\\n'+\\\n",
    "       'But I would not engage the wombat\\n'+\\\n",
    "       'In any form of mortal combat.\\n'\n",
    "\n",
    "# The lower method converts the string to lower case.\n",
    "print(poem.lower())\n",
    "\n",
    "# The upper methods converts the string to upper case.\n",
    "# This is useful for letters to the editor and ransom notes.\n",
    "print(poem.upper())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# A bank account class\n",
    "\n",
    "Let's design a class named BankAccount that represents a bank account.  We begin with the elements of data and the operations that form the abstraction of a bank account. For example, a bank account has:\n",
    "\n",
    "* an account number, and\n",
    "* an account balance.\n",
    "\n",
    "These will be the data stored in the class object.\n",
    "\n",
    "You must perform certain operations on a bank account:\n",
    "\n",
    "* create an object for each bank account;\n",
    "* deposit money;\n",
    "* withdraw money;\n",
    "* generate a statement.\n",
    "\n",
    "These define the methods of the class."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Class definition\n",
    "\n",
    "Here is a minimal working class."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    pass # Something has to be here!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The keyword <code>class</code> indicates that this is a class definition.  This is followed by the name of the class, which must follow the same rules as variables names.  In most popular programming languages, the convention is to capitalize each word in the class name (including the first). Finally, there is the <code>(object)</code>; this is **parent class** of the <code>BankAccount</code> class.  We will discuss parent classes later in detail, but for now if suffices to know that this part of the definition ensures that <code>BankAccount</code> inherits all the default pieces of a class.\n",
    "\n",
    "Now let's see what's under the hood.  The <code>dir</code> function will display the attributes of our class."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "dir(BankAccount)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 'Zounds!  Where did all that stuff come from?\n",
    "\n",
    "We haven't put anything in our class yet, so where did all these methods come from?\n",
    "\n",
    "The methods were inherited by <code>BankAccount</code> from <code>object</code>."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating an instance of the class\n",
    "\n",
    "The class definition is just a template for the object.  We must bring particular **instances** of the object into being ourselves.  This is called **instantiation**.\n",
    "\n",
    "We do this by calling a class **constructor**, which is done by invoking the class name as if it were a function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "my_first_class = BankAccount()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "dir(my_first_class)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Instances of a class are just variables\n",
    "\n",
    "We can have multiple instances of the same class, in the same way we can have multiple instances of the integer type, the float type, etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "my_second_class = BankAccount()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can look at our active variables using the built-in Python command <code>whos</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "whos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note how <code>whos</code> differentiates between <code>BankAccount</code>, which is a type of class, and <code>my_first_class</code>, which is an instance of a <code>BankAccount</code> object."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Our first method\n",
    "\n",
    "Now let's add a method to <code>BankAccount</code>.  Methods are functions, with one twist---they always have a special argument which by universal convention is called <code>self</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    def bark (self):\n",
    "        print('arf!  arf!  arf!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will explain <code>self</code> in just a second.  We can call the method <code>bark</code> as follows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# I'm tired of long variable names.\n",
    "b = BankAccount()\n",
    "b.bark()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The class constructor\n",
    "\n",
    "So far, <code>BankAccount</code> doesn't really do anything.  Let's give the user the option to initialize the account balance to a nonzero amount.\n",
    "\n",
    "The class constructor, which is called whenever an instance of the class is created, is a method with the special name \n",
    "\n",
    "<pre>\n",
    "\\__init__\n",
    "</pre>\n",
    "(two underscores before and after)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    def __init__(self, initial_balance):\n",
    "        self.balance = initial_balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b = BankAccount(42)\n",
    "print(b.balance)\n",
    "c = BankAccount(54)\n",
    "print(c.balance)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Let's unpack this\n",
    "\n",
    "When an object calls one its methods, Python automatically maps the first parameter of the method to the object that is calling the method.  That is, an object always implicitly passes itself to its methods!\n",
    "\n",
    "Hence the name <code>self</code>: when we initialize the account balance for <code>b</code>, we need to pass <code>b</code> to the constructor, which sets the balance in account <code>b</code> to <code>initial_balance</code>.\n",
    "\n",
    "So the statement\n",
    "\n",
    "<pre>\n",
    "b = BankAccount(42)\n",
    "</pre>\n",
    "\n",
    "really looks more like the function call \n",
    "\n",
    "<pre>\n",
    "__init__(b, 42)\n",
    "</pre>\n",
    "\n",
    "In so doing, we are initializing an attribute of the class, namely, <code>balance</code>.\n",
    "\n",
    "We can then examine this attribute with the syntax <code>b.balance</code>."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Modifying the constructor\n",
    "\n",
    "Besides the initial balance, we need to enter the account number when we create a new account.  Let's change the constructor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    def __init__(self, account_number, initial_balance):\n",
    "        self.account_number = account_number\n",
    "        self.balance = initial_balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b = BankAccount(1234, 42)\n",
    "print(b.account_number, b.balance)\n",
    "c = BankAccount(5678, 54)\n",
    "print(c.account_number, c.balance)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question\n",
    "Why can have both a parameter and an instance variable called <code>account_number</code>? The same question applies to <code>balance</code>."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Adding utility functions\n",
    "\n",
    "Rather than let people directly access the data inside a <code>BankAccount</code> object, we'll create helper functions that will mediate between users and the object.\n",
    "\n",
    "For instance, let's add a method named <code>balance</code> that returns the balance in the account.  To avoid collision with the variable that stores the balance, we'll rename the latter to be <code>__balance</code>.  The double underscore is also a convention to let users not to access this attribute directly.\n",
    "\n",
    "We'll do the same for <code>account_number</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    def __init__(self, account_number, initial_balance):\n",
    "        self.__account_number = account_number\n",
    "        self.__balance = initial_balance\n",
    "        \n",
    "    def account_number(self):\n",
    "        return self.__account_number\n",
    "    \n",
    "    def balance(self):\n",
    "        return self.__balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b = BankAccount(1234, 42)\n",
    "print(b.account_number(), b.balance())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Finishing BankAccount\n",
    "\n",
    "Remember that in our design, a bank account has:\n",
    "\n",
    "* an account number, and\n",
    "* an account balance.\n",
    "\n",
    "We also wish to perform certain operations:\n",
    "\n",
    "* create an object for each bank account;\n",
    "* deposit money;\n",
    "* withdraw money;\n",
    "* generate a statement.\n",
    "\n",
    "We will also create a function named <code>__str__</code> which will allow us to convert a <code>BankAccount</code> into a string, say, for the purposes of printing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "class BankAccount (object):\n",
    "    def __init__(self, account_number, initial_balance):\n",
    "        self.__account_number = account_number\n",
    "        self.__balance = initial_balance\n",
    "        \n",
    "    def __str__(self):\n",
    "        s = 'account no.: ' + str(self.__account_number)\\\n",
    "          + '\\n'\\\n",
    "          + 'balance: $' + str(self.__balance)\n",
    "        return s\n",
    "    \n",
    "    def balance(self):\n",
    "        return self.__balance\n",
    "    \n",
    "    def account_number(self):\n",
    "        return self.__account_number\n",
    "    \n",
    "    def deposit(self, amount):\n",
    "        self.__balance = self.__balance + amount\n",
    "        \n",
    "    def withdraw(self, amount):\n",
    "        self.__balance = self.__balance - amount\n",
    "        \n",
    "    def statement(self):\n",
    "        print('Statement for account no.', self.account_number())\n",
    "        print('Your current balance is: $' + str(self.balance()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b = BankAccount(1234, 42)\n",
    "b.statement()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b.deposit(54)\n",
    "b.statement()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b.withdraw(40)\n",
    "b.statement()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(str(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b.deposit(3.27)\n",
    "b.statement()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(str(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Another example of a class\n",
    "\n",
    "Here is another example.  It stores information about animals in a zoo:\n",
    "\n",
    "* the animal's individual name,\n",
    "* the animal's common name,\n",
    "* the animal's zoological name, and\n",
    "* the animal's diet.\n",
    "\n",
    "There are also utility functions that allow us to access this information."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Animal (object):\n",
    "    def __init__(self, individual, common_name, latin_name, diet):\n",
    "        self.__individual  = individual\n",
    "        self.__common_name = common_name\n",
    "        self.__latin_name  = latin_name\n",
    "        self.__diet        = diet\n",
    "        \n",
    "    def __str__(self):\n",
    "        s = self.__individual + ' is a ' + self.__common_name\\\n",
    "            + ' (' + self.__latin_name + ').  Its diet is primarily '\\\n",
    "            + self.__diet + '.'\n",
    "        return s\n",
    "    \n",
    "    def diet(self):\n",
    "        return self.__diet\n",
    "    \n",
    "    def common_name(self):\n",
    "        return self.__common_name\n",
    "    \n",
    "    def latin_name(self):\n",
    "        return self.__latin_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "harry_buffalo = Animal('Harry', 'American buffalo', 'Bison bison', 'grass')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(str(harry_buffalo))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "rocky_squirrel = Animal('Rocky',\\\n",
    "                        'Eastern gray squirrel',\\\n",
    "                        'Sciurus carolinensis',\\\n",
    "                        'apple cores, pizza crusts, and other assorted garbage')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "print(str(rocky_squirrel))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "wally_wombat = Animal('Wally',\\\n",
    "                      'Common wombat',\\\n",
    "                      'Vombatus ursinus',\\\n",
    "                      'missionaries')\n",
    "print(str(wally_wombat))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### An annoying feature\n",
    "\n",
    "You may have noticed an annoying feature of this class: it fails to distinguish between the use of \"a\" and \"an\".  How might you fix this using Python features we have studied?"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
