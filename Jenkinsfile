pipeline {
        agent any
        stages {
                parallel 'Build Phase': {
                        stage('Build Phase') {
                                steps {
                                        echo 'Build phase completed'
                                }
                        }, 'Stage Phase': {
                                stage('Testing Phase') {
                                        steps {
                                                echo 'Testing phase comepleted'
                                        }
                                }
                        }, 'Deploy Phase': {
                        stage('Deployment Phase') {
                                steps {
                                        echo 'Deployment completed'
                                }
                        }
                        }
                }    
                
        }

}
