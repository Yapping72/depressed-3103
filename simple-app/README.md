# Simple Web Application
* Containerized application built using Django with Postgres Backend.
* Files in the [basic_web directory](basic_web\basic_web) are default Django Configuration files.
* Files used to achieved homepage functionality can be found in the [website directory](basic_web\website)
    * The homepage has a search form that will perform validation and sanitization.
    * If XSS or SQL injection is detected, an error message is displayed, the input is cleared and user remains on home page.
    * If search deemed to be valid, they are redirected to the search page.

# Usage
1.  Clone repository and navigate to simple-app directory
    * ``git clone https://github.com/Yapping72/depressed-3103.git``
    * ``cd depressed-3103\simple-app``
3. ``docker-compose build``
4. ``docker-compose up -d``
5. You should be able to access homepage at:
    * localhost:8000/home
6. UI test can be found in [ui-test](..\ui-test\ui_tests.py)