node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        bat 'pytest -v -s -k test_script.py'
    }

}
