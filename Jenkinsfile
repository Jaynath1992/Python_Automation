node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        sh 'pytest -v -s test_script.py'
    }

}
