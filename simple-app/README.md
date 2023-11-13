# Simple Web Application
* Built using Django with Postgres Backend.
* Files in the [basic_web directory](basic_web\basic_web) are default Django Configuration files.
* Files used to achieved homepage functionality can be found in the [website directory](basic_web\website)
    * The homepage has a search form that will perform validation and sanitization.
    * If XSS or SQL injection is detected, an error message is displayed, the input is cleared and user remains on home page.
    * If search deemed to be valid, they are redirected to the search page.
