node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        pytest -v -s -k test_script.py
    }

}
