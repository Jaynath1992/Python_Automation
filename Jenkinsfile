node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        bat 'pytest -v -s test_script.py'
    }

}
