node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        cmd 'pytest -v -s test_script.py'
    }

}
