#BHIS.org

## Source code for the website behavioralhealthis.org

## Instructions for local installation
1. Install pip if you have not already
   * To confirm if pip is installed, run  `pip --version`
   * If you don't have pip installed, you can install it by following the instructions [here](https://pip.pypa.io/en/stable/installing/).
 2. Install virtualenv if you have not already.
    * To confirm if virtualenv is installed, run  `virtualenv --version`
    * If you don't have virtualenv installed, you can install it by running `pip install virtualenv`.
 3. Create and activate a Python 2.7 virtual environment (instructions [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/) if needed)
 4. Clone the repo (instructions [here](https://help.github.com/articles/cloning-a-repository/) if needed)
 5. `cd Main`
 6. `pip install -r requirements.txt`

## Instructions for viewing the site locally
From within the top level directory of the repo:
`cd Main`
`python application.py`

## Running the app locally after the one-time setup:
 1. Activate the virtual environment
 2. `cd bhis.org`
 3. `cd Main`
 4. `python application.py`
 5. If successful, you should see the following in the terminal, and you can see the app by visiting http://127.0.0.1:5000/ :
 ```
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger pin code: 172-543-413
 ```

 ## Deployment
 $ cd Main
 $ eb deploy bhis
