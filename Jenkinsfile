pipeline {
    stages {
        stage('Git Checkout') {
            scm checkout
        }
        stage('Run test') {
            sh 'python -m pytest -v -s -k test_script.py'
        }
    }

}
